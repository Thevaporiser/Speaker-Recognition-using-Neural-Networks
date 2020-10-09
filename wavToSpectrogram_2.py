import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
import IPython.display as ipd

class wave2Spec:
    
    def convert(audio_clips, save_image):
        #audio_fpath = "/Users/priyanshringe/Documents/College_Stuff/DATASETS/minor_dataset/testSpectro"
        #audio_clips = os.listdir(audio_fpath)
        #print("No. of .wav files in audio folder = ",len(audio_clips))

        x, sr = librosa.load(audio_clips, sr=22050)#44100)

        #print(type(x), type(sr))
        #print(x.shape, sr)
        '''
        plt.figure(figsize=(14, 5))
        librosa.display.waveplot(x, sr=sr)

        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        plt.figure(figsize=(14, 5))
        librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
        plt.colorbar()
        '''
        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        
        plt.figure(figsize=(14, 5))
        librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
        plt.colorbar()
        
        plt.savefig(save_image)
    
   
        
    
