import streamlit as st
from transformers import pipeline

st.title("AI Text Summarizer & Quiz Generator")

text = st.text_area("Enter your text:")

if st.button("Generate"):
    if text:

        # SUMMARY
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)

        st.subheader("Summary")
        st.write(summary[0]['summary_text'])

        # QUESTION GENERATION (simple logic)
        st.subheader("Quiz")

        questions = [
            "What is the main topic?",
            "What is the key idea?",
            "What are the benefits?"
        ]

        # 👉 Answer generate using summary
        for q in questions:
            st.write("Q:", q)
            st.write("A:", summary[0]['summary_text'])  # better than dummy

        # IMAGE (stable one)
        st.subheader("Generated Image")
        st.image("https://picsum.photos/600/400")
