# ----------------------------------- #
#               APA - T1              #
#              Exercici 3             #
#        Yago Carballo Barroso        #
# ----------------------------------- #

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
# import sounddevice as sd
from numpy.fft import fft
import os

actual_dir = os.path.dirname(os.path.abspath(__file__))
x_r,fs = sf.read(actual_dir + '/señal2.wav')
frec = 440

T = 1/frec 
L = int(fs*5*T)
t = np.arange(L)/fs

N = 2**10 # 1024 muestras
X_R = fft(x_r[0:L], N)
modul_X_R = 20*np.log10(np.abs(X_R))
fase_X_R = np.angle(X_R)
f = np.arange(N)*fs/N

plt.figure(1)
plt.subplot(311)
plt.plot(t[0:L], x_r[0:L])
plt.title('Señal de audio (5 periodos)')
plt.ylabel('Señal de 440 Hz')
plt.subplot(312)
plt.plot(f[:N//2], modul_X_R[:N//2])
plt.ylabel('Módulo de DTF en dB')
plt.subplot(313)
plt.plot(fase_X_R)
plt.xlabel('Numero de muestra')
plt.ylabel('Fase de DTF')
plt.show()

# Comprova que la mesura de freqüència es correspon amb la freqüència de la sinusoide que has fet servir.
frecuencia_sinusoide = f[np.argmax(modul_X_R[:N//2])]
print(f"Frecuencia de la sinusoide: {frecuencia_sinusoide} Hz")

# Com pots identificar l'amplitud de la sinusoide a partir de la representació de la transformada?
amplitud_sinusoide = np.max(modul_X_R[:N//2])
print(f"Amplitud de la sinusoide: {amplitud_sinusoide} dB")