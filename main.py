# main.py

# Remove this when running locally
#__import__('pysqlite3')
#import sys
#sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')



import os
import streamlit as st
from utils.populate_database import (load_documents,
                                     split_documents,
                                     add_to_chroma)
from utils.query_data import query_rag





# ------------ Stateful Buttons ----------------
if 'update_db' not in st.session_state:
    st.session_state.update_db = False

if 'continue_update' not in st.session_state:
    st.session_state.continue_update = False
    
def update_db():
    st.session_state.update_db = True

def continue_update():
    st.session_state.continue_update = True

# ------------ Stateful Buttons ----------------


st.title('✅ Electronics Engineer Licensure Exam Generator')
with st.sidebar:
    intro = '''
    This Retrieval Augmentated Generation application is a project by
    JL Bualoy & Denver Magtibay from Smart Edge ECE Review Specialist.
    It is still in experimental stage and may produce inaccurate results.
    Make sure to validate the questions and answers generated.
    
    Currently, only Electronics Systems and Technologies topics
    are supported.
    
    ### TOPNOTCHER CUTIE 💯🙌
    '''
    st.write(intro)
    
    st.success('To get your own API key, visit [OpenAI Platform](https://platform.openai.com/) page.')
    # Get API to environment variables
    input_key = st.text_input('OpenAI API Key',type='password')
    os.environ["OPENAI_API_KEY"] = input_key
    
    
    if input_key:
        st.button("Update Database", on_click=update_db)
        if st.session_state.update_db:

            st.warning('Updating the database only works locally.')
            doc = st.file_uploader('Upload a PDF for additional context',type='pdf')
            
            st.button("Continue", on_click=continue_update)
            if st.session_state.continue_update:
                with st.spinner("Updating Database"):
                    docs = load_documents(doc)
                    chunks = split_documents(docs)
                    add_to_chroma(chunks)
                    st.success('Updated the database ✅')
                    st.session_state.update_db = False
                    st.session_state.continue_update = False
        

            
            
            
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
