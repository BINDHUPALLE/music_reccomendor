# music_recommender
## 🎵 Music Recommender System
Welcome to the Music Recommender System — a smart app that helps you discover songs based on lyrics and artist similarity! Whether you're vibing with something mellow or want a track that feels just like your favorite, this tool is designed to make music discovery intuitive and enjoyable.

## 📌 What This Project Does
This app takes a song name as input and recommends 5 similar songs based on:

Lyrics content (semantic similarity using NLP)

Artist context

Spotify metadata (album art + direct listen links)

All recommendations are powered by sentence embeddings (via SentenceTransformer) and cosine similarity, with a clean UI built using Streamlit.

## 🔍 How It Works
Text Preprocessing:

Cleans and standardizes lyrics and artist names.

Removes punctuation and special characters.

Embedding Generation:

Lyrics are encoded using all-MiniLM-L6-v2 from SentenceTransformers.

A weighted combination of lyrics and artist embeddings is used to capture both textual and contextual info.

Similarity Calculation:

Cosine similarity is computed between all songs.

A dictionary of top 30 similar tracks is created and compressed with gzip + pickle.

Interactive UI:

Select a song and instantly see recommendations with album covers and direct Spotify links.


## 📁 Project Structure
bash
Copy code
- app.py : Streamlit UI
- filtered_music.csv  : Cleaned data with lyrics, artists, and Spotify info
- top30_similar.pkl.gz  : Precomputed similarity dictionary
- spotify.csv : Raw input lyrics + song/artist data
- requirements.txt  : Dependencies
- README.md   : You are here!
##🧠 Models and Libraries Used
SentenceTransformers (all-MiniLM-L6-v2)

spotipy for Spotify API access

pandas, numpy, sklearn, gzip, pickle

Streamlit for the frontend
