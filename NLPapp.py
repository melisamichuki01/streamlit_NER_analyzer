#pip install -r requirements.txt
import streamlit as st
from PIL import Image
import os

# Importing Obsei libraries
from obsei.analyzer.spacy_analyzer import SpacyAnalyzer
from obsei.sink.streamlit_sink import StreamlitSink
from obsei.source.text_input_source import TextInputSource
from obsei.pipeline.simple_pipeline import SimplePipeline

# Loading spacy model
spacy_analyzer = SpacyAnalyzer(model_name='en_core_web_sm')

# Initializing StreamlitSink
streamlit_sink = StreamlitSink()

# Layout Templates
title_temp = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
    <h4 style="color:white;text-align:center;">Obsei Streamlit</h1>
    </div>
    """

def main():
    st.set_page_config(page_title='Obsei Streamlit App', page_icon=':ner:')
    
    # Add a title and image to the page
    st.title("Obsei Streamlit App")
    our_image = load_image(os.path.join('SpaCy_logo.svg.png'))
    st.image(our_image)

    menu = ['Home', 'NER']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Home')
        raw_docx = st.text_area('Your Docs', 'Enter Text')
        if st.button("Analyze"):
            # Initializing TextInputSource
            text_input_source = TextInputSource(
                text = raw_docx,
                name = 'TextInputSource'
            )

            # Initializing SimplePipeline
            pipeline = SimplePipeline([
                spacy_analyzer,
            ], text_input_source, streamlit_sink)

            # Running the pipeline
            pipeline.run()

    elif choice == 'NER':
        st.subheader('Named Entity Recognizer')
        raw_docx = st.text_area('Your Text', 'Enter Text')
        if st.button('Analyze'):
            # Initializing TextInputSource
            text_input_source = TextInputSource(
                text = raw_docx,
                name = 'TextInputSource'
            )

            # Initializing SimplePipeline
            pipeline = SimplePipeline([
                spacy_analyzer,
            ], text_input_source, streamlit_sink)

            # Running the pipeline
            pipeline.run()

if __name__ == '__main__':
    main()
