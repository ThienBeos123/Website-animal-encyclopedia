import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Bách khoa động vật",
    page_icon=":book:",
    layout="wide")

st.title("**Bách khoa động vật** :palm_tree:")
chosen_animal = ""
col1, col2, col3, col4, col5 = st.columns(5)

animal_info = {"Khỉ":
                   {"image": "required elements/Monkey properties/Monkey image.jpg",
                    "video": "https://www.youtube.com/watch?v=NjgL7Pumb4Q",
                    "audio": open("required elements/Monkey properties/Monkey sound.mp3", "rb"),
                    "emoji": ":monkey:"},

               "Sư tử":
                   {"image": "required elements/Lion properties/Lion image.jfif",
                    "video": "https://www.youtube.com/watch?v=uFIEIFLJtSQ",
                    "audio": open("required elements/Lion properties/Lion sound.mp3", "rb"),
                    "emoji": "🦁"},

               "Mèo":
                   {"image": "required elements/Cat properties/Cat image.jfif",
                    "video": "https://www.youtube.com/watch?v=8ImtbHTX9gc",
                    "audio": open("required elements/Cat properties/Cat sound.mp3", "rb"),
                    "emoji": ":cat:"},

               "Cá heo":
                   {"image": "required elements/Dolphin properties/Dolphin image.jfif",
                    "video": "https://www.youtube.com/watch?v=jM6WTXSmG78",
                    "audio": open("required elements/Dolphin properties/Dolphin sound.mp3", "rb"),
                    "emoji": ":dolphin:"},

               "Hươu cao cổ":
                   {"image": "required elements/Giraffe properties/Giraffe image.webp",
                    "video": "https://www.youtube.com/watch?v=P_ckAbOr0r4",
                    "audio": open("required elements/Giraffe properties/Giraffe sound.mp3", "rb"),
                    "emoji": "🦒"}
               }


def displaying_content(b):
    if b != "":
        st.header(f"**{b}** {animal_info[b]["emoji"]}")
        st.image(animal_info[b]["image"], caption=f"{b} trong môi trường tự nhiện của nó")
        st.header(f"**Âm thanh của {b}** :musical_note:")
        st.audio(animal_info[b]["audio"], format="audio/mp3")
        st.header(f"**Video về {b}** :movie_camera:")
        st.video(animal_info[b]["video"], format="video/mp4")
    else:
        pass


with col1:
    b1 = st.button("Khỉ")
with col2:
    b2 = st.button("Sư tử")
with col3:
    b3 = st.button("Mèo")
with col4:
    b4 = st.button("Cá heo")
with col5:
    b5 = st.button("Hươu cao cổ")

if b1:
    chosen_animal = "Khỉ"
if b2:
    chosen_animal = "Sư tử"
if b3:
    chosen_animal = "Mèo"
if b4:
    chosen_animal = "Cá heo"
if b5:
    chosen_animal = "Hươu cao cổ"

displaying_content(chosen_animal)

with st.sidebar:
    pass
