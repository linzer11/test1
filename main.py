import streamlit as st
import openai

# 🔐 OpenAI API 키 설정
openai.api_key = "YOUR_OPENAI_API_KEY"

# 🌟 페이지 기본 설정
st.set_page_config(page_title="AI 성격 분석기", page_icon="🧠", layout="centered")

st.title("🧠 AI 성격 분석 + 닮은 인물 찾기")
st.markdown("간단한 질문에 답하면, 당신의 성격과 닮은 유명 인물을 찾아드립니다 ✨")

# 📋 질문 리스트
questions = [
    "1️⃣ 혼자 있는 시간이 좋으신가요, 사람들과 어울리는 걸 더 좋아하시나요?",
    "2️⃣ 계획대로 움직이는 걸 좋아하나요, 즉흥적인 걸 더 선호하시나요?",
    "3️⃣ 감정보다는 논리로 결정하는 편인가요, 감정을 중시하나요?",
    "4️⃣ 새로운 아이디어에 열려 있는 편인가요, 현실적인 걸 선호하나요?",
    "5️⃣ 갈등 상황에서 어떻게 대응하시나요?"
]

# ✍️ 사용자 응답 받기
responses = []
for q in questions:
    responses.append(st.text_area(q, placeholder="여기에 답변을 작성하세요", height=80))

# 🎯 분석 버튼
if st.button("🔍 성격 분석 + 인물 추천 받기"):
    with st.spinner("AI가 당신의 성격을 분석 중입니다...🧠"):
        prompt = (
            "다음은 한 사람의 성격에 대한 응답입니다. "
            "이 정보를 바탕으로 해당 인물의 MBTI 성격 유형을 추정하고, 닮은 유명 인물 한 명과 그 이유를 설명해주세요.\n\n"
        )
        for i, r in enumerate(responses):
            prompt += f"Q{i+1}: {questions[i]}\nA{i+1}: {r}\n"
        prompt += "\n결과 형식: \n1. 성격 분석 요약\n2. 예상 MBTI 유형\n3. 닮은 유명 인물 + 간단한 설명"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )

            result = response['choices'][0]['message']['content']
            st.success("분석 완료! 🎉")
            st.markdown("## 📊 결과")
            st.markdown(result)

        except Exception as e:
            st.error("오류 발생: OpenAI API 응답 실패")
            st.exception(e)

st.markdown("---")
st.markdown("👤 예시 인물: BTS RM, Steve Jobs, IU, Elon Musk, 유재석 등")
st.markdown("💡 친구와 함께 테스트하고 공유해보세요!")
