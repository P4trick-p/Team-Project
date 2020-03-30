import numpy as np
import glob
import imageio
import time
import matplotlib.pyplot as plt

def signaltonoise(a, axis=0, ddof=0): # deprecated scipy function
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

arty = ('Beksinski','Hockney','Gogh')
art = ( glob.glob("base\Beksinski\\*.jpg") , glob.glob("base\Hockney\\*.jpg") , glob.glob("base\Gogh\\*.jpg") )


# Tworzenie wektorów
avg = [0] * 3
img = [0] * 50
snr = [[0]*50]*3
#snr = [0] * 50
for X in range(3):
    print(arty[X])
    i = 0
    for image_path in art[X]:
        im = imageio.imread(image_path) #Wczytywanie obrazów z katalogu
        img[i] = im
        i += 1

    for x in range(50): # Liczenie SNR (Signal to Noise Ratio) //
        snr[X][x] = signaltonoise(img[x] , axis=None )
        print(x+1, 'SNR =' , snr[X][x])
        #tmp[x] = snr[X][x]
    avg[X] = np.average(snr[X])
    #time.sleep(0.5)
    print('Average SNR = ' , avg[X])
    #print(tmp)
    #time.sleep(2)
#plt.scatter(X+1, snr[0] ) #, s=area, c=colors, alpha=0.5)

plt.scatter(snr, snr[X][:] ) #, s=area, c=colors, alpha=0.5)
plt.show()