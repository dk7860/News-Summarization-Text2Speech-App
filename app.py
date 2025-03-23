import streamlit as st
from utils import fetch_news, analyze_sentiment, generate_hindi_audio, compare_sentiments
st.title("Company News")
company_name = st.text_input("Enter Company Name:")
if company_name:
    news_articles = fetch_news(company_name)
    st.subheader("Extracted News Articles")
    for i, article in enumerate(news_articles):
        st.write(f"**{i+1}. {article['title']}**")
        st.write(f"_Summary:_ {article['summary']}")
        st.write(f"[Read More]({article['url']})")
        
        sentiment = analyze_sentiment(article["summary"])
        st.write(f"Sentiment: {sentiment['sentiment']} (Score: {sentiment['score']})")
        st.markdown("---")
        
    analysis = compare_sentiments(news_articles)
    st.subheader("Sentiment Distribution")
    st.write(analysis)

    hindi_text = " ".join([article["summary"] for article in news_articles[:3]])
    audio_file = generate_hindi_audio(hindi_text)
    st.audio(audio_file, format="audio/mp3")