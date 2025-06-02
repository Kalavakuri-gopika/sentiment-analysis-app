import streamlit as st
from textblob import TextBlob

st.title("💬 Sentiment Analysis (No Dataset or Training Needed)")

user_input = st.text_area("Enter text:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            st.success(f"😊 Positive Sentiment (Score: {polarity:.2f})")
        elif polarity < 0:
            st.error(f"😠 Negative Sentiment (Score: {polarity:.2f})")
        else:
            st.info(f"😐 Neutral Sentiment (Score: {polarity:.2f})")
