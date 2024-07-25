from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

dfm = pd.read_csv("/Datasets_limpios/movies_dataset_clean.csv.csv",sep = ',', encoding="UTF-8", low_memory=False)
dfc = pd.read_csv("/Datasets_limpios.csv/credits_dataset_clean.csv")

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de películas"}


#Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultad
# en la totalidad del dataset.
@app.get("/cantidad_filmaciones_mes/{mes}")
def read_item(mes: str):
    name_mes = mes.lower()
    result_filter = dfm.loc[dfm['release_month'].str.lower().apply(lambda x: name_mes in x)]
    if result_filter.empty:
        return{'error: El mes ingresado no se encuentra en la base de datos. Ingrese un mes valido en Español'}
    else:
        print(result_filter)

#Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en
# la totalidad del dataset.

#Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.


#Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones.
# La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple
# esta condición y que por ende, no se devuelve ningun valor.


#Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno.
# Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores.
@app.get("/get_actor/{actor}")
def read_item(director: str):
    name_actor = actor.lower()
    result_filter = dfc.loc[dfc['actor'].str.lower().apply(lambda x: name_actor in x)]
    if result_filter.empty:
        return {"error": "El actor ingresado no se encuentro en la base de datos, pruebe con el nombre completo o ingrese otro actor"}
    else:
        id_actor = result_filter['id'].to_list()
        movies_director = dfm[dfm['id'].isin(id_movies)]
        best_movie = movies_director.loc[movies_director['popularity'].idxmax()]
        column_rename = {'title': 'Titulo', 'release_year': 'Año de lanzamiento', 'return': 'Retorno', 'budget': 'Costo', 'revenue': 'Ganancia'}
        list_movies = movies_director[['title','release_year', 'return', 'budget', 'revenue']].rename(columns=column_rename).to_dict('records')
        return {
            "Director": name_director,
            "Mejor Pelicula": best_movie['title'],
            "Lista de Peliculas": list_movies
            }


#Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
@app.get("/get_director/{director}")
def read_item(director: str):
    name_director = director.lower()
    result_filter = dfc.loc[dfc['directors'].str.lower().apply(lambda x: name_director in x)]
    if result_filter.empty:
        return {"error": "El director ingresado no se encuentro en la base de datos, pruebe con el nombre completo o ingrese otro director"}
    else:
        id_movies = result_filter['id'].to_list()
        movies_director = dfm[dfm['id'].isin(id_movies)]
        best_movie = movies_director.loc[movies_director['popularity'].idxmax()]
        column_rename = {'title': 'Titulo', 'release_year': 'Año de lanzamiento', 'return': 'Retorno', 'budget': 'Costo', 'revenue': 'Ganancia'}
        list_movies = movies_director[['title','release_year', 'return', 'budget', 'revenue']].rename(columns=column_rename).to_dict('records')
        return {
            "Director": name_director,
            "Mejor Pelicula": best_movie['title'],
            "Lista de Peliculas": list_movies
            }


@app.get("/recomendacion/{titulo}")
def read_item(titulo: str):
    def get_recommendations(titulo, dfm):
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(dfm['title'])
        search_vector = tfidf_vectorizer.transform([titulo])
        similar_score = cosine_similarity(search_vector, tfidf_matrix).flatten()
        dfm['score'] = similar_score
        dfm = dfm.sort_values(by='score', ascending=False)
        result_dict = {}
        for index in range(5):
            result_dict[dfm.iloc[index]['title']] = dfm.iloc[index]['score']
        return result_dict

    recommend = get_recommendations(titulo, dfm)

    if len(recommend) < 0:
        return {"error": "La pelicula ingresada no se encuentro en la base de datos, pruebe con el nombre completo o ingrese otra pelicula"}
    else:
        return {"Peliculas similares recomendadas": recommend}
    
@app.get("/health")
def health():
    return {"status": "ok"}