# ----------------------------------- #
#               APA - T1              #
#        Yago Carballo Barroso        #
# ----------------------------------- #

# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft 

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

# Write
sf.write('señal1.wav', señal1, fm)
sf.write('señal2.wav', señal2, fm)


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


N = 2**13                           # Número de puntos de la FFT (8192)
X1 = fft(señal1[0:L1], N)/L1               # Transformada de Fourier de la señal 1
X2 = fft(señal2[0:L2], N)/L2               # Transformada de Fourier de la señal 2
f = np.arange(N)*fm/N               # Eje de frecuencias

plt.figure(3)
plt.subplot(211)
plt.plot(f, 2*np.abs(X1))
plt.title(f'Transformada de la señal 1 de L={L1} muestras con DFT de N={N}')
plt.ylabel('Amplitud')
plt.subplot(212)
plt.plot(f, np.unwrap(np.angle(X1)))
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase')
plt.show()

plt.figure(3)
plt.subplot(211)
plt.plot(f, 2*np.abs(X2))
plt.title(f'Transformada de la señal 2 de L={L2} muestras con DFT de N={N}')
plt.ylabel('Amplitud')
plt.subplot(212)
plt.plot(f, np.unwrap(np.angle(X2)))
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase')
plt.show()

# 2
x_r,fs = sf.read('./señal2.wav')
Ty = 1/fx2
L2 = int(fm*5*Ty)
N = 2**13
fft_x_r = fft(x_r, N)/L2

plt.figure(4)
plt.plot(t[0:L2], x_r[0:L2])
plt.title('Señal de audio (5 periodos)')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo [s]')
plt.show()


X_R = fft(x_r[0:L2], N)/L2
f_x_r = np.arange(N)*fs/N
modul_X_R = 2*np.abs(X_R)
fase_X_R = np.unwrap(np.angle(X_R))

plt.figure(5)
plt.subplot(211)
plt.plot(f_x_r, modul_X_R)
plt.title(f'Transformada de la señal x_r de L={L2} muestras con DFT de N={N}')
plt.ylabel('Amplitud')
plt.subplot(212)
plt.plot(f_x_r, fase_X_R)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase')
plt.show()

# 3

