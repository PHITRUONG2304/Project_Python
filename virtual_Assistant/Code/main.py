# pyttsx3 is a cross-platform text to speech library
import pyttsx3
import logging, datetime, os
import speech_recognition as sr
import webbrowser
import pygame
import time

class Virtual_Assistant:
    def __init__(self, log=True, voice_type='male'):
        self.engine = pyttsx3.init()
        self.tone = {"male":0, "female": 1}
        self.user = sr.Recognizer()
        if log: 
            self.logging_file = '../Logs/program_logs.log'
            logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s',filename = self.logging_file, filemode = 'a')
        # set voice for virtual assistant
        self.setVoice(voice_type)
        
    def run(self):
        self.welcome()
        while True:
            command = self.takeCommand().lower()
            if "google" in command:
                self.speakFromStr("What do you want to search")
                search = self.takeCommand().lower()
                url = 'https://www.google.com.vn/search?q=%s'%search
                webbrowser.get().open(url)
                self.speakFromStr("Here is your result when I search %s"%search)
                continue
            elif "youtube" in command:
                self.speakFromStr("What do you want to search")
                search = self.takeCommand().lower()
                url = 'https://www.youtube.com/search?q=%s'%search
                webbrowser.get().open(url)
                self.speakFromStr("Here is your result when I search %s"%search)
                continue
            elif "video" in command:
                self.speakFromStr("OK here you are")
                path = "../Musics/BabyShark.mp3"
                pygame.mixer.init()
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()
                MUSIC_END = pygame.USEREVENT+1
                pygame.mixer.music.set_endevent(MUSIC_END)
                while pygame.mixer.music.get_endevent() != MUSIC_END:
                    time.sleep(0.5)
                    
                continue
            elif "none" in command:
                self.speakFromStr("Sorry, I can't\nCan you ask me something else")
                continue
            elif "goodbye" in command:
                self.speakFromStr("Bye. Check Out GFG for more exciting things")
                exit()
            
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 2
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query= r.recognize_google(audio,language= 'en-in')
            print(f"You said: {query}\n")
        except Exception as e:
            self.speakFromStr("Sorry, I couldn't recognize what you said, speak once more.")
            print("Sorry, couldn't recognize what you said, speak once more.")
            return "none"
        return query
        
    def welcome(self):
        now = datetime.datetime.now().hour
        if now >= 0 and now < 12: self.speakFromStr('Good morning')
        elif now >= 12 and now < 18: self.speakFromStr("Good afternoon")
        else: self.speakFromStr("Good evening")
        self.speakFromStr("How can I help you")
        
    def setVoice(self, type):
        # get all voice in your machine: male tone and female tone
        voice = self.engine.getProperty('voices')
        try: 
            self.engine.setProperty("voice", voice[self.tone[type]].id)
            logging.info("%s voice is set"%type)
        except: 
            if self.logging_file != None:
                logging.error("Voice does not exist. Default: male voice") 
            self.engine.setProperty("voice", voice[self.tone["male"]].id)
                   
    def speakFromStr(self, str):
        print(self.getTimeNow(), ": " , str)
        self.engine.say(str)
        self.engine.runAndWait()
        
    def getTimeNow(self):
        return datetime.datetime.now().strftime("%I:%M:%p")
    
    
if __name__ == "__main__":
    assistant = Virtual_Assistant(log=True, voice_type='female')
    assistant.run()
    
