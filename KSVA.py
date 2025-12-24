import speech_recognition as sr  # My assistence can speech

import pyttsx3  # activate the voice of my assistence

import logging # To capture the problem or othes my assistence

import os # to handle the operating system (define the path )

import datetime # KSVA can said time and date

import wikipedia # KSVA can search and find my question or queiers in wikipidia

import webbrowser # KSVA is capable to open web browser

import random  # KSVA is randomly play music

import subprocess # KSVA is also open calculate, notepad, cmd others subprocess tasks

import google.generativeai as genai # for casual conversation



# Logging configuration 
LOG_DIR = "logs" # Folder name

LOG_FILE_NAME = "application.log" # log file name

os.makedirs(LOG_DIR, exist_ok=True) # here, create a folder or directory

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME) # here the path of directory

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

# Activating voice from our System

# initialize the pyttx3
engine = pyttsx3.init("sapi5")

# set the voice Property
engine.setProperty('rate', 160)

# acivate the voice 
voices = engine.getProperty("voices")

# choose the first (male) voice
engine.setProperty('voice', voices[0].id)

# To see the voice name
# print(voices[0].id)

# This is speak function

def speak(text):
    """
    This function converts text to voice
    
    Args:
        text
    return:
        voice
    
    """
    # speak our assistence
    engine.say(text)
    
    engine.runAndWait() # After speak the close it.
    

# This Function recognize the spech and convert it to text(use speech_recognition package or function)
    
def takeCommand():
    """
    - This Function takes command & recognize 
    
    - Return
        text as query
    """
    # initialize the recognizer()
    r = sr.Recognizer()
    
    # capcare the command (so, active the microphone)
    with sr.Microphone() as source:
        print("Listening...") # assistence can listening you command
        r.pause_threshold = 1 # pause value 
        
        # listen the command by source
        audio = r.listen(source)
        
        
        #  convert autio to text using (google speak to text converter API - which is external that way we use exception handling)
        
        try:
            # convert to text if no problem
            print("Recognizing...")
            # use google api 
            query = r.recognize_google(audio, language = 'en-in')
            
            print(f"User said: {query}\n")
            
        except Exception as e:
            logging.info(e)
            print("Say that again please") # for terminal show
            return "None" # if exception is arise
        
        return query
    
# Another functionality of my assistence
def greeting():
    """
    - Capture the current time.
    - 
    
    """
    # extract the Current hour
    hour = (datetime.datetime.now().hour)
    
    if hour >=0 and hour <= 12: # both condition must be true (<=12)
        speak("Good Morning sir! How are you doing?")
        
    elif hour >=12 and hour <=18:
        speak("Good Evning sir! How are you doing?")
    else:
        speak("Good Evening sir! How are you doing?")
        
    speak("I am Kz. Please tell me how may I help you today?")
    

def play_music():
    music_dir = "E:\\Project\Kz-Smart-Voice-Assistant-KSVA-\\music"   # <-- change this to your music folder
    try:
        songs = os.listdir(music_dir)
        if songs:
            random_song = random.choice(songs)
            speak(f"Playing a random song sir: {random_song}")
            os.startfile(os.path.join(music_dir, random_song))
            logging.info(f"Playing music: {random_song}")
        else:
            speak("No music files found in your music directory.")
    except Exception:
        speak("Sorry sir, I could not find your music folder.")


# genai model 

def genai_model_respone(user_input):
    # api key
    GEMINI_API_KEY = ""
    genai.configure(api_key= GEMINI_API_KEY) 
    
    # model selection
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = f"Your name is Kz, you act like Kz. Answer the provided question in short, Question: {user_input}"

    respone = model.generate_content(prompt)

    result = respone.text
    
    return result
    


# calling the greeting function(because greeting is only once time)
greeting()

while True:      
    # call the takeComman() function
    query = takeCommand().lower() # lower() convert the all command in lower case.

    # call and pass my query in speak function
    # speak(query)
    
    # To traditional way to handle our assistence

    # when asked the name
    if "name" in query:
        speak("My name is Kz")
        logging.info("user asked for assistant's name")
        
    # when asked the time
    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")
        logging.info("User asked for current time.")
    
    # Small talk
    elif "how are you" in query:
        speak("I am functioning at full capacity sir!")
        logging.info("User asked about assistant's well-being.")
    
        # made 
    elif "who made you" in query:
        speak("I was created by Raihan sir, a brilliant mind!")
        logging.info("User asked about assistant's creator.")
        
    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")
        logging.info("User expressed gratitude.")
        
    # open google [- using webbrowser() Becuase googel is web file or that is not our system file]
    elif "open google" in query:
        speak("ok sir. Please type her what do you want to read")
        webbrowser.open("google.com")
        logging.info("User requested to open Google.")
        
    # open Calculator [using subprocess because calculator is our system file]
    elif "open calculator" in query or "calculator" in query:
        speak("Opening  calculator...")
        subprocess.Popen("calc.exe") # calc.exe this is the executeable file of calculator
        logging.info("User requested to open Calculator.")     
        
    # open notepad (notepad our system file that way use subprocess)
    elif "open notepad" in query:
        speak("Opening  notepad...")
        subprocess.Popen("notepad.exe")
        logging.info("User requested to open Notepad.")
        
    # open terminal command prompt (notepad our system file that way use subprocess)
    elif "open terminal" in query or "command prompt" in query:
        speak("Opening terminal...")
        subprocess.Popen("cmd.exe") 
        logging.info("User requested to open Command Prompt.")
        
    # open google Calender
    elif "open calendar" in query or "calendar" in query:
        speak("Opening windows calendar")
        webbrowser.open("https://calender.google.com")  
        logging.info("User requested to open Calendar.")     
        
    # YouTube search
    elif "youtube" in query:
        speak("Opening YouTube for you.")
        query = query.replace("youtube", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        
        logging.info("User requested to search on YouTube.")
        
    # open facebook
    elif "open facebook" in query:
        speak("ok sir. opening facebook")
        webbrowser.open("facebook.com")
        logging.info("User requested to open Facebook.")
        
    # open github 
    elif "open github" in query:
        speak("ok sir. opening github")
        webbrowser.open("github.com")
        logging.info("User requested to open GitHub.")
        
     # speak joke  
    elif "joke" in query:
        jokes = [
            "Why don't programmers like nature? Too many bugs.",
            "I told my computer I needed a break. It said no problem, it will go to sleep.",
            "Why do Java developers wear glasses? Because they don't C sharp."
        ]
        speak(random.choice(jokes))
        logging.info("User requested a joke.")
    
    # search specific person in wikipedia 
    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        logging.info("User requested information from Wikipedia.")
    
    elif "play music" in query or "music" in query:
        music_dir = "paht_of_folder_music"
        play_music()
        
    elif "exit the program" in query:
        speak("Thank you for your time sir. Have a great day ahead!")
        print("Thank you for your time sir. Have a great day ahead!")
        logging.info("User exited the Program")
        exit()
    
    else:
        respone = genai_model_respone(query)
        speak(respone)
        logging.info("User asked for casual conversation")
       
    
    


