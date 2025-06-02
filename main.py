import streamlit as st
import random

st.set_page_config(
    page_title="🎵 감정 기반 음악 추천기",
    page_icon="🎧",
    layout="centered"
)

# 감정별 추천 노래 데이터
emotion_music = {
    "😄 기쁨": [
        ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Good Time - Owl City & Carly Rae Jepsen", "https://www.youtube.com/watch?v=H7HmzwI67ec"),
        ("Can't Stop the Feeling! - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
    ],
    "😢 슬픔": [
        ("Someone Like You - Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ("Jealous - Labrinth", "https://www.youtube.com/watch?v=50VWOBi0VFs"),
    ],
    "😡 화남": [
        ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
        ("Believer - Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc"),
        ("Numb - Linkin Park", "https://www.youtube.com/watch?v=kXYiU_JCYtU"),
    ],
    "😌 평온함": [
        ("Weightless - Marconi Union", "https://www.youtube.com/watch?v=UfcAVejslrU"),
        ("Bloom - The Paper Kites", "https://www.youtube.com/watch?v=8inJtTG_DuU"),
        ("River Flows in You - Yiruma", "https://www.youtube.com/watch?v=7maJOI3QMu0"),
    ],
    "🤩 설렘": [
        ("Electric Love - BØRNS", "https://www.youtube.com/watch?v=RYr96YYEaZY"),
        ("Lover - Taylor Swift", "https://www.youtube.com/watch?v=-BjZmE2gtdo"),
        ("Love Scenario - iKON", "https://www.youtube.com/watch?v=vecSVX1QYbQ"),
    ]
}

st.markdown("<h1 style='text-align: center; color: #ff6f61;'>🎧 감정 기반 음악 추천기</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>오늘 당신의 감정은 어떤가요? 기분에 맞는 노래를 추천해드릴게요 🎵</p>", unsafe_allow_html=True)

# 감정 선택
emotion = st.selectbox("🧠 지금 느끼는 감정을 선택하세요", list(emotion_music.keys()))

# 추천 버튼
if st.button("🔍 노래 추천 받기"):
    st.markdown(f"<h3>{emotion} 감정에 어울리는 노래 🎶</h3>", unsafe_allow_html=True)
    tracks = emotion_music.get(emotion, [])
    random.shuffle(tracks)
    for title, url in tracks[:3]:
        st.markdown(f"- [{title}]({url})")

# 이모지 배경 효과
emotion_emoji = {
    "😄 기쁨": "🌞🌈🎉",
    "😢 슬픔": "🌧️😔💧",
    "😡 화남": "🔥💢⚡",
    "😌 평온함": "🌿🕊️💤",
    "🤩 설렘": "💘✨🌸"
}
st.markdown("---")
st.markdown(f"<h2 style='text-align: center;'>{emotion_emoji.get(emotion, '')}</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>음악이 당신의 하루에 작은 힘이 되기를 💖</p>", unsafe_allow_html=True)
