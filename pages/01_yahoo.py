import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 글로벌 시가총액 TOP 10 기업 (2024 기준, 티커는 Yahoo Finance 기준)
top10_companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "TSMC": "TSM",
    "Eli Lilly": "LLY"
}

st.set_page_config(page_title="Top 10 Global Stocks", layout="wide")
st.title("📈 글로벌 시가총액 TOP 10 기업 - 주가 변화 추이")

# 날짜 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

st.write(f"기간: **{start_date.date()} ~ {end_date.date()}**")

# 데이터 수집
@st.cache_data(show_spinner=True)
def fetch_data(tickers):
    data = yf.download(tickers, start=start_date, end=end_date)["Adj Close"]
    return data

tickers = list(top10_companies.values())
data = fetch_data(tickers)

# Plotly 시각화
fig = go.Figure()

for name, ticker in top10_companies.items():
    if ticker in data.columns:
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data[ticker],
            mode='lines',
            name=name
        ))

fig.update_layout(
    title="최근 1년간 주가 추이 (종가 기준, USD)",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    template="plotly_dark",
    height=600,
    legend_title="기업명"
)

st.plotly_chart(fig, use_container_width=True)
@st.cache_data(show_spinner=True)
def fetch_data(tickers):
    data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker', auto_adjust=True)
    
    # 여러 티커가 있을 경우에는 MultiIndex, 하나일 경우에는 단일 컬럼
    if isinstance(data.columns, pd.MultiIndex):
        adj_close = pd.DataFrame()
        for ticker in tickers:
            try:
                adj_close[ticker] = data[("Adj Close", ticker)]
            except KeyError:
                st.warning(f"⚠️ 데이터 누락: {ticker} 의 데이터를 가져올 수 없습니다.")
    else:
        adj_close = pd.DataFrame()
        try:
            adj_close[tickers[0]] = data["Adj Close"]
        except KeyError:
            st.error("❌ 'Adj Close' 컬럼이 존재하지 않습니다.")
            return pd.DataFrame()
    
    return adj_close
