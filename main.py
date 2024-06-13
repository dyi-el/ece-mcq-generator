# main.py

import os
import streamlit as st
from utils.populate_database import (load_documents_local,
                                     load_documents_uploaded,
                                     split_documents,
                                     add_to_chroma)
from utils.query_data import query_rag



st.title('✅ Electronics Engineer Licensure Exam Generator')

with st.sidebar:
    intro = '''
    This Retrieval Augmentated Generation application is a project by
    JL Bualoy & Denver Magtibay from Smart Edge ECE Review Specialist.
    
    ### TOPNOTCHER CUTIE 💯🙌
    '''
    st.write(intro)
    
    
    input_key = st.text_input('OpenAI API Key')
    os.environ["OPENAI_API_KEY"] = input_key
    
    if input_key:
        if st.button("Update Database"):
            uploaded = st.file_uploader('Upload another context file',type='pdf')

            st.warning('''Updating the database will affect only this session.
                    Choose local or uploaded update.
                    ''')
            
            if st.button("Local"):
                with st.spinner("Updating Database"):
                    docs = load_documents_local()
                    chunks = split_documents(docs)
                    add_to_chroma(chunks)
            
            if st.button("Uploaded"):
                with st.spinner("Updating Database"):
                    docs = load_documents_uploaded()
                    chunks = split_documents(docs)
                    add_to_chroma(chunks)
            
if input_key:
    tos_topic = st.selectbox(
    "Select the topic for the licensure exam:",
    ("Signal Spectra and Processing",
        "Principles of Communication",
        "Digital Communications",
        "Transmission and Antenna Systems",
        "Electronic Systems and Design",
        "Data Communications")
    )

    mcq_num = st.number_input('How many items do you need?', step=1)
        
        

    if st.button("Generate Exam", type="primary"):
        # Generate exam questions
        with st.spinner("Generating Exam Questions"):
            output_mcq = query_rag(tos_topic, mcq_num)
        
        # Formatting the response
        questions_and_answers = output_mcq.content.split("### Answer Key:")
        questions = questions_and_answers[0].strip()
        answer_key = questions_and_answers[1].strip()

        st.write(questions)
        with st.sidebar.expander("See Answer Key"):
            st.write(answer_key)
        
        st.sidebar.success(output_mcq.response_metadata)
        st.sidebar.success(output_mcq.usage_metadata)
else:
    st.write("Please input API Key, select a topic and click the 'Generate Exam' button.")
