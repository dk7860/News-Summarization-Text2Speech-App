
# News-Summarization-Text2Speech-App
Develop a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi

# Overview
A web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The tool should allow users to input a company name and receive a structured sentiment report along with an audio output.

# Tech Stack:
Frontend: Streamlit
Backend: FastAPIs
NLP Models: Hugging Face transformers (Sentiment Analysis)
Text-to-Speech: gTTS (Hindi Speech)

# Prerequisites
Python 3.8+
pip

# Clone the Repository
Clone this repository locally. In a terminal, run the following command:

$ git clone https://github.com/dk7860/News-Summarization-Text2Speech-App.git
$ cd News-Summarization-Text2Speech-App

# Install Dependencies:
* pip install -r requirements.txt

# Run the Application:
* streamlit run app.py

## Deployment on Hugging Face Spaces

The application is deployed on Hugging Face Spaces for public use. You can access it here:
* [News Summarization and Text-to-Speech App](https://huggingface.co/spaces/dk74433/News-Summarization-and-Text-to-Speech-App)

  To deploy manually:
* Create a Hugging Face Space
* Select Python - Streamlit
* Push code to the Hugging Face repository

title: News Summarization Text To Speech App

emoji:📊

colorFrom: purple

colorTo: green

sdk: streamlit

sdk_version: 1.43.2

app_file: app.py

pinned: false

short_description: Generates a text-to-speech (TTS) output in Hindi
  
