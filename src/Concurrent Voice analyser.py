import os
import speech_recognition as sr
from tqdm import tqdm
from multiprocessing.dummy import Pool

pool = Pool(8) # Number of concurrent threads

#with open("api-key.json") as f:
 #   GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()
#print(os.listdir('C://Users/Matias/Desktop/python'))

r = sr.Recognizer()
files = sorted(os.listdir('C://Users/Matias/Desktop/mb/Bayesian-Modulation/sounds'))#'C://Users/Matias/Desktop/python/sounds'


def transcribe(data):
    idx, file = data
    name = "parts/" + file

    print("Loading "+file + " started...")
    # Load audio file
    with sr.AudioFile('C://Users/Matias/Desktop/mb/Bayesian-Modulation/sounds/genevieve.wav') as source:
        audio = r.record(source)
    # Transcribe audio file
    print("Transcribing " + file + " started...")
    text = r.recognize_google(audio, None)
    print(name + " done")
    return {
        "idx": idx,
        "text": text
    }

all_text = pool.map(transcribe, enumerate(files))
pool.close()
pool.join()

print("finished transcribing !!!")
transcript = ""
for t in sorted(all_text, key=lambda x: x['idx']):
    total_seconds = t['idx'] * 30
    # Cool shortcut from:
    # https://stackoverflow.com/questions/775049/python-time-seconds-to-hms
    # to get hours, minutes and seconds
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)

    # Format time as h:m:s - 30 seconds of text
    transcript = transcript + "{:0>2d}:{:0>2d}:{:0>2d} {}\n".format(h, m, s, t['text'])

print(transcript)

with open("recognitionOutput.txt", "w") as f:
    f.write(transcript)