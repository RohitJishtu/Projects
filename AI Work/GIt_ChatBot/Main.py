import gradio as gr
import spacy
from annoy import AnnoyIndex
from Model import * 
from RAG import * 
from Prompt import * 
import os

# Define the function that alternates between agreement and disagreement
def execute(github_link=None, message=None):
        if github_link != None:
            # calling RAG first 

            repo_path = github_link.rsplit("/", 1)[-1]
            try :
                subprocess.run(["git", "clone", github_link])
            except:
                print('path exists')
            try:
                RAG1 = RAGSystemWithSpacy(repo_path=repo_path)
                RAG1.index_documents()
                doc_answer = RAG1.ask_question(message)
            except:
                doc_answer='RAG didnt work well'
        print(doc_answer)
            
        if message:
            m1 = Model()
            p1=PromptsStand(message)
            if doc_answer != 'No relevant document found.' or doc_answer ==None  or github_link==None :
                custom='Summary Agent'
                document_answer= p1.create_prompts(doc_answer,custom)
                print(f'prompt1 {document_answer}')
                response = m1.Calling_Local_LAMA(document_answer)
            else:
                custom='Cloning and Summary Agent for ' + str(github_link)
                document_answer= p1.create_prompts(doc_answer,custom)
                print(f'prompt2 {document_answer}')
                response = m1.Calling_Local_LAMA(document_answer)
            return response  # Return response for use in the chatbot
        else:
            return 'Sorry, I cannot understand.'

# Create a simple chatbot interface with an additional GitHub link input
with gr.Blocks() as Main:
    chatbot = gr.Chatbot(label="KnowYourRepo")  # Chatbot display
    github_link = gr.Textbox(label="GitHub Link", placeholder="Paste your GitHub link here...", lines=1)  # Input for GitHub link
    msg = gr.Textbox(label="Your Question", placeholder="Type your question here...", lines=1)  # Input for message
    
    with gr.Row():  # Organize the buttons in a row
        submit_btn = gr.Button("Submit", size="sm")  # Submit button, small size
        clear_btn = gr.Button("Clear Results", size="sm")  # Clear results button, small size
        IP_clear_btn = gr.Button("Clear Inputs", size="sm")  # Clear input button, small size

    # Function to handle the submission of a question and GitHub link
    def respond(message, github_link, history):
        response = execute(github_link, message)  # Call the function with the actual variable
        history.append((message, response))  # Update history with the new message and response
        return history  # Return updated history to update the chatbot display

    def clear_inputs():
        return "", ""  # Return empty strings for both input fields

    # Link the submit button to the respond function
    submit_btn.click(respond, inputs=[msg, github_link, chatbot], outputs=chatbot)
    clear_btn.click(lambda: [], None, chatbot)  # Clear the chatbot display
    IP_clear_btn.click(clear_inputs, outputs=[msg, github_link])  # Clear input fields

# Launch the chatbot interface
Main.launch()
