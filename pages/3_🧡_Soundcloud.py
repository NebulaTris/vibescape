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
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Sad":
           st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Angry":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Fear":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Surprise":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Neutral":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        else:
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")

    bengali = st.button("Bengali")
    if bengali:
        if st.session_state["run"] == "Happy":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Sad":
           st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Angry":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Fear":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Surprise":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Neutral":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        else:
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
    
    marathi = st.button("Marathi")
    if marathi:
        if st.session_state["run"] == "Happy":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Sad":
           st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Angry":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Fear":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Surprise":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        elif st.session_state["run"] == "Neutral":
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
        else:
            st_player("https://soundcloud.com/miss_happy/sets/hindi-songs")
   
with col2:
   english = st.button("English")
   if english:
        if st.session_state["run"] == "Happy":
            st_player("https://soundcloud.com/gabriela-astudillo-398435247/sets/happy-english-music")
        elif st.session_state["run"] == "Sad":
           st_player("https://soundcloud.com/jishnu-rajwani-695997535/sets/famous-english-sad-songs-of")
        elif st.session_state["run"] == "Angry":
            st_player("https://soundcloud.com/thomashayden/sets/tech-house-vibes-only")
        elif st.session_state["run"] == "Fear":
            st_player("https://soundcloud.com/tito-tito-675324717/sets/horror-english")
        elif st.session_state["run"] == "Surprise":
            st_player("https://soundcloud.com/manea-claudia/sets/top-love-songs-2022-playlist-1")
        elif st.session_state["run"] == "Neutral":
            st_player("https://soundcloud.com/sejal-agarkar/sets/english-songs-hits")
        else:
            st_player("https://soundcloud.com/mona-khaled-858700005/sets/english-cringe")
            
   punjabi = st.button("Punjabi")
   if punjabi:
        if st.session_state["run"] == "Happy":
            st_player("https://soundcloud.com/danyal-safir/sets/punjabi-party-songs-2022")
        elif st.session_state["run"] == "Sad":
           st_player("https://soundcloud.com/tania-tania-658084779/sets/best-punjabi-sad-songs-2023")
        elif st.session_state["run"] == "Angry":
            st_player("https://soundcloud.com/jas-singh-31/sets/gym-punjabi-playlist")
        elif st.session_state["run"] == "Fear":
            st_player("https://soundcloud.com/user-94762183/timmy-trumpet-punjabi-x-code_pandorum-murda-fvck-riddim-x-horror-noise-ofdts-mashup")
        elif st.session_state["run"] == "Surprise":
            st_player("https://soundcloud.com/itslovesmusic/sets/top-50-punjabi-songs-2022-1")
        elif st.session_state["run"] == "Neutral":
            st_player("https://soundcloud.com/tania-tania-658084779/sets/best-punjabi-hits-songs-2023")
        else:
            st_player("https://soundcloud.com/gvdotbnerxpu/sets/bad-punjabi-remix")
            
   telugu = st.button("Telugu")
   if telugu:
        if st.session_state["run"] == "Happy":
            st_player("https://soundcloud.com/sumit-indoria/sets/telugu-party-time")
        elif st.session_state["run"] == "Sad":
           st_player("https://soundcloud.com/user-738522704/sets/sad-telugu-songs")
        elif st.session_state["run"] == "Angry":
            st_player("https://soundcloud.com/user-692822299/sets/telugu-workout-remix")
        elif st.session_state["run"] == "Fear":
            st.write("No such playlist found , hence default playlist is being played.")
            st_player("https://soundcloud.com/vinod-kumar-761560211/sets/telugu-songs-regular-update")
        elif st.session_state["run"] == "Surprise":
            st_player("https://soundcloud.com/vinod-kumar-761560211/sets/telugu-songs-regular-update")
        elif st.session_state["run"] == "Neutral":
            st_player("https://soundcloud.com/vinod-kumar-761560211/sets/telugu-songs-regular-update")
        else:
            st.write("No such playlist found , hence default playlist is being played.")
            st_player("https://soundcloud.com/vinod-kumar-761560211/sets/telugu-songs-regular-update")
   