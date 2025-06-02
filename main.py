import streamlit as st
import random

st.set_page_config(
    page_title="🌟 MBTI 진로 추천기",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="auto"
)

# 이모지 스타일 타이틀
st.markdown(
    """
    <h1 style='text-align: center; color: #FF69B4;'>✨ MBTI 기반 진로 추천기 💼</h1>
    <h4 style='text-align: center;'>당신의 성격 유형에 맞는 찰떡 직업은?! 🔮</h4>
    """,
    unsafe_allow_html=True
)

# MBTI 목록
mbti_types = [
    "INTJ 🧠", "INTP 🧪", "ENTJ 🚀", "ENTP 💡",
    "INFJ 🔮", "INFP 🎨", "ENFJ 🌟", "ENFP 🌈",
    "ISTJ 📊", "ISFJ 💖", "ESTJ 🏗️", "ESFJ 🤝",
    "ISTP 🛠️", "ISFP 🎸", "ESTP 🎯", "ESFP 🎤"
]

# MBTI별 추천 직업 데이터
job_recommendations = {
    "INTJ": ["데이터 과학자 📊", "전략 기획자 📈", "AI 연구원 🤖"],
    "INTP": ["이론 물리학자 🧪", "프로그래머 💻", "UX 디자이너 🎨"],
    "ENTJ": ["CEO 🧑‍💼", "프로덕트 매니저 📋", "경영 컨설턴트 🕴️"],
    "ENTP": ["스타트업 창업가 🚀", "마케팅 디렉터 📢", "기획자 🧩"],
    "INFJ": ["심리상담사 🧘", "작가 ✍️", "교육자 🎓"],
    "INFP": ["시인 📝", "일러스트레이터 🎨", "사회복지사 🫶"],
    "ENFJ": ["리더십 트레이너 👩‍🏫", "멘토 🧑‍🤝‍🧑", "공공정책 전문가 🏛️"],
    "ENFP": ["예술가 🎭", "홍보 전문가 📣", "크리에이터 📹"],
    "ISTJ": ["회계사 📒", "군인 🎖️", "엔지니어 ⚙️"],
    "ISFJ": ["간호사 💉", "초등교사 🧑‍🏫", "보건복지사 🩺"],
    "ESTJ": ["프로젝트 매니저 🧱", "관리직 공무원 🏢", "은행원 💰"],
    "ESFJ": ["이벤트 플래너 🎊", "HR 매니저 🧑‍💼", "간병인 ❤️"],
    "ISTP": ["정비사 🔧", "경찰관 🚓", "응급구조사 🚑"],
    "ISFP": ["플로리스트 💐", "사진작가 📷", "애니메이터 🎞️"],
    "ESTP": ["세일즈 전문가 💼", "스턴트맨 🤸", "외교관 🌐"],
    "ESFP": ["연예인 🌟", "패션 디자이너 👗", "방송인 🎙️"]
}

# 사용자 선택
selected_mbti_raw = st.selectbox("🧬 당신의 MBTI를 선택하세요!", mbti_types)

# MBTI 키만 추출
selected_mbti = selected_mbti_raw.split()[0]

# 추천 버튼
if st.button("🔍 직업 추천 받기!"):
    st.markdown(f"## 🎉 {selected_mbti_raw}에게 어울리는 직업은?")
     recommended_jobs = job_recommendations.get(selected_mbti, [])
    if recommended_jobs:
        for job in recommended_jobs:
            st.markdown(f"- {job}")
    else:
        st.warning("죄송합니다. 해당 MBTI에 대한 정보가 아직 없습니다. 🙇")

# 꾸미기용 이모지
st.markdown("---")
st.markdown("<h4 style='text-align: center;'>🌟 세상에 단 하나뿐인 당신만의 진로를 응원합니다! 💖</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ by [Your Name]</p>", unsafe_allow_html=True)
  

