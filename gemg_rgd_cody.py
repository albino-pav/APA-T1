#Exercici-1
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=4000                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx = 1 / fx
Ls = int(fm * 5* Tx)

plt.figure(0)
plt.plot(t[0:Ls], x[0:Ls])
plt.xlabel('t en segons')
plt.title('5 periodes de la sinusoide')
plt.show()

from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

#Exercici-2
x_r, fm = sf.read('so_exemple1.wav')
T = (1/fm)*len(x_r)
Tm=1/fm
t= Tm*np.arange(L)
fx=4000
Tx = 1/ fx
Ls=int(fm*5*Tx)
plt.figure(2)
plt.plot(t[0:Ls], x_r[0:Ls])
plt.xlabel('t en segons')
plt.title('5 periodes de la sinusoide')
plt.show()
sd.play(x_r,fm)

X=fft(x_r[0: Ls], N)
N=5000
k= np.arange(N)
plt.figure(3)
plt.subplot(211)
plt.plot(k,abs(X))
plt.title(f'Transformada del senyal de Ls= {Ls} mostres amb DFT de N= {N}')
plt.ylabel('|X[k]')
plt.subplot(212)
plt.plot(k,np.unwrap(np.angle(X)))
plt.xlabel('Index k')
plt.ylabel('$\phi_x[k]$')
plt.show()

#Exercici-3
T = 2.5
fm=8000
fx=440
A=4
pi=np.pi
L = int(fm *T)
Tm=1/fm
t= Tm*np.arange(L)
x=A*np.cos(2 * pi * fx * t)
sf.write('so_exemple3.wav', x, fm)
Tx = 1/ fx
Ls=int(fm*5*Tx)
plt.figure(4)
plt.plot(t[0:Ls], x[0:Ls])
plt.xlabel('t en segons')
plt.title('5 períodes')
plt.show()
sd.play(x,fm)

N=5000
X=fft(x[0 : Ls], N)
k=np.arange(N)
plt.figure(5)
dB = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N
plt.subplot(211)
plt.plot(fk,dB[0:N//2+1])
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')
plt.ylabel('Mòdul en dB')
plt.subplot(212)
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )
plt.xlabel('f en Hz')
plt.ylabel('$\phi_x[k]$')
plt.show()

#Exercici-4
T= 0.025
data, fm =sf.read('luzbel44.wav')
L = int(fm * T)
Tm=1/fm
t=Tm*np.arange(L)
plt.figure(6)
plt.plot(t[0:L],data[0:L])
plt.xlabel('t en segons')
plt.title('Exercici 4')
plt.show()

N=5000
X=fft(data[0 : L], N)
k=np.arange(N)
plt.figure(7)
dB = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N
plt.subplot(211)
plt.plot(fk,dB[0:N//2+1])
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')
plt.ylabel('Mòdul en dB')
plt.subplot(212)
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )
plt.xlabel('f en Hz')
plt.ylabel('$\phi_x[k]$')
plt.show()