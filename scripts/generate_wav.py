from pydub import AudioSegment
import os

# assign directory
directory = 'audio'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    #parse the file for directory, name with .mp3, just name, and just .mp3
    f = os.path.join(directory, filename)
    directory_, f = f.split('/')
    f2, extension = f.split(".")

    #converts the .mp3 file into a .wav file
    #exports it into /audio.wav
    sound = AudioSegment.from_mp3(directory + "/" + f)
    sound.export(f"audio.wav/{f2}.wav", format="wav")
