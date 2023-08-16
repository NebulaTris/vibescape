import streamlit as st
import webbrowser
from streamlit_extras.app_logo import add_logo
import streamlit.components.v1 as components
from streamlit_player import st_player

page_bg_img = """
<style>
div.stButton > button:first-child {
    all: unset;
    width: 300px;
    height: 60px;
    font-size: 32px;
    background: transparent;
    border: none;
    position: relative;
    color: #f0f0f0;
    cursor: pointer;
    z-index: 1;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;

}
div.stButton > button:before, div.stButton > button:after {
    content: '';
    position: absolute;
    bottom: 0;
    right: 0;
    z-index: -99999;
    transition: all .4s;
}

div.stButton > button:before {
    transform: translate(0%, 0%);
    width: 100%;
    height: 100%;
    background: #331400;
    border-radius: 10px;
}
div.stButton > button:after {
  transform: translate(10px, 10px);
  width: 35px;
  height: 35px;
  background: #ffffff15;
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border-radius: 50px;
}

div.stButton > button:hover::before {
    transform: translate(5%, 20%);
    width: 110%;
    height: 110%;
}


div.stButton > button:hover::after {
    border-radius: 10px;
    transform: translate(0, 0);
    width: 100%;
    height: 100%;
}

div.stButton > button:active::after {
    transition: 0s;
    transform: translate(0, 5%);
}

[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1592838890225-2c052fa0cf34?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}

[data-testid="stSidebar"] > div:first-child {
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
background : black;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}
</style>
"""
add_logo("https://github.com/NebulaTris/vibescape/blob/main/logo.png?raw=true")

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Vibescape-Soundcloud")
st.sidebar.success("Soundcloud has been selected as your music player.")
st.write("You current emotion is: " , st.session_state["run"])

col1, col2 = st.columns(2)

with col1:
    hindi = st.button("Hindi")
    if hindi:
        if st.session_state["run"] == "Happy":
            st_player("https://soundcloud.com/imaginedragons/demons")
        elif st.session_state["run"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXdFesNN9TzXT?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["run"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7pS8tMgJgzQ8XSGpOajOqb?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["run"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7EZ4lWeM1OLxZYfGmhDbJI?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["run"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7vatYrf39uVaZ8G2cVtEik?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["run"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX0XUfTFmNBRM?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://www.jiosaavn.com/featured/best-of-romance-hindi/SBKnUgjNeMIwkg5tVhI3fw__" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)

    bengali = st.button("Bengali")
    marathi = st.button("Marathi")
   
with col2:
   english = st.button("English")
   punjabi = st.button("Punjabi")
   telugu = st.button("Telugu")