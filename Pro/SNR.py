import matplotlib.pyplot as plt
import numpy as np
import imageio
import glob
import time

def signaltonoise(a, axis=0, ddof=0): # deprecated scipy function
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

artists = ('Beksinski','Hockney','Gogh')
arts = ( glob.glob("base\Beksinski\\*.jpg") , glob.glob("base\Hockney\\*.jpg") , glob.glob("base\Gogh\\*.jpg") )

# Tworzenie wektorów
avg = [0] * 3
img = [0] * 50
snr = np.zeros((3,50))
for I in range(3):
    #print(artists[I])
    i = 0
    for image_path in arts[I]:
        im = imageio.imread(image_path) #Wczytywanie obrazów z katalogu
        img[i] = im
        i += 1
    i=0
    for i in range(50): # Liczenie SNR (Signal to Noise Ratio)
        snr[I,i] = signaltonoise(img[i] , axis=None )
        #print(i+1, 'SNR =' , snr[I,i])
    avg[I] = np.average(snr[I])
    #print('Average SNR = ' , avg[I])
print('Beksinski Average SNR = ' , avg[0])
print('Hockney Average SNR = ' , avg[1])
print('Gogh Average SNR = ' , avg[2])
#plt.scatter(I+1, snr[0] ) #, s=area, c=colors, alpha=0.5)
I=0
SNR = np.zeros((50,3))
for I in range(3):
    i=0
    for i in range(50): # Odwracanie macierzy
        SNR[i,I] = snr[I,i]
np.savetxt("art.csv", SNR, delimiter=";")