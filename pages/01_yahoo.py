import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd

st.set_page_config(page_title="글로벌 시가총액 Top10 주가 변화", layout="wide")
st.title("📈 글로벌 시가총액 TOP 10 기업 - 최근 1년 주가 변화")

# 날짜 설정 (최근 1년)
end_date = datetime.today()
start_date = end_date - timedelta(days=365)
st.markdown(f"📅 기간: **{start_date.date()} ~ {end_date.date()}**")

# 시가총액 기준 TOP 10 기업 티커
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK.B",  # Yahoo에서는 BRK-B가 아닌 BRK.B 사용
    "Meta": "META",
    "TSMC": "TSM",
    "Eli Lilly": "LLY",
    "Saudi Aramco": "2222.SR"
}

# 개별 주가 데이터 수집 함수
@st.cache_data(show_spinner="📥 데이터를 가져오는 중...")
def get_close_prices():
    data = {}
    for name, ticker in companies.items():
        try:
            df = yf.download(ticker, start=start_date, end=end_date, progress=False, auto_adjust=True)
            if not df.empty and "Close" in df.columns:
                data[name] = df["Close"]
            else:
                st.warning(f"⚠️ {name} ({ticker})의 종가 데이터가 비어 있거나 없습니다.")
        except Exception as e:
            st.warning(f"❌ {name} ({ticker})의 데이터를 불러오는 중 오류 발생: {e}")
    return data

data = get_close_prices()

# 주가 그래프 시각화
if data:
    fig = go.Figure()
    for name, price_series in data.items():
        fig.add_trace(go.Scatter(
            x=price_series.index,
            y=price_series.values,
            mode="lines",
            name=name
        ))

    fig.update_layout(
        title="📊 최근 1년간 글로벌 시가총액 TOP 10 기업 주가 추이",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        template="plotly_white",
        height=600,
        legend_title="기업명"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("❌ 불러온 데이터가 없습니다. 네트워크 상태 또는 티커 확인이 필요합니다.")
