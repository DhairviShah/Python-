
import os
from pydub import AudioSegment
from gtts import gTTS
import pandas as pd

def texttospeech(text,filename):
    mytxt = str(text)
    language = "hi"
    obj  = gTTS(text=mytxt,lang=language,slow=False)
    obj.save(filename)

def mergeaudios(audios):
    merged = AudioSegment.empty()
    for audio in audios:
        merged += AudioSegment.from_mp3(audio)
    return merged


def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    # attention sound
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1hindi.mp3", format="mp3")
    # starting city

    # "ko jane wali " sound
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3hindi.mp3", format="mp3")

    # via city

    # "raste pr " sound 
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5hindi.mp3", format="mp3")

    # destination city

    # "train info " sound
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7hindi.mp3", format="mp3")

    # train no. and name

    # "platform " sound
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9hindi.mp3", format="mp3")

    # platform number

    # "coming" sound
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11hindi.mp3", format="mp3")



def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    # print(df)
    for index, item in df.iterrows():
        #Starting city
        texttospeech(item['from'], '2hindi.mp3')

        #Via city
        texttospeech(item['via'], '4hindi.mp3')

        # Destination city
        texttospeech(item['to'], '6hindi.mp3')

        #Train no and name
        texttospeech(item['train_no'] + " " + item['train_name'], '8hindi.mp3')

        #Platform number
        texttospeech(item['platform'], '10hindi.mp3')

        audios = [f"{i}hindi.mp3" for i in range(1,12)]

        announcement = mergeaudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
    
