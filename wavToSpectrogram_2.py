import os
import matplotlib.pyplot as plt
import gc

#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
import IPython.display as ipd

class wave2Spec:
    
    def convert(audio_clips, save_image):
        
        x, sr = librosa.load(audio_clips, sr=22050)#44100)
        
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
        plt.clf()
        plt.close("all")
        gc.collect()
   
        
    
