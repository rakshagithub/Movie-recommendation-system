import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
