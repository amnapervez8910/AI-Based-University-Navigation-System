import speech_recognition as sr
import pyttsx3
import spacy

# Initialize speech recognition, TTS, and NLP
recognizer = sr.Recognizer()
engine = pyttsx3.init()
nlp = spacy.load("en_core_web_sm")

# Graph representation (campus map)
graph = {
    "Main gate": ["Tuc Shop", "Library"],
    "Tuc Shop": ["Main gate", "CS Department"],
    "Library": ["Main gate", "Admin Block"],
    "CS Department": ["Tuc Shop", "Admin Block"],
    "Admin Block": ["Library", "CS Department"]
}

# DFS algorithm to find all paths
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = dfs(graph, node, goal, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Text-to-Speech output
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Get user voice input
def get_command():
    with sr.Microphone() as source:
        print("Say your query:")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query
        except Exception as e:
            speak("Sorry, I could not understand. Please try again.")
            return None

# Process query using NLP to extract start and destination
def process_query(query):
    doc = nlp(query)
    locations = [ent.text for ent in doc.ents if ent.label_ == "ORG" or ent.label_ == "GPE"]
    if len(locations) >= 2:
        return locations[0], locations[1]
    else:
        return None, None

# Main function
if __name__ == "__main__":
    query = get_command()
    if query:
        start, goal = process_query(query)
        if start and goal:
            paths = dfs(graph, start, goal)
            if paths:
                speak(f"Found {len(paths)} path(s) from {start} to {goal}.")
                for path in paths:
                    route = " -> ".join(path)
                    print("Path:", route)
                    speak(route)
            else:
                speak("No path found.")
        else:
            speak("Could not detect start and destination.")
