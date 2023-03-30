import streamlit as st
import spacy_streamlit
import spacy
from PIL import Image
import os

# Load the SpaCy model
spacy_model = "en_core_web_sm"
nlp = spacy.load(spacy_model)

# Define a function to load an image
@st.cache
def load_image(img):
    im = Image.open(img)
    return im

# Define the layout templates
title_temp ="""
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
    <h4 style="color:white;text-align:center;">SpaCy Streamlit</h1>
    </div>
    """

def main():
    # Set the page title and favicon
    st.set_page_config(page_title='SpaCy Streamlit App', page_icon=':ner:')
    
    # Add a title and image to the page
    st.title("SpaCy Streamlit App")
    our_image = load_image(os.path.join('SpaCy_logo.svg.png'))
    st.image(our_image)

    # Define the menu options
    menu = ['Home', 'Named Entity Recognition']
    choice = st.sidebar.selectbox('Select an option', menu)

    # Define the "Home" page
    if choice == 'Home':
        st.subheader('Home')
        # Add a file uploader for input
        raw_docx = st.file_uploader('Upload a document', type=['txt'])
        # If the user uploads a file and clicks the "Tokenize" button, visualize the tokens
        if raw_docx is not None and st.button('Tokenize'):
            spacy_streamlit.visualize_tokens(nlp(raw_docx.read().decode()), attrs=["text", "pos_", "dep_", "ent_type_"])

    # Define the "Named Entity Recognition" page
    elif choice == 'Named Entity Recognition':
        st.subheader('Named Entity Recognition')
        # Add a text area for input
        raw_docx = st.text_area('Enter some text', 'Type here...')
        # If the user clicks the "Analyze" button, visualize the entities
        if st.button('Analyze'):
            spacy_streamlit.visualize_ner(nlp(raw_docx), labels=nlp.get_pipe("ner").labels)

if __name__ == '__main__':
    main()
