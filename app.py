import pickle
import streamlit as st
import json
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=af97cdf3f0b222a40c26e0c1fba660ec".format(movie_id)
    data = requests.get(url)
    data = data.json()
    #st.text(data)
    poster_path = data['poster_path']
    #data=json.loads(url.text)
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        title=movies.iloc[i[0]].title
       #  response = requests.get("https://api.themoviedb.org/3/search/movie?api_key=af97cdf3f0b222a40c26e0c1fba660ec&query="+title)
       #  jd=json.loads(response.text)
       #  arr =jd.get("results")
       #  movie_id=0
       #
       # # for x in arr:
       #     if(x.get("title")==title):
       #         movie_id=x.get("id")
        movie_id=movies.iloc[i[0]].id
        #st.text(movie_id)


        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)


    return recommended_movie_names , recommended_movie_posters



st.header('Movie Recommender System')
movies = pickle.load(open('./movie_list.pkl','rb'))
similarity = pickle.load(open('./similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.text("\n")
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.text("\n")
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.text("\n")
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.text("\n")
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.text("\n")
        st.image(recommended_movie_posters[4])