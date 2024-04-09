from allosaurus.app import read_recognizer
import os
import pickle

# load your model
model = read_recognizer()

# assign directory
directory = 'audio.wav'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    #parse the file for directory, name with .wav, just name, and just .wav
    f = os.path.join(directory, filename)
    directory_, f = f.split('/')
    f2, extension = f.split(".")

    with open(f"pickle_files/{f2}.pkl", 'wb') as file:
    # run inference -> æ l u s ɔ ɹ s
        pickle.dump(model.recognize(directory_ + "/" + f, timestamp = True),file)