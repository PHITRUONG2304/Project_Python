from cmath import log
import pyttsx3, logging, datetime, os
import speech_recognition as sr
import pyaudio
import webbrowser


class Virtual_Assistant:
    def __init__(self, log=True, voice_type='male'):
        self.ast = pyttsx3.init()
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
            command = self.get_command().lower()
            if "google" in command:
                self.speakFromStr("What do you want to search")
                search = self.get_command().lower()
                url = 'https://www.google.com.vn/search?q=%s'%search
                webbrowser.get().open(url)
                self.speakFromStr("Here is your result when I search %s"%search)
            elif "youtube" in command:
                self.speakFromStr("What do you want to search")
                search = self.get_command().lower()
                url = 'https://www.youtube.com/search?q=%s'%search
                webbrowser.get().open(url)
                self.speakFromStr("Here is your result when I search %s"%search)
            elif "open video" in command:
                self.speakFromStr("OK here you are")
                path = "../Musics/BabyShark.mp3"
                os.open(path=path)
            elif "quit" or 'close' or 'exit' in command:
                self.speakFromStr("Do you really want to quit")
                while True:
                    command = self.get_command().lower()
                    if command != '': break
                    
                if 'yes' in command:
                    self.speakFromStr("Good bye See you later")
                    break
            
    def get_command(self):
        with sr.Microphone() as source:
            self.user.pause_threshold = 3
            audio = self.user.listen(source)
        query = ''
        try:
            query = self.user.recognize_google(audio, language='en-US')
            print("User: " + query)
        except Exception as e:
            if self.logging_file != None:
                logging.warning("User's command is not regconized")
                logging.warning(e)
            self.speakFromStr("Sorry I don't understand what you say")
            self.speakFromStr("Please say it again")
        return query
    
    def welcome(self):
        now = datetime.datetime.now().hour
        if now >=0 and now < 12: self.speakFromStr('Good morning')
        elif now >= 12 and now < 18: self.speakFromStr("Good afternoon")
        else: self.speakFromStr("Good evening")
        self.speakFromStr("How can I help you")
        
    def setVoice(self, type):
        # get all voice in your machine: male tone and female tone
        voice = self.ast.getProperty('voices')
        try: 
            self.ast.setProperty("voice", voice[self.tone[type]].id)
            logging.info("%s voice is set"%type)
        except: 
            if self.logging_file != None:
                logging.error("Voice does not exist. Default: male voice") 
            self.ast.setProperty("voice", voice[self.tone["male"]].id)
                   
    def speakFromStr(self, str):
        print(self.getTimeNow(), ": " , str)
        self.ast.say(str)
        self.ast.runAndWait()
        
    def getTimeNow(self):
        return datetime.datetime.now().strftime("%I:%M:%p")
    
    
if __name__ == "__main__":
    assistant = Virtual_Assistant(log=True, voice_type='female')
    assistant.run()
    
