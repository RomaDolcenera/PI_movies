from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from functions import buscames

dfm = pd.read_csv("./Datasets_limpios/movies_dataset_clean.csv")
dfc = pd.read_csv("./Datasets_limpios/credits_dataset_clean.csv")

app = FastAPI()

#Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultad
# en la totalidad del dataset.
@app.get("/cantidad_filmaciones_mes/{mes}")
def read_item(mes: str):
    try:
        mes_numero = buscames(mes.lower())
    except ValueError:
        return {'error': 'El mes ingresado no se encuentra en la base de datos. Ingrese un mes válido en Español'}
    
    result_filter = dfm[dfm['release_month'] == mes_numero]
    cantidad_peliculas = len(result_filter)
    mensaje = f'Un total de {cantidad_peliculas} peliculas fueron estrenadas en el mes de {mes}'
    return {'mensaje': mensaje}

#Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en
# la totalidad del dataset.
@app.get("/cantidad_filmaciones_dia/{dia}")
def read_item(dia: str):
    name_dia = dia.lower()
    dfm['day_of_week'] = dfm['day_of_week'].str.lower()
    result_filter = dfm.loc[dfm['day_of_week'] == name_dia]
    
    if result_filter.empty:
        return {'error': 'El dia ingresado no se encuentra en la base de datos, ingrese un dia en Español.'}
    
    else:
        cantidad_peliculas = result_filter.shape[0]
        mensaje = f'{cantidad_peliculas} peliculas fueron estrenadas en el dia {dia}'
        return {'mensaje': mensaje}

#Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
@app.get("/cantidad_filmaciones_dia/{dia}")
def read_item(dia: str):
    name_dia = dia.lower()
    result_filter = dfm.loc[dfm['day_of_week'].str.lower() == name_dia]
    
    if result_filter.empty:
        return {'error': 'El dia ingresado no se encuentra en la base de datos, ingrese un dia en Español.'}
    
    else:
        cantidad_peliculas = result_filter.shape[0]
        mensaje = f'{cantidad_peliculas} peliculas fueron estrenadas en el dia {dia}'
        return {'mensaje':mensaje}
    
#Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones.
# La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple
# esta condición y que por ende, no se devuelve ningun valor.
@app.get('/votos_titulo/{titulo}')
def read_item(titulo: str):
    titulo = titulo.lower()
    result_filter = dfm.loc[dfm['title'].str.lower() == titulo]
    
    if result_filter.empty:
        return {'mensaje': 'La película ingresada no se encuentra en la base de datos, ingrese otro título'}
    votos = result_filter['vote_count'].values[0]
    promedio_votos = result_filter['vote_average'].values[0]
    
    if votos < 2000:
        return {'mensaje': 'La película no cumple con la condición de tener al menos 2000 valoraciones, no se devuelve ningún valor'}
    
    titulo_original = result_filter['title'].values[0]
    anio_estreno = result_filter['release_year'].values[0]
    mensaje = f'La película {titulo_original} fue estrenada en el año {anio_estreno} La misma cuenta con un total de {votos} valoraciones, con un promedio de {promedio_votos}'
    
    return {'mensaje': mensaje}

#Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno
# Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores
@app.get('/get_actor/{nombre_actor}')
def read_item(nombre_actor: str):
    actor = dfc.loc[dfc['actores'].str.lower().apply(lambda x: nombre_actor.lower() in x), 'id']
    
    if actor.empty:
        return f"Error: No se encontraron coincidencias para el actor {nombre_actor}."
    
    else:
        movies = dfm[dfm.id.isin(actor)]
        film_count  = movies.shape[0]
        total_gross_return  = movies['revenue'].sum()
        average_gross_return  = total_gross_return / film_count if film_count > 0 else 0
        mensaje = f"El actor {nombre_actor} ha participado de {film_count} cantidad de filmaciones, el mismo ha conseguido un retorno de {total_gross_return} con un promedio de {average_gross_return} por filmación"
        return {'mensaje': mensaje}
            

#Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
# Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
@app.get("/get_director/{director}")
def read_item(director: str):
    name_director = director.lower()
    result_filter = dfc.loc[dfc['directores'].str.lower().apply(lambda x: name_director in x)]
    
    if result_filter.empty:
        return {"error": "El director ingresado no se encuentra en la base de datos, pruebe con el nombre completo o ingrese otro director"}
    
    else:
        id_movies = result_filter['id'].to_list()
        movies_director = dfm[dfm['id'].isin(id_movies)]
        best_movie = movies_director.loc[movies_director['popularity'].idxmax()]
        column_rename = {'title': 'Titulo', 'release_year': 'Año de lanzamiento', 'return': 'Retorno', 'budget': 'Costo', 'revenue': 'Ganancia'}
        list_movies = movies_director[['title','release_year', 'return', 'budget', 'revenue']].rename(columns=column_rename).to_dict('records')
        return { "Datos del Director": name_director, "Mejor Pelicula": best_movie['title'],
            "Lista de Peliculas": list_movies
        }
        
# Machine Learning code
def get_recommendations(titulo, dfm):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(dfm['title'])
    search_vector = tfidf_vectorizer.transform([titulo])
    similar_score = cosine_similarity(search_vector, tfidf_matrix).flatten()
    dfm['score'] = similar_score
    dfm = dfm.sort_values(by='score', ascending=False)
    dfm = dfm[dfm['title'].str.lower() != titulo.lower()]
    top_5_titles = dfm.head(5)['title'].tolist()
    return top_5_titles

@app.get("/recomendacion/{titulo}")
def read_item(titulo: str):
    if titulo.lower() not in dfm['title'].str.lower().values:
        return {"error": "La pelicula ingresada no se encuentra en la base de datos, pruebe con el nombre completo o ingrese otra pelicula"}

    recommend = get_recommendations(titulo, dfm)

    if len(recommend) == 0:
        return {"error": "No se encontraron recomendaciones para la película ingresada."}
    
    else:
        return {"Peliculas similares recomendadas": recommend}
    
@app.get("/health")
def health():
    return {"status": "ok"}
