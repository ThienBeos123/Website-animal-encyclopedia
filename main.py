import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Bách khoa động vật",
    page_icon=":book:",
    layout="wide")

st.title("**Bách khoa động vật** :palm_tree:")
chosen_animal = ""
col1, col2, col3, col4, col5 = st.columns(5)
col6, col7 = st.columns([1.5, 1])

animal_info = {"Khỉ":
                   {"image": "required elements/Monkey properties/Monkey image.jpg",
                    "video": "https://www.youtube.com/watch?v=NjgL7Pumb4Q",
                    "audio": open("required elements/Monkey properties/Monkey sound.mp3", "rb"),
                    "emoji": ":monkey:",
                    "general facts": ["Động vật có vú", "infraorder Simiiformes"],
                    "fun facts": ["Khỉ có thể dùng dụng cụ và giao tiếp cùng loài na ná con người",
                                  "Khỉ có thể nhận ra chính nó trong gương, khác so với các loài khác",
                                  "Khỉ có cảm xúc khá giống người"]},

               "Sư tử":
                   {"image": "required elements/Lion properties/Lion image.jfif",
                    "video": "https://www.youtube.com/watch?v=uFIEIFLJtSQ",
                    "audio": open("required elements/Lion properties/Lion sound.mp3", "rb"),
                    "emoji": "🦁",
                    "general facts": ["Động vật có vú", "Panthera leo"],
                    "fun facts": ["Sư tử không chăm chỉ như ta nghĩ, với việc nó ngủ trung bình tận _**20 tiếng**_! một ngày :sleeping:",
                                  "Sư tử cái :large_purple_square: lại đảm nhiệm vai trò đi săn, còn sư tử đực :large_blue_square: lại đảm nhiện việc chông lo con cái",
                                  "Sư tử là một loại mèo :cat:"]},

               "Mèo":
                   {"image": "required elements/Cat properties/Cat image.jfif",
                    "video": "https://www.youtube.com/watch?v=8ImtbHTX9gc",
                    "audio": open("required elements/Cat properties/Cat sound.mp3", "rb"),
                    "emoji": ":cat:",
                    "general facts": ["Động vật có vú", "Felis catus"],
                    "fun facts": ["Mèo có thể nhau cao gấp _**6 lần!**_ chiều cao cơ thể ",
                                  "Mèo không kêu 'meo meo' với các con mèo khác, nó chỉ kêu như thế với con người",
                                  "Mèo có thể xoay đôi tai của nó _**180 độ!**_ :arrows_counterclockwise:"]},

               "Cá heo":
                   {"image": "required elements/Dolphin properties/Dolphin image.jfif",
                    "video": "https://www.youtube.com/watch?v=jM6WTXSmG78",
                    "audio": open("required elements/Dolphin properties/Dolphin sound.mp3", "rb"),
                    "emoji": ":dolphin:",
                    "general facts": ["Động vật có vú", "Delphinidae"],
                    "fun facts": ["Cá heo ngủ với một mắt :zany_face:",
                                  "Mỗi con cá heo có một _'tên'_ riêng",
                                  "Cá heo sử dụng cá nóc để chơi bóng chuyền :volleyball:"]},

               "Hươu cao cổ":
                   {"image": "required elements/Giraffe properties/Giraffe image.webp",
                    "video": "https://www.youtube.com/watch?v=P_ckAbOr0r4",
                    "audio": open("required elements/Giraffe properties/Giraffe sound.mp3", "rb"),
                    "emoji": "🦒",
                    "general facts": ["Động vật có vú", "Giraffa"],
                    "fun facts": ["Lưỡi của một con hươu cao cổ dài tận _**50cm!**_ Và có màu tím đen",
                                  "Tim của một con hươu cao cổ nặng tận _**11kg!**_ :anatomical_heart:",
                                  "Hươu cao cổ đực dùng cổ đánh nhau để tranh dành con cái :crossed_swords:"]}
               }


def displaying_content(b):
    if b != "":
        with col6:
            st.header(f"**{b}** {animal_info[b]["emoji"]} :film_projector:")
            st.video(animal_info[b]["video"], format="video/mp4")
        with col7:
            st.header(f"Âm thanh của {b} :musical_note:")
            st.audio(animal_info[b]["audio"], format="audio/mp3")
            st.header(f"Ảnh của {b} :camera_with_flash:")
            st.image(animal_info[b]["image"], caption=f"{b} trong môi trường tự nhiện của nó")
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
    if chosen_animal != "":
        st.title(f"**Thông tin về {chosen_animal}** {animal_info[chosen_animal]["emoji"]}")
        with st.expander(":blue[**Thông tin trung trung**]"):
            st.write(f":red[Tên khoa học]: {animal_info[chosen_animal]["general facts"][1]}")
            st.write(f":red[Loài]: {animal_info[chosen_animal]["general facts"][0]}")
        with st.expander(":blue[**Thông tin thú vị**]"):
            st.write(":red[Bạn có biết?]")
            st.write(animal_info[chosen_animal]["fun facts"][0])
            st.write(animal_info[chosen_animal]["fun facts"][1])
            st.write(animal_info[chosen_animal]["fun facts"][2])
    else:
        st.title("Vui lòng chọn động vật")
