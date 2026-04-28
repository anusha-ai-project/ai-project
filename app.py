import streamlit as st
from transformers import pipeline

st.title("AI Text Summarizer & Quiz Generator")

text = st.text_area("Enter your text:")

if st.button("Generate"):
    if text:

        # ===== SUMMARY =====
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)

        st.subheader("Summary")
        st.write(summary[0]['summary_text'])

        # ===== QUIZ =====
        st.subheader("Quiz")

        questions = [
            "What is the main topic?",
            "Where is it used?",
            "What are the benefits?"
        ]

        for q in questions:
            st.write("Q:", q)

            if "topic" in q.lower():
                st.write("A: Artificial Intelligence (AI)")
            elif "used" in q.lower():
                st.write("A: It is used in healthcare, education, finance and many industries")
            elif "benefits" in q.lower():
                st.write("A: It improves efficiency, accuracy and automation")

        # ===== IMAGE =====
        st.subheader("Generated Image")
        st.image("https://picsum.photos/600/400")
