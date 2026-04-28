import streamlit as st

st.title("AI Text Summarizer & Quiz Generator")

text = st.text_area("Enter your text:")

if st.button("Generate"):
    if text:
        summary = text[:200] + "..."

        st.subheader("Summary")
        st.write(summary)

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
