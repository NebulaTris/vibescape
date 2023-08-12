import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import webbrowser
import cv2
import numpy as np
import mediapipe as mp
from keras.models import load_model
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="Vibescape",
    page_icon="🎵",
)

page_bg_img = """
<style>

div.stButton > button:first-child {
    all: unset;
    width: 120px;
    height: 40px;
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
    background: #0f001a;
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
background-image: url("https://images.unsplash.com/photo-1613327986042-63d4425a1a5d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
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
st.title("Vibescape")
st.sidebar.success("Select a page below.")

model = load_model("model.h5")
label = np.load("label.npy")

holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

if "run" not in st.session_state:
    st.session_state["run"] = ""

run = np.load("emotion.npy")[0]

try:
    emotion = np.load("emotion.npy")[0]
except:
    emotion = ""

    
class EmotionProcessor:
    def recv(self,frame):
        frm = frame.to_ndarray(format="bgr24")
        frm = cv2.flip(frm, 1)  
        res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
        
        lst = []
        if res.face_landmarks:
            for i in res.face_landmarks.landmark:
                lst.append(i.x - res.face_landmarks.landmark[1].x)
                lst.append(i.y - res.face_landmarks.landmark[1].y)
        
            if res.left_hand_landmarks:
                for i in res.left_hand_landmarks.landmark:
                    lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
            else:
                for i in range(42):
                    lst.append(0.0)
        
            if res.right_hand_landmarks:
                for i in res.right_hand_landmarks.landmark:
                    lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
            else:
                for i in range(42):
                    lst.append(0.0)
        
            lst = np.array(lst).reshape(1, -1)
        
            pred = label[np.argmax(model.predict(lst))]
            print(pred)
            cv2.putText(frm, pred, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            
            np.save("emotion.npy",np.array([pred]))
            
            emotion = pred
       
        drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
        drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS) 
        drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)
    
        return av.VideoFrame.from_ndarray(frm, format="bgr24")
    
st.header("Hello dear user! Welcome to Vibescape!")

if st.session_state["run"] != "false":
    webrtc_streamer(key="key", desired_playing_state=True , video_processor_factory=EmotionProcessor)
btn = st.button("Check your emotion")

if btn:
    if not(emotion):
        st.warning("Please wait for the emotion to be detected")
        
    else:
        np.save("emotion.npy",np.array([""]))
        st.session_state["run"] = run
        st.write("Your current emotion is: " ,emotion)
        st.subheader("Choose your streaming service")
        
col1, col2, col3 = st.columns(3)

with col1:
    btn = st.button("Spotify")
    if btn:
        switch_page("Spotify")

with col2:
    btn2 = st.button("Youtube")
    if btn2:
        switch_page("Youtube")

with col3:
    btn3 = st.button("Saavn")
    if btn3:
        switch_page("Saavn")