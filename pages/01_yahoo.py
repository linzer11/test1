import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="글로벌 시가총액 Top10 주가 시각화", layout="wide")
st.title("📈 글로벌 시가총액 TOP 10 기업 - 주가 변화 추이")

# 시가총액 기준 TOP 10 기업 (2024 기준)
top10_companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "TSMC": "TSM",
    "Eli Lilly": "LLY",
    "Saudi Aramco": "2222.SR"  # 주의: 종종 데이터 누락 발생
}

# 날짜 범위 설정 (최근 1년)
end_date = datetime.today()
start_date = end_date - timedelta(days=365)
st.write(f"기간: **{start_date.date()} ~ {end_date.date()}**")

# 데이터 가져오기 함수
@st.cache_data(show_spinner="📥 주가 데이터를 불러오는 중...")
def fetch_data(tickers):
    raw = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        group_by='ticker',
        progress=False,
        threads=True
    )

    adj_close = pd.DataFrame()

    # 여러 티커 → MultiIndex 구조
    if isinstance(raw.columns, pd.MultiIndex):
        for ticker in tickers:
            try:
                adj_close[ticker] = raw[("Adj Close", ticker)]
            except KeyError:
                st.warning(f"⚠️ '{ticker}'의 데이터를 가져올 수 없습니다.")
    else:
        # 단일 티커 → 일반 구조
        try:
            adj_close[tickers[0]] = raw["Adj Close"]
        except KeyError:
            st.error("❌ 'Adj Close' 컬럼을 찾을 수 없습니다.")
    
    return adj_close

# 데이터 다운로드
tickers = list(top10_companies.values())
data = fetch_data(tickers)

# 데이터 확인 (디버깅용)
# st.dataframe(data.head())

# 시각화
fig = go.Figure()

for name, ticker in top10_companies.items():
    if ticker in data.columns:
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data[ticker],
            mode="lines",
            name=name
        ))
    else:
        st.warning(f"📉 {name} ({ticker}) 데이터가 누락되어 시각화에서 제외됩니다.")

fig.update_layout(
    title="최근 1년간 주가 변화 (Adj Close, USD)",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    template="plotly_white",
    height=600,
    legend_title="기업명"
)

st.plotly_chart(fig, use_container_width=True)
