<h1 align=center>P.I Machine Learning Operations (MLOps)</h1>

<p align="center"><img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300></p>


## *Introducción:*
Como Data Scientist en una empresa de agregación de plataformas de streaming, fui asignado a desarrollar un sistema de recomendación de películas desde cero. Esta tarea era crucial para mejorar la experiencia del usuario y aumentar el engagement en nuestra plataforma.
Al iniciar el proyecto, me encontré con que los datos disponibles eran inmaduros y desorganizados. Asumí la responsabilidad de transformar estos datos en información útil, lo que implicó realizar labores de Data Engineer para la recolección, transformación y carga de los datos (ETL). 
Este proceso incluyó la limpieza y estructuración de los datos provenientes de fuentes de streaming.
Con los datos preparados, desarrollé un modelo de recomendación utilizando técnicas de Machine Learning. El modelo fue entrenado para ofrecer sugerencias personalizadas a los usuarios, optimizando tanto la precisión como la relevancia de las recomendaciones.
Finalmente, desplegué el modelo en Render, asegurando su integración y funcionamiento continuo. Este proyecto no solo mejoró significativamente la experiencia del usuario, sino que también demostró nuestra capacidad para innovar y enfrentar desafíos complejos en un entorno de datos real.

## *Objetivos:*
- Limpieza y estructuracion de los datos.
- Desarrollo de un Sistema de Recomendacion de Peliculas.
- Desarrollo de la API.
- Deploy en Render.

## *Desarrollo*
1- Data Engineer: 
- *Extracción, Transformación y Limpieza de los datos(ETL):* Se realiza la tarea de extracción de los datos de los archivos otorgados, se detalla en cada caso las desiciones tomadas a traves de un markdown, limpieza, normalizacion para su posterior uso. Los códigos realizados se pueden observar dentro de la carpeta [ETL y EDA](https://github.com/RomaDolcenera/PI_movies/tree/master/ETL).
- *Datos Procesados (csv final):* Los datos ya tratados mediante el ETL se encuentran en la carpeta [Datasets Limpios](https://github.com/RomaDolcenera/PI_movies/tree/master/Datasets_limpios).
  
2- Desarrollo del Software:
- *Desarollo de la API:* Para el desarrollo de la API se utiliza siguiente código: [main.py](https://github.com/RomaDolcenera/PI_movies/blob/master/main.py)
- *Virtualizacion y Deployment:* Se realizó la virtualización y el despliegue de la infraestructura necesaria para que la API esté disponible y sea accesible para futuras consultas.

## Tecnología utilizada:
 El proyecto fue desarrollado en *Python*, se utilizaron diversas librerias como:
 - *Pandas y Numpy*: Para la carga y limpieza y transformacion de los datos.
 - *Matplotlib, Seaborn, Wordcloud*: Para el Eda.
 - *Sckit-learn*: Para el sistema de recomendacion.

## Herramientas Utilizadas:
- Visual Studio Code: Herramienta utilizada para el desarrollo del proyecto.
- FastApi: Para consultas.
- Render: Servicio en la nube para la implementacion del modelo de ML.

### Links de interes:

- Los siguientes links te llevaran a la documentacion de cada libreria.
  
<a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" /></a><a href="https://numpy.org/"><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" /></a><a href="https://matplotlib.org/"><img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="Matplotlib" /></a><a href="https://seaborn.pydata.org/"><img src="https://img.shields.io/badge/Seaborn-%2370399F.svg?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn" /></a><a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn" /></a>

- Los siguientes links te llevaran a las paginas oficiales de las herramientas utilizadas
  
<a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=ffffff" alt="Visual Studio Code" /></a><a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI" /></a><a href="https://render.com/"><img src="https://img.shields.io/badge/Render-46E3B7.svg?style=for-the-badge&logo=Render&logoColor=white" alt="Render" /></a>

- El siguientes link te llevaran a los Datasets originales
 
<a href="https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5"><img src="https://media.geeksforgeeks.org/wp-content/uploads/20230908123137/Dataset---Examples-Features-and-Properties.png" alt="Dataset" width="100" /></a>

- El siguiente link te llevara al Diccionario de Datos con las descripciones de las columnas disponibles en el dataset.

<a href="https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit?gid=0#gid=0"><img src="https://cdn-icons-png.flaticon.com/512/5402/5402392.png" alt="Google Sheets" width="50" /></a>

- El siguiente link te llevara al **Deploy en Render**:

<a href="https://pi-movies-czqp.onrender.com"><img src="https://img.shields.io/badge/Render-46E3B7.svg?style=for-the-badge&logo=Render&logoColor=white" alt="Render" /></a>


## Desarrollo de la API:
Se disponibilizan los datos ya trabajados en FastAPI, para su correcta comprension se detalla a continuacion los endpoints:
- Def cantidad_filmaciones_mes(mes): Debe ingresar un mes en idioma Español, la consulta retornara el total de peliculas que fueron estrenadas en el mes solicitado.
- Def cantidad_filmaciones_dia(dia): Debe ingresar un dia de la semana en idioma Español, la consulta retornara la cantidad de peliculas que fueron estrenadas en el dia solicitado.
- def score_titulo(titulo): Debe ingresar el titulo de la pelicula que se desea consultar, la consulta retornara el titulo de la pelicula consultada el año que fue lanzada, y su popularidad.
- def votos_titulo(titulo): Debe ingresar el titulo de la pelicula que se desea consultar, la consulta retornara el titulo de la pelicula consultada,el año que fue lanzada, su valoracion y promedio. Dicho endpoint solo tomara en cuenta las filmaciones que tienen al menos 2000 valoraciones.
- def get_actor(nombre_actor): Debe ingresar el Nombre y Apellido del actor a consultar, dicha consulta retornara el nombre y apellido del actor, la cantidad total de filmaciones en las que ha participado, su retorno y promedio de ganancia.
- def get_director(director): Debe ingresar el Nombre y Apellido del director a consultar, dicha consulta retornara el nombre y apellido del director, el exito medido a traves del retorno y una lista con el nombre de cada pelicula que dirigio, fecha de lanzamiento, retorno indivicual, costo y ganancia de las mismas.

Sistema de recomendacion de peliculas en ML:
- def recomendaciones(titulo): Debe ingresar el nombre de la pelicula y el sistema recomendara un total de 5 filmaciones recomendadas.

## Proyecto creado por:

<a href="https://www.linkedin.com/in/rociomarquezz/"><img src="./imagenes/rm.jpg"/></a>

**Haz click en la imagen para ver mi perfil en LinkedIn**

¡Muchas gracias por dedicarle tiempo a la lectura de mi primer proyecto! 

Saludos cordiales


