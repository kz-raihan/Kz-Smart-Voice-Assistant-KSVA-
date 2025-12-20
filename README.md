# Kz-Smart-Voice-Assistant-KSVA-

KSVA ( **Kz Smart Voice Assistant** ) is a Python-based AI voice assistant capable of  **real-time speech recognition** ,  **natural voice responses** , and  **command execution like opening applications, searching on Google or Wikipedia, playing music randomly, telling jokes, and having small talk.**

The project focuses on building a clean, extensible, and practical voice-controlled system suitable for learning and real-world experimentation.

## 🚀 Features

KSVA provides a set of practical and interactive voice-driven capabilities designed for real-time usage:

* 🕒 **Context-Aware Greeting**
  * Greets the user intelligently based on the time of day (morning, afternoon, evening).
* 🎙️ **Voice Command Recognition**
  - Converts spoken commands into text using  **Google Speech Recognition.**
* 🔊 **Natural Voice Responses**
  - Delivers spoken feedback and responses using  **pyttsx3**.
* ⏰ **Time & Date Announcements**
  - Announces the current time and date on request.
* 🌐 **Wikipedia Search**
  - Fetches and reads out concise summaries from Wikipedia.
* 🔗 **Website Navigation**
  - Opens commonly used websites such as Google, Facebook, and YouTube.
* 🎵 **Music Playback**
  - Plays random music from a predefined local folder.
* 🖥️ **System Application Control**
  - Opens system utilities including Calculator, Notepad, and Command Prompt.
* 📅 **Calendar Access**
  - Opens Google Calendar directly in the browser.
* 😄 **Entertainment & Small Talk**
  - Tells jokes and responds to basic conversational prompts.
* ❌ **Graceful Exit**
  - Terminates the assistant smoothly via a voice command.

## **🏗️ System Architecture**

- User Speech

  ↓
- Speech Recognition (STT)

  ↓
- Command / Intent Processing

  ↓
- Action Execution

  ↓
- Text-to-Speech (TTS)

  ↓
- Voice Response

## 💻 Requirements

- Python 3.11 or higher

## **⚙️ How to run?**

1. Clone the repository

   ```
    git clone https://github.com/your-username/KSVA.git
    cd KSVA
   ```
2. Create and activate a virtual environment

   ```
    conda create -n KSVA python=3.11 -y

   ```
3. Activate virtual environment

   ```
     conda activate KSVA
   ```
4. Install required packages

   ```
     pip install -r requirements.txt
   ```
5. Run the script:

   ```
   python KSVA.py
   ```

## 🧪 Future Improvements

* Wake word detection ("Hey KSVA")
* NLP-based intent recognition
* Integration with APIs (weather, news, search)
* GUI or web dashboard
* Multi-language support

## 👤 Author

**KzRaihan**
Engineering Student | AI & Data Science Enthusiast

Inspired by **Boktiar Ahmed Bappy** and Tony Stark's JARVIS

## 📜 License

This project is licensed under the MIT License and it's open-source and free to use for learning purposes.
