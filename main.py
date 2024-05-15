from pytube import YouTube
import os
import speech_recognition as sr

import moviepy.editor as mp

def descargar_video_youtube(url, output_path):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(output_path=output_path)
    video_file = os.path.join(output_path, video.default_filename)
    wav_file = os.path.splitext(video_file)[0] + '.wav'
    clip = mp.AudioFileClip(video_file)
    clip.write_audiofile(wav_file)
    os.remove(video_file)
    return wav_file

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    text = recognizer.recognize_google(audio_data, language='es-MX')
    print("Transcripción: {}".format(text))

if __name__ == "__main__":
    video_url = input("Introduce la URL del video de YouTube: ")
    
    script_directory = os.path.dirname(__file__)
    print("El directorio del script es:", script_directory)

    audio_file_path = descargar_video_youtube(video_url, script_directory)
    print("El archivo de audio se guardó en:", audio_file_path)

    transcribe_audio(audio_file_path)
