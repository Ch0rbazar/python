import streamlit as st

st.set_page_config(page_title="Spotify Demo", layout="wide")

# --- Sidebar ---
st.sidebar.title("Spotify Demo")
selected_menu = st.sidebar.radio("Menu", ["Home", "Search", "Your Library"])

# --- Header ---
st.title("🎵 Spotify Demo")

# --- Home Page (Mock Data) ---
if selected_menu == "Home":
    st.header("Featured Playlists")
    cols = st.columns(3)

    playlists = [
        ("Chill Vibes", "Relaxing music for focus."),
        ("Top Hits", "Trending songs right now."),
        ("Workout Mix", "High-energy gym tracks."),
    ]

    for col, (name, desc) in zip(cols, playlists):
        col.image("https://via.placeholder.com/300x300.png?text=Playlist", use_column_width=True)
        col.subheader(name)
        col.write(desc)
        col.button(f"Play {name}")

# --- Search Page ---
elif selected_menu == "Search":
    st.header("Search Music")
    query = st.text_input("Search for songs, artists, or albums")

    if query:
        st.write(f"Showing results for **{query}**")
        st.image("https://via.placeholder.com/100x100.png?text=Result")
        st.write("Mock Song - Mock Artist")
        st.button("Play")

# --- Library Page ---
elif selected_menu == "Your Library":
    st.header("Your Library")
    st.write("Saved playlists and albums will appear here.")
    st.image("https://via.placeholder.com/200x200.png?text=Your+Playlist")
    st.subheader("My Chill Mix")
