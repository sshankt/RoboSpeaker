import pyttsx3
engine = pyttsx3.init()

engine.say("'Hello sgithashank ', Welcome to the RoboSpeaker 1.2...")
engine.runAndWait()
while True:
    
    x = input("Enter what you want to Speak :")
    if x == "s":
        engine.say("Thanku for using me ....")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()



#use key s for stop all this program