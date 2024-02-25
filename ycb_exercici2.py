# ----------------------------------- #
#               APA - T1              #
#              Exercici 2             #
#        Yago Carballo Barroso        #
# ----------------------------------- #

# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
# import sounddevice as sd # No es necesario para este ejercicio
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
modul_X_R = np.abs(X_R)
fase_X_R = np.angle(X_R)


plt.figure(1)
plt.subplot(311)
plt.plot(t[0:L], x_r[0:L])
plt.title('Señal de audio (5 periodos)')
plt.ylabel('Señal de 440 Hz')
plt.subplot(312)
plt.plot(modul_X_R)
plt.ylabel('Módulo de DTF')
plt.subplot(313)
plt.plot(fase_X_R)
plt.xlabel('Numero de muestra')
plt.ylabel('Fase de DTF')
plt.show()

# Explica el resultado del apartado anterior:

# La señal de audio de 440 Hz se representa en el dominio del tiempo y en el dominio de la frecuencia.
# En el dominio del tiempo, se observa la señal de audio de 440 Hz durante 5 periodos. En el dominio 
# de la frecuencia, se observa el módulo y la fase de la transformada de Fourier de la señal en función 
# del número de muestra. Finalmente, añadir que para obtener la frecuencia de la señal a partir del archivo 
# habría que analizar el paso mínimo entre armónicos.
