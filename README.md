# Primera tasca APA 2023: Anàlisi fitxer de so

## Nom i cognoms: Ferran Murcia Rull

## Representació temporal i freqüencial de senyals d'àudio

### Domini temporal


Per llegir, escriure i representar un fitxer en format `*.wav` en python podem fem servir els següents mòduls:

- Numpy:

    ```python
    import numpy as np
    ```

- Matplotlib:

    ```python
    import matplotlib.pyplot as plt
    ```

- Soundfile:

    ```python
    import soundfile as sf
    ```

Per **crear** i **guardar** a un fitxer un senyal sinusoidal de freqüència `fx Hz`, digitalitzat a `fm Hz`, de durada `T` segons i amplitud
`A` fem:

```python
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav
```

El resultat és un fitxer guardat al directori de treball i que es pot reproduir amb qualsevol reproductor d'àudio

Per **representar** gràficament 5 períodes de senyal fem:

```python
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 
```

El resultat del gràfic és:

![5 periodes de la sinusoide](img/sinusoide.png)

> Nota: Si es treballa amb ipython, es pot escriure %matplotlib i no cal posar el plt.show() per veure gràfics

El senyal es pot **escoltar (reproduir)** directament des de python important un entorn de treball amb els dispositius de so, com per
exemple `sounddevice`:

```python
import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio
```

### Domini transformat

Domini transformat. Els senyals es poden analitzar en freqüència fent servir la Transformada Discreta de Fourier.

La funció que incorpora el paquet `numpy` al submòdul `fft` és `fft`:

```python
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
```

I podem representar el mòdul i la fase, en funció de la posició de cada valor amb:

```python
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
```

![Transformada del senyal de Ls=90 mostres](img/TF.png)

## Proves i exercicis a fer i entregar

1. Reprodueix l'exemple fent servir diferents freqüències per la sinusoide. Al menys considera $f_x = 4$ kHz, a banda d'una
    freqüència pròpia en el marge audible. Comenta els resultats.


   ## Exercici  1
### Comentar resultats:

Hem modificat la freqüència del senyal 1 perquè sigui 4khz i hem creat una nova sinusoide de 440hz. Hem calculat les respectives fft. Com podem veure a la primera gràfica, ens mostra 5 períodes dels dos senyals sinusoidals. En la primera sinusoide l'eix d'abscisses en 5 períodes va del 0 als 0,001 s i a la segona del 0 al 0,01.

A causa de la freqüència de mostratge escollida podem observar que la primera sinusoide a tenir una elevada freqüència en representar-la sembla més aviat un senyal triangular.

A les respectives fft's veiem un pic a k=2500 que és correspon amb f0 = 4khz (k/N = f0/fm) i a la segona veiem un pic a k = 275 i a k = 4725 que és la repetició simètrica de la freqüència fonamental.




2. Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que has creat (`x_r, fm = sf.read('nom_fitxer.wav')`).

    - Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.

    - Explica el resultat del apartat anterior.


## Exercici 2
### Comentar resultats:

Com podem observar, en aquesta nova imatge hem utilitzat el anterior fitxer 'exemple_4kHz' i l'hem carregat i llegit per a aquest nou exercici. Hem hagut de modificar/ajustar la fx a 4kHz i la Tx per a obtenir el número de mostres corresponents per a aquesta nova figura.

La gràfica de la sinusoide i de la seva nova transformada és la mateixa que hem obtingut per a l'exercici anterior, ja que és l'arxiu que simplement hem llegit a l'exercici anterior.



3. Modifica el programa per representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en el marge de
    $0$ a $f_m/2$ en Hz.

    - Comprova que la mesura de freqüència es correspon amb la freqüència de la sinusoide que has fet servir.

    - Com pots identificar l'amplitud de la sinusoide a partir de la representació de la transformada?
      Comprova-ho amb el senyal generat.

    > NOTES:
    >
    > - Per representar en dB has de fer servir la fórmula següent:
    >
    > $X_{dB}(f) = 20\log_{10}\left(\frac{\left|X(f)\right|}{\max(\left|X(f)\right|}\right)$
    >
    > - La relació entre els valors de l'índex k i la freqüència en Hz és:
    >
    > $f_k = \frac{k}{N} f_m$


## Exercici 3
### Comentar resultats:

Hem hagut de canviar l'escala de representació agafant la meitat de número de mostres, calcula en db utilitzant la fòrmula donada evitant la divisó entre 0 sumant 1 al valor de la transformada després de fer el valor absolut.

Com podem veure en la ilustració de la transformada, tenim un pic a l'index de la k de 2500 el qual com em demostrat abans es correspont amb la freqüència de 4000 Hz. La fase correspont és la mateixa que teniem abans pero dividit entre 2.




4. Tria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity).
    Llegeix el fitxer d'àudio i comprova:

    - Freqüència de mostratge.
    - Nombre de mostres de senyal.
    - Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.
    - Representa la seva transformada en dB en funció de la freqüència, en el marge $0\le f\le f_m/2$.
    - Quines son les freqüències més importants del segment triat?


## Exercici 4
### Comentar resultats:

Hem agafat l'arxiu *'canso.wav'* mono de duració 4 segons on hem definit els següent punts:

- *fm* = agafat directament de la lectura del fitxer
- *L* = producte de *fm * x_r* (tamany de la cançó) 
- *ls* --> hem representat en 25 ms la transformada del senyal
- *X_db* --> hem passat a db la transformada del senyal en el marge indicat
- Les freqüència més important que podem notar és la freqüència fonamental on la podem trobar a *f0 = 153 Hz* i la segona a *f02 = 47846 Hz* que és el reflexa de la primera però és fora del rang audible i no és important com la primera.



## Entrega

- L'alumne ha de respondre a totes les qüestions formulades en aquest mateix fitxer, README.md.
  - El format del fitxer es l'anomenat *Markdown* que permet generar textos amb capacitats gràfiques (com ara *cursiva*, **negreta**,
  fòrmules matemàtiques, taules, etc.), sense perdre la llegibilitat en mode text.
  - Disposa d'una petita introducció a llenguatge de Markdown al fitxer `MARKDOWN.md`.
- El repositori GitHub ha d'incloure un fitxer amb tot el codi necesari per respondre les qüestions i dibuixar les gràfiques.
- El nom del fitxer o fitxers amb el codi ha de començar amb les inicials de l'alumne (per exemple, `fvp_codi.py`).
- Recordéu ficar el el vostre nom complet a l'inici del fitxer o fitxers amb el codi i d'emplar el camp `Nom i cognoms` a dalt de tot
  d'aquest fitxer, README.md.
