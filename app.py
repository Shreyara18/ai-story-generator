import streamlit as st
from story_generator import generate_story

st.title("AI Story Generator")

main_character = st.text_input(
    "Enter Main Character"
)

supporting_character = st.text_input(
    "Enter Supporting Character"
)

setting = st.text_input(
    "Enter Story Setting"
)

genre = st.selectbox(
    "Choose Genre",
    ["Fantasy", "Adventure", "Romance", "Sci-Fi", "Mystery", "Horror", "Comedy", "Sibling Rivalry", "Thriller","Friendship", "Family", "Supernatural", "Fairy Tale", "Mythology"]
)

if st.button("Generate Story"):

    with st.spinner("Generating Story..."):

        story = generate_story(
            main_character,
            supporting_character,
            setting,
            genre
        )

        st.subheader("Generated Story")

        st.write(story)