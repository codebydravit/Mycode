import speech_recognition as sr
import pyttsx3

#initize the recognizer
r =sr.Recognizer()

def record_text():
    #loop in case of errors
    while(1):
        print("@@@@@@@@@@@@@@ ready to speak @@@@@@@@@@@@@@@@@@@@")
        try:
            #use the microphone as source for input
            with sr.Microphone() as source2:
                #prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2,duration=0.2)

                #listens for the user's input
                audio2 = r.listen(source2)

                #Usingle google to recognize audio
                MyText = r.recognize_google(audio2)
                return MyText


        except sr.RequestError as e:
            print("@@@@@@@@@@@@@@@@ could not request results @@@@@@@@@@@@@@@@@;{0}".format(e))

        except sr.UnknownValueError:
            print("@@@@@@@@@@@@@ Unknown error occured @@@@@@@@@@@@@@")

    return
def output_text(text):
    f=open("output_text.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text=record_text()
    output_text(text)

    print("@@@@@@@@@@@@@@@@@@@@@@@@@ wrotetext @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
