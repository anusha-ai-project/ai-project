import streamlit as st
from transformers import pipeline

st.title("AI Text Summarizer & Quiz Generator")

text = st.text_area("Enter your text:")

if st.button("Generate"):
    if text:
        summarizer = pipeline("summarization")

        summary = summarizer(text, max_length=80, min_length=20, do_sample=False)

        st.subheader("Summary")
        st.write(summary[0]['summary_text'])

        st.subheader("Quiz")

        questions = [
            "What is the main topic?",
            "Where is it used?",
            "What are the benefits?"
        ]

        for q in questions:
            st.write("Q:", q)
            st.write("A:", "Based on the text")

        st.subheader("Generated Image")
        st.image("https://source.unsplash.com/600x400/?technology")
