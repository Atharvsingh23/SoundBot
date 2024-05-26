import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        say("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            say(result)

        except:
            say("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        say("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
       
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        say("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        say("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
       
        results = wikipedia.summary(query,sentences = 2)
        say("According to wikipedia..")
        print(results)
        say(results)
