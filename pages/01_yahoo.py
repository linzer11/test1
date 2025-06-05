import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="글로벌 시가총액 Top10 주가 시각화", layout="wide")
st.title("📈 글로벌 시가총액 TOP 10 기업 - 주가 변화 추이")

# 최근 1년 날짜 범위
end_date = datetime.today()
start_date = end_date - timedelta(days=365)
st.write(f"기간: **{start_date.date()} ~ {end_date.date()}**")

# 시가총액 TOP 10 기업 (티커: Yahoo Finance 형식 사용)
top10_companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK.B",  # BRK-B → BRK.B
    "Meta (Facebook)": "META",
    "TSMC": "TSM",
    "Eli Lilly": "LLY",
    "Saudi Aramco": "2222.SR"
}

# 데이터 다운로드 함수
@st.cache_data(show_spinner="📥 주가 데이터를 가져오는 중입니다...")
def fetch_data(ticker):
    try:
        df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True, progress=False)
        if "Close" in df.columns and not df.empty:
            return df["Close"]
    except Exception as e:
        st.warning(f"❌ {ticker} 데이터 요청 실패: {e}")
    return None

# 데이터 수집
stock_data = {}
for name, ticker in top10_companies.items():
    data = fetch_data(ticker)
    if data is not None:
        stock_data[name] = data
    else:
        st.warning(f"⚠️ '{name}' ({ticker})의 데이터를 가져올 수 없습니다.")

# 시각화
if stock_data:
    fig = go.Figure()
    for name, series in stock_data.items():
        fig.add_trace(go.Scatter(
            x=series.index,
            y=series.values,
            mode="lines",
            name=name
        ))

    fig.update_layout(
        title="최근 1년간 주가 변화 (종가 기준, USD)",
        xaxis_title="날짜",
        yaxis_title="주가 (USD)",
        template="plotly_white",
        height=600,
        legend_title="기업명"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("❌ 모든 기업의 데이터를 불러오는 데 실패했습니다.")
