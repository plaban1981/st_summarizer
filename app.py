import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
import json
#
image_path = "image.jpg"
image = Image.open(image_path)

st.set_page_config(page_title="Extractive Text Summarization App", layout="centered")
st.image(image, caption='Text Summarization')
#
# page header
st.title(f"The Extractive Text Summarization App")
with st.form("Extract"):
   text1 = st.text_input("Enter text here")
   submit = st.form_submit_button("Summarize")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Keyword Extraction API
        url = "https://app.aimarketplace.co/api/marketplace/models/text-summarizer-f890dad5/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key sVKZMdoU.qQpg7hWner2Uh6TMNHMgbacdMGfHxcSU','Cache-Control': 'no-cache'}

        response = requests.request("POST", url, headers=headers, files=payload)
        #
        print(response.text)
        # output header
        st.header("Summarized Text")
        # output results
        st.success(response.text.split("Text Summary =")[1].replace("}","").replace("]",""))