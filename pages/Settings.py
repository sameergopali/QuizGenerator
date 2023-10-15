import streamlit as st
import os
def settings():
    st.title("Settings")
    st.write("This is the settings section.")

    openai_api_key = st.text_input("Enter a Open API Key:")
    huggingface_api_key = st.text_input("Enter a HuggingFace API Key:")
    pinecone_api_key = st.text_input("Enter a Pinecone API Key:")
    if openai_api_key and huggingface_api_key and pinecone_api_key:
        # Save the API key 
        os.environ["OPENAI_API_KEY"] = openai_api_key
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_api_key
        os.environ["PINECONE_API_KEY"] =  pinecone_api_key
        # st.session_state["apikeys"] ={ "openai" :openai_api_key,
        #                               "huggingface": huggingface_api_key,
        #                               "pinecone" : pinecone_api_key

        
settings()
