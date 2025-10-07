# Voice Campus Navigation

A simple voice-controlled campus navigation system that listens to your query, understands start and destination points using NLP, and finds paths between locations using DFS.

## Features

- Voice input for queries
- Extracts locations using NLP
- Finds all paths between two locations
- Speaks out the directions

## Requirements

- Python 3
- speech_recognition
- pyttsx3
- spacy
- en_core_web_sm (SpaCy language model)

## Setup

1. Install required packages:
pip install speechrecognition pyttsx3 spacy
python -m spacy download en_core_web_sm


2. Run the script:
python your_script_name.py
