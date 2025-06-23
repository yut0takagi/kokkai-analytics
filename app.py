# app.py
import streamlit as st
from utils.fetch_kokkai import get_speech_by_name
from utils.analyzer import generate_wordcloud
import matplotlib.pyplot as plt

st.title("国会議員の発言傾向分析アプリ")

name = st.text_input("議員名を入力してください（例：岸田文雄）")
submit = st.button("発言を取得し分析")

if submit and name:
    with st.spinner("発言を取得中..."):
        speeches = get_speech_by_name(name)

    if speeches:
        st.success(f"{name} の発言数: {len(speeches)} 件")

        text = "\n".join(speeches)
        st.subheader("WordCloud")
        wordcloud = generate_wordcloud(text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("発言が見つかりませんでした")