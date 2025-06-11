# ui.py
import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="Gif Generator",
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/Nafisatibrahim/Giffy-gif-generator',
            'Report a bug': 'mailto:nafisat.l@outlook.com',
            'About': 'This is a Gif Generator app built with Streamlit.'
        }
    )

def render_header():
    st.title("Gif Generator")
    st.markdown("""
    ## Welcome to the Gif Generator App!
    This app allows you to create and customize GIFs with ease.  
    Use the sidebar to navigate through different functionalities.
    """)

def render_sidebar():
    st.sidebar.title("Navigation")
    st.sidebar.markdown("""
- Home  
- 🎯 Generate a GIF
- 📊 Top 3 GIFs
- 🎲 Random GIF
""")

def render_footer():
    st.markdown("""
---
Made with ❤️ by [Nafisat Ibrahim](https://github.com/Nafisatibrahim)
""")


