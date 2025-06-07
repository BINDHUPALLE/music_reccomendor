import pickle
import streamlit as st
import gzip
import pandas as pd
st.set_page_config(page_title="Music Recommender", layout="wide")
# Load data and similarity matrix
music = pd.read_csv("filtered_music.csv")  
with gzip.open("top30_similar.pkl.gz", "rb") as f:
    similarity = pickle.load(f)
# Recommendation logic
def recommend(song):
    if song not in similarity:
        return [], [], []

    top_similar = similarity[song]

    recommended_music_names = []
    recommended_music_posters = []
    recommended_spotify_links = []

    for entry in top_similar[:5]:  # Get top 5 recommendations
        sim_song = entry["song"]
        artist = entry["artist"]

        # Get row in original music DataFrame
        row = music[(music['song'] == sim_song) & (music['artist'] == artist)]
        if not row.empty:
            row = row.iloc[0]
            recommended_music_names.append(row['song'])
            recommended_music_posters.append(row['album_cover_url'])
            recommended_spotify_links.append(row['spotify_url'])

    return recommended_music_names, recommended_music_posters, recommended_spotify_links

# Streamlit UI

st.header('🎵 Music Recommender System')

music_list = music['song'].dropna().unique()
selected_song = st.selectbox("🎧 Type or select a song from the dropdown", music_list)

if st.button('🔍 Show Recommendations'):
    names, posters, links = recommend(selected_song)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_container_width=True)
            st.markdown(f"**{names[i]}**")
            st.markdown(f"[Listen on Spotify]({links[i]})", unsafe_allow_html=True)
