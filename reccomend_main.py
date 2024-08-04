
import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('movies_dataset.csv')
movies = df[['id','title','overview','genre']]
movies['tags'] = movies['overview']+movies['genre']
new_data = movies.drop(['overview','genre'],axis=1)

tfidf = TfidfTransformer(stop_words = 'english',max_features=10000)
vector = tfidf.fit_transform(new_data['tags'].values.astype('U')).toarray()

similarity = cosine_similarity(vector)
movies = pickle.load(open('movies_list.pkl','rb'))
#similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = movies['title'].values

st.header('Movie Recommender System')
selectvalue=st.selectbox('Select Movie from dropdown',movies_list)



def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    recommended_movie=[]
    for i in distance[1:6]:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie


if st.button("Show Recommend"):
    movie_name = recommend(selectvalue)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])
