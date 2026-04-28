import streamlit as st
from transformers import pipeline

st.title("AI Text Summarizer & Quiz Generator")

# Input
text = st.text_area("Enter your text:")

if st.button("Generate"):
    if text:

        # Summarization
        summarizer = pipeline(
            task="summarization",
            model="facebook/bart-large-cnn"
        )

        summary = summarizer(
            text,
            max_length=100,
            min_length=30,
            do_sample=False
        )

        st.subheader("Summary")
        st.write(summary[0]['summary_text'])

        # Quiz Section
        st.subheader("Quiz")

        questions = [
            "What is the main topic?",
            "Where is it used?",
            "What are the benefits?"
        ]

        for q in questions:
            st.write("Q:", q)
            st.write("A:", "Based on the text")

        # Image Section (simple working)
        st.subheader("Generated Image")
        st.image("https://source.unsplash.com/600x400/?technology")
