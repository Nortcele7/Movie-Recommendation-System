import streamlit as st
import pickle
import pandas as pd

st.title("Movie Recommendation System")

movies_dict = pickle.load(open("movies_dict.pkl","rb"))
movies_df = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl","rb"))

def recommend_movie(movie):
    movie_index = movies_df[movies_df["title"]==movie].index[0]
    movies_index_lst = [x[0] for x in sorted(list(enumerate(similarity[movie_index])),reverse=True, key=lambda x:x[1])[1:6]]

    recommended_movies = [movies_df.iloc[i].title for i in movies_index_lst]

    return recommended_movies


movie_selected = st.selectbox(
    'Movies List',
    movies_df['title'].values
)

if st.button("Recommend"):
    recommendations = recommend_movie(movie_selected)
    for i in recommendations:
        st.write(i)