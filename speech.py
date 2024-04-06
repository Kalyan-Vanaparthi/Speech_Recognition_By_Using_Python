import speech_recognition as sr

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source)

        print("Please say something Sir/Madam...🙏")

        audio = r.listen(source)

        print("Recognizing Now.......")

        # recognize speech using google
        try:
            print("You have said \n" + r.recognize_google(audio))
            
            global stoping_loop
            stoping_loop  = r.recognize_google(audio)
            if stoping_loop.lower() == "stop":
                print("speech Recgnition stoped Succesfully")
            else:
                print("Audio Recorded Successfully\n ")
            
        except Exception as e:
            print("Error : " + str(e))


        # write audio

        with open("recorded.mp3", "wb") as f:
            f.write(audio.get_wav_data())


print("NOTE:- If You Want To Quit This Speed Recognition Please Say > STOP")
if __name__ == "__main__":

        while True :
            main()
            if stoping_loop.lower() == "stop":
                print("Namaskaram🙏 Jai Hind ")
                break

