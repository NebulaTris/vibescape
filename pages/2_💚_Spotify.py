import streamlit as st
import webbrowser
from streamlit_extras.app_logo import add_logo
import streamlit.components.v1 as components

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
    background: #001a00;
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
background-image: url("https://images.unsplash.com/photo-1581084324492-c8076f130f86?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
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
st.title("Vibescape-Spotify")
st.sidebar.success("Spotify has been selected as your music player.")
st.write("You current emotion is: " , st.session_state["run"])

col1, col2 = st.columns(2)

with col1:
    hindi = st.button("Hindi")
    if hindi:
        if st.session_state["run"] == "Happy":
            # webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD?si=df5b7bbf752b4e11")
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWTwbZHrJRIgD?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["run"] == "Sad":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT")
        elif st.session_state["run"] == "Angry":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/7pS8tMgJgzQ8XSGpOajOqb")
        elif st.session_state["run"] == "Fear":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7EZ4lWeM1OLxZYfGmhDbJI")
        elif st.session_state["run"] == "Surprise":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7vatYrf39uVaZ8G2cVtEik")
        elif st.session_state["run"] == "Neutral":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DX0XUfTFmNBRM")
        else:
            webbrowser.open_new_tab("https://open.spotify.com/playlist/3sKYXN4FEWLpg4FiJlxSrN")
            
    bengali = st.button("Bengali")
    if bengali:
        if st.session_state["run"] == "Happy":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD?si=df5b7bbf752b4e11")
        elif st.session_state["run"] == "Sad":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT")
        elif st.session_state["run"] == "Angry":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/7pS8tMgJgzQ8XSGpOajOqb")
        elif st.session_state["run"] == "Fear":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7EZ4lWeM1OLxZYfGmhDbJI")
        elif st.session_state["run"] == "Surprise":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7vatYrf39uVaZ8G2cVtEik")
        elif st.session_state["run"] == "Neutral":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DX0XUfTFmNBRM")
        else:
            webbrowser.open_new_tab("https://open.spotify.com/playlist/3sKYXN4FEWLpg4FiJlxSrN")
            
    marathi = st.button("Marathi")
    if marathi:
        if st.session_state["run"] == "Happy":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD?si=df5b7bbf752b4e11")
        elif st.session_state["run"] == "Sad":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT")
        elif st.session_state["run"] == "Angry":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/7pS8tMgJgzQ8XSGpOajOqb")
        elif st.session_state["run"] == "Fear":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7EZ4lWeM1OLxZYfGmhDbJI")
        elif st.session_state["run"] == "Surprise":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7vatYrf39uVaZ8G2cVtEik")
        elif st.session_state["run"] == "Neutral":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DX0XUfTFmNBRM")
        else:
            webbrowser.open_new_tab("https://open.spotify.com/playlist/3sKYXN4FEWLpg4FiJlxSrN")
   
with col2:
   english = st.button("English")
   if english:
        if st.session_state["run"] == "Happy":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD?si=df5b7bbf752b4e11")
        elif st.session_state["run"] == "Sad":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT")
        elif st.session_state["run"] == "Angry":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/7pS8tMgJgzQ8XSGpOajOqb")
        elif st.session_state["run"] == "Fear":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7EZ4lWeM1OLxZYfGmhDbJI")
        elif st.session_state["run"] == "Surprise":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7vatYrf39uVaZ8G2cVtEik")
        elif st.session_state["run"] == "Neutral":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DX0XUfTFmNBRM")
        else:
            webbrowser.open_new_tab("https://open.spotify.com/playlist/3sKYXN4FEWLpg4FiJlxSrN")
            
   punjabi = st.button("Punjabi")
   if punjabi:
        if st.session_state["run"] == "Happy":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD?si=df5b7bbf752b4e11")
        elif st.session_state["run"] == "Sad":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT")
        elif st.session_state["run"] == "Angry":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/7pS8tMgJgzQ8XSGpOajOqb")
        elif st.session_state["run"] == "Fear":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7EZ4lWeM1OLxZYfGmhDbJI")
        elif st.session_state["run"] == "Surprise":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7vatYrf39uVaZ8G2cVtEik")
        elif st.session_state["run"] == "Neutral":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DX0XUfTFmNBRM")
        else:
            webbrowser.open_new_tab("https://open.spotify.com/playlist/3sKYXN4FEWLpg4FiJlxSrN")
            
   telugu = st.button("Telugu")
   if telugu:
        if st.session_state["run"] == "Happy":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD?si=df5b7bbf752b4e11")
        elif st.session_state["run"] == "Sad":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT")
        elif st.session_state["run"] == "Angry":
           webbrowser.open_new_tab("https://open.spotify.com/playlist/7pS8tMgJgzQ8XSGpOajOqb")
        elif st.session_state["run"] == "Fear":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7EZ4lWeM1OLxZYfGmhDbJI")
        elif st.session_state["run"] == "Surprise":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/7vatYrf39uVaZ8G2cVtEik")
        elif st.session_state["run"] == "Neutral":
            webbrowser.open_new_tab("https://open.spotify.com/playlist/37i9dQZF1DX0XUfTFmNBRM")
        else:
            webbrowser.open_new_tab("https://open.spotify.com/playlist/3sKYXN4FEWLpg4FiJlxSrN")