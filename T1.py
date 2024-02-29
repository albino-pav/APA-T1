import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

# Reprodueix l'exemple fent servir diferents freqüències per 
# la sinusoide. Al menys considera fx = 4 kHz, a banda d'una
# freqüència pròpia en el marge audible. Comenta els resultats.

T = 2.5
fm = 48000
fx = 1000
A = 4
pi = np.pi
L = int(fm*T)
Tm = 1/fm
t = Tm*np.arange(L)
x = A*np.sin(2*pi*fx*t)
sf.write('s_sin1.wav', x, fm)
sd.play(x, fm)

# Com més alta la freqüència de la sinusoide (so més agut), més alta ha de ser la freqüència 
# de mostreig per poder representar gràficament la sinusoide d'una manera correcta 
# i evitar aliasing. 

# Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que 
# has creat (`x_r, fm = sf.read('nom_fitxer.wav')`).
#   - Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.
#   - Explica el resultat del apartat anterior.

x1, fm1 = sf.read("s_sin1.wav")
Tx=1/fx                                   
Ls=int(fm*5*Tx)                           

plt.figure(0)                             
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                 
plt.title('5 periodes de la sinusoide')   
plt.show()