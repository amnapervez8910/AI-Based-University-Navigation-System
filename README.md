Voice Campus Navigator

A simple Python app that listens to your voice to find routes between campus locations.

What it does

Takes voice input to understand start and destination locations.

Finds all possible paths between those points on a small campus map.

Speaks out the found paths.

How to use

Run the program:

python main.py


When prompted, say something like:

"Go from Main gate to Admin Block."

The app will tell you the possible routes.

Setup

Install dependencies:

pip install SpeechRecognition pyttsx3 spacy
python -m spacy download en_core_web_sm

Note that

The campus map is simple and fixed in the code.

Works best with clear location names.
