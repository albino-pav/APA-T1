# ----------------------------------- #
#               APA - T1              #
#              Exercici 1             #
#        Yago Carballo Barroso        #
# ----------------------------------- #

# ¡¡¡CUIDADO!!! con el volumen porque fx1 = 4000 Hz es especialmente molesto :)

# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft 
import os

# 1. Para fx = [4kHz, 440Hz]

T = 2.5                             # Duración de la señal
fm = 44100                          # Frecuencia de muestreo
fx1 = 4000                          # Frecuencia de la señal 1
fx2 = 440                           # Frecuencia de la señal 2
A = 1                               # Amplitud de la señal
L = int(fm*T)                       # Número de muestras
t = np.arange(L)/fm                 # Vector de tiempo
señal1 = A*np.cos(2*np.pi*fx1*t)    # Señal 1
señal2 = A*np.cos(2*np.pi*fx2*t)    # Señal 2

# Creamos los archivos de audio
actual_dir = os.path.dirname(os.path.abspath(__file__))
print(f'Los archivos de audio se han guardado en {actual_dir}')
sf.write(actual_dir + '/señal1.wav', señal1, fm)
sf.write(actual_dir + '/señal2.wav', señal2, fm)

plt.figure(1)
plt.subplot(211)
plt.plot(t, señal1)
plt.title('Señales')
plt.ylabel('Amplitud')
plt.subplot(212)
plt.plot(t, señal2)
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.show()

Tx = 1/fx1                          # Periodo de la señal 1
Ty = 1/fx2                          # Periodo de la señal 2
L1 = int(fm*5*Tx)                   # Número de muestras en 5 periodos de la señal 1
L2 = int(fm*5*Ty)                   # Número de muestras en 5 periodos de la señal 2

plt.figure(2)
plt.subplot(211)
plt.plot(t[0:L1], señal1[0:L1])
plt.title('Señales de 5 periodos')
plt.ylabel('Amplitud')
plt.subplot(212)
plt.plot(t[0:L2], señal2[0:L2])
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.show()

sd.wait()                           # Para que no se reproduzca en segundo plano
sd.play(señal1, fm)
sd.wait()                           # Para que no se reproduzcan a la vez
sd.play(señal2, fm)
sd.wait()                           # Para que se reproduzca hasta el final


N = 2**12                        # Número de puntos de la FFT (4096)
X1 = fft(señal1[0:L1], N)        # Transformada de Fourier de la señal 1
X2 = fft(señal2[0:L2], N)        # Transformada de Fourier de la señal 2
k = np.arange(N)                 # Eje de frecuencias

plt.figure(3)
plt.subplot(211)
plt.plot(k, np.abs(X1))
plt.title(f'Transformada de la señal 1 de L={L1} muestras con DFT de N={N}')
plt.ylabel('Amplitud')
plt.subplot(212)
plt.plot(k, np.angle(X1))
plt.xlabel('Numero de muestra')
plt.ylabel('Fase')
plt.show()

plt.figure(3)
plt.subplot(211)
plt.plot(k, np.abs(X2))
plt.title(f'Transformada de la señal 2 de L={L2} muestras con DFT de N={N}')
plt.ylabel('Amplitud')
plt.subplot(212)
plt.plot(k, np.angle(X2))
plt.xlabel('Numero de muestra')
plt.ylabel('Fase')
plt.show()
