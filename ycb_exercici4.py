# ----------------------------------- #
#               APA - T1              #
#              Exercici 4             #
#        Yago Carballo Barroso        #
# ----------------------------------- #

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft
import os 

actual_dir = os.path.dirname(os.path.abspath(__file__))
x_r,fs = sf.read(actual_dir + '/luzbel44.wav')

# ------------------------ #
# Freqüència de mostratge.
# ------------------------ #

print(f"Freqüència de mostratge: {fs} Hz")

# ---------------------------- #
# Nombre de mostres de senyal.
# ---------------------------- #

print(f"Nombre de mostres de senyal: {len(x_r)}")

# --------------------------------------------------------------------------------------- #
# Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.
# --------------------------------------------------------------------------------------- #

L = int(25e-3*fs)
mitad = int(len(x_r)/2)+293

plt.figure(1)
plt.plot(x_r[mitad:mitad+L])
plt.title('Evolución temporal del señal')
plt.show()

# ------------------------------------------------------------------------------------------- #
# Representa la seva transformada en dB en funció de la freqüència, en el marge 0 < f < fs/2.
# ------------------------------------------------------------------------------------------- #

N = 2**10 # 1024 muestras
modul_x = 20*np.log10(np.abs(fft(x_r[mitad:mitad+L],N)))
fase_x = np.angle(fft(x_r[mitad:mitad+L]))
f = np.arange(N)*fs/N 

plt.figure(2)
plt.subplot(211)
plt.plot(f[:int(len(f)/2)],modul_x[:int(len(f)/2)])
plt.title('Transformada en dB en función de la frecuencia')
plt.subplot(212)
plt.plot(f[:int(len(f)/2)],fase_x[:int(len(f)/2)])
plt.title('Fase en función de la frecuencia')
plt.show()
