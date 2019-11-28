import os
import speech_recognition as sr
from tqdm import tqdm
from multiprocessing.dummy import Pool


recognizer = sr.Recognizer()

def getAudio(file):
    with sr.AudioFile(file) as source:
        return recognizer.record(source)



list = ['C://Users/Matias/Desktop/mb/Bayesian-Modulation/sounds/genevieve.wav','C://Users/Matias/Desktop/mb/Bayesian-Modulation/sounds/Cópia.wav']
list = map(lambda x: getAudio(x), list)
list= map(lambda x: recognizer.recognize_google(x, None), list)

all_text='\n'.join(list)

with open("recognitionOutput.txt", "w") as f:
    f.write(all_text)


#files = sorted(os.listdir('C://Users/Matias/Desktop/mb/Bayesian-Modulation/sounds'))
'''all_text = pool.map(transcribe, enumerate(files))
pool.close()
pool.join()
'''