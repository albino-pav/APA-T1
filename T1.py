import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft

T = 2.5
fm = 48000
fx = 2000
A = 4
pi = np.pi
L = int(fm*T)
Tm = 1/fm
t = Tm*np.arange(L)
x = A*np.sin(2*pi*fx*t)
sf.write('s_sin1.wav', x, fm)
#sd.play(x, fm)

Tx=1/fx                                   
Ls=int(fm*5*Tx)                           

plt.figure(1)                             
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                 
plt.title('5 periodes de la sinusoide')   
plt.show()

N = 5000
X = fft(x[0 : Ls], N)

k=np.arange(N)                        

plt.figure(2)                         
plt.subplot(211)                      
plt.plot(k,abs(X))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))    
plt.xlabel('Index k')                 
plt.ylabel('$\phi_x[k]$')             
plt.show() 

XdB = 20*np.log10(abs(X)/max(abs(X)))
fk = k*fm/N

plt.figure(3)                                            
plt.plot(fk[0:int(len(fk)/2)],XdB[0:int(len(fk)/2)])                    
plt.title(f'Mòdul de la transformada del senyal en el marge de 0 a fm/2')  
plt.xlabel('fk')                 
plt.ylabel('X(dB)') 
plt.show()

# Fitxer de veu

x1, fm1 = sf.read("APA_T1\mao3_1.wav")
print('\n', "Freqüència de mostratge: " + str(fm1))
print(" Mostres de senyal: " + str(len(x1)))

t_seg = 25E-3
m_inici = 15500
m_final = int(m_inici + t_seg * fm1)
Tm1 = 1 / fm1
tx_seg = np.arange(0, t_seg, Tm1)

plt.figure(4)                             
plt.plot(tx_seg, x1[m_inici:m_final])                
plt.xlabel('t')                 
plt.ylabel('x')
plt.title('Senyal en el domini temporal')   
plt.show()

# N = 5000
X1 = fft(x1[m_inici:m_final], N)
k1 = np.arange(N)  
XdB1 = 20*np.log10(abs(X1)/max(abs(X1)))
fk1 = k1*fm1/N

plt.figure(5)                                            
plt.plot(fk1[0:int(len(fk1)/2)],XdB1[0:int(len(fk1)/2)])                    
plt.title(f'Mòdul de la transformada del senyal en el marge de 0 a fm/2')  
plt.xlabel('fk')                 
plt.ylabel('X(dB)') 
plt.show()