# app.py
import streamlit as st
from ui import setup_page, render_header, render_sidebar, render_footer
from utils import get_gif_url, get_top_gifs, get_random_gif

# Setup UI
setup_page()
render_header()
render_sidebar()

# API key
api_key = "CArMIVIACGeMOos0APv9R5X27T1G4XHg"

# User input
st.subheader("🎯 Try a Gen-Z Term")
user_input = st.text_input("Enter a Gen-Z slang term:")

# Translate to GIF
if st.button("Translate"):
    if user_input:
        with st.spinner("Searching for the perfect GIF..."):
            gif_url = get_gif_url(user_input, api_key)
            if gif_url:
                st.image(gif_url, caption=f"GIF for '{user_input}'", width=300)
            else:
                st.warning("Couldn't find a GIF. Try a different word.")
    else:
        st.warning("Please enter a Gen-Z word first.")

# Top 3 GIFs section
st.subheader("🎬 Top 3 GIFs for your term")
if st.button("Show Top 3 GIFs"):
    if user_input:
        with st.spinner("Fetching top 3 trending GIFs..."):
            top_gifs = get_top_gifs(user_input, api_key)
            if top_gifs:
                cols = st.columns(len(top_gifs))
                for i, gif_url in enumerate(top_gifs):
                    with cols[i]:
                        st.image(gif_url, use_container_width=True)
            else:
                st.warning("No top GIFs found for that term.")
    else:
        st.warning("Please enter a Gen-Z word first.")

# Random GIF section
st.subheader("🎲 Feeling Lucky?")
if st.button("Random GIF"):
    with st.spinner("Fetching a random mood..."):
        gif_url = get_random_gif(api_key)
        if gif_url:
            st.image(gif_url, caption="Random Giphy Mood", width=300)
        else:
            st.warning("Couldn't load a random GIF. Try again.")

# Footer
render_footer()
