import streamlit as st
import pandas as pd
import base64
import urllib.request
import json
import warnings
warnings.filterwarnings('ignore')
import os
import sys


from SnowflakeConnect import *
from langChainLLM import *
from UseModel import *
import time
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
from snowflake.connector.pandas_tools import write_pandas
import sqlite3

# Define your function to process the input
def process_input(Question, Context='', model='GPT'):
    Objects1 = ModelClass()
    Prompt = Objects1.Clean_Context_Prompts(Context, Question)
    print('reached here')

    if model in ['Llama', 'Mistral']:
        ConnLab = Lab_snowflake_connection()
        print(f"{ConnLab=}")
        full_result, timetaken = Objects1.CallModel(Prompt, model, ConnLab)
        # full_result, timetaken='No result',10
    else:
        full_result, timetaken = Objects1.CallModel(Prompt, model)
    summary = full_result[:1000]  # Display the first 1000 characters as summary

    return summary, timetaken, full_result

# Streamlit app
def main():
    st.title("TransLoom Insights ")

    # Input fields for question and context
    question = st.text_area("Question:", height=100, value=st.session_state.get('question', ''))
    models = ["GPT", "Llama", "Mistral"]
    selected_model = st.radio("Select Model:", models, index=0)
    context = st.text_area("Context (optional):", height=50, value=st.session_state.get('context', ''))
    if st.button("Process"):
        if question:
            # Process the input text
            summary, timetaken, full_result = process_input(question, context, selected_model)
            
            # Store the results and inputs in session state
            st.session_state.question = question
            st.session_state.context = context
            st.session_state.summary = summary
            st.session_state.timetaken = timetaken
            st.session_state.full_result = full_result

            # Display the summary
            st.write("Summary:")
            st.write(summary)

            st.write("Time taken:")
            st.write(timetaken)

            # Provide a download link for the full result
            b64 = base64.b64encode(full_result.encode()).decode()  # Encode the full result
            href = f'<a href="data:file/txt;base64,{b64}" download="result.txt">Download full result</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.write("Please enter a question.")
    
    if 'summary' in st.session_state:
        if st.button("Load Results to DB"):
            Objects1 = ModelClass()
            Objects1.WritetoDB(st.session_state.question, selected_model, st.session_state.context, st.session_state.summary, st.session_state.timetaken, st.session_state.full_result)
            st.write("Results loaded to DB.")

    # Button to show history
    if 'show_history' not in st.session_state:
        st.session_state.show_history = False

    if st.button("Show History of Results"):
        st.session_state.show_history = not st.session_state.show_history

    if st.session_state.show_history:
        Conn=Dev_snowflake_connection()
        history_df = pd.read_sql("""select Question,Context, model, summary, timetaken from EDW_LS.DATASCIENCE_GENAI.LLM_COMPARE
                                    order by LoadTime desc
                                 """, Conn)
        st.dataframe(history_df)

if __name__ == "__main__":
    main()
