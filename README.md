# Primera tasca APA 2023: Anàlisi fitxer de so

## Nom i cognoms: Maider Duró i Victoria Blanco

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

2. Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que has creat (`x_r, fm = sf.read('nom_fitxer.wav')`).

    - Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.

    - Explica el resultat del apartat anterior.

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

4. Tria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity).
    Llegeix el fitxer d'àudio i comprova:

    - Freqüència de mostratge.
    - Nombre de mostres de senyal.
    - Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.
    - Representa la seva transformada en dB en funció de la freqüència, en el marge $0\le f\le f_m/2$.
    - Quines son les freqüències més importants del segment triat?

## Entrega

- L'alumne ha de respondre a totes les qüestions formulades en aquest mateix fitxer, README.md.
  - El format del fitxer es l'anomenat *Markdown* que permet generar textos amb capacitats gràfiques (com ara *cursiva*, **negreta**,
  fòrmules matemàtiques, taules, etc.), sense perdre la llegibilitat en mode text.
  - Disposa d'una petita introducció a llenguatge de Markdown al fitxer `MARKDOWN.md`.
- El repositori GitHub ha d'incloure un fitxer amb tot el codi necesari per respondre les qüestions i dibuixar les gràfiques.
- El nom del fitxer o fitxers amb el codi ha de començar amb les inicials de l'alumne (per exemple, `fvp_codi.py`).
- Recordéu ficar el el vostre nom complet a l'inici del fitxer o fitxers amb el codi i d'emplar el camp `Nom i cognoms` a dalt de tot
  d'aquest fitxer, README.md.


1. Reprodueix l'exemple fent servir diferents freqüències per la sinusoide. Al menys considera 4 kHz, a banda d'una freqüència pròpia en el marge audible. Comenta els resultats.
En términos de percepción auditiva, cuando la frecuencia de una señal sinusoidal aumenta, la señal se vuelve más aguda y su duración percibida es menor. Este efecto se refleja en la representación digital de la señal cuando la frecuencia de muestreo se ajusta a la frecuencia de la señal

Cuando la frecuencia de muestreo es igual a la frecuencia de la señal sinusoidal en el margen audible, se produce lo que se conoce como aliasing. Esto ocurre porque el teorema de muestreo de Nyquist-Shannon establece que para evitar el aliasing, la frecuencia de muestreo debe ser al menos el doble de la frecuencia más alta presente en la señal que se está muestreando.

Si la frecuencia de muestreo es igual a la frecuencia de la señal sinusoidal, solo se captura una muestra de la señal por ciclo, lo que resulta en una señal muestreada que parece tener una frecuencia más baja de lo que realmente es. Esto puede percibirse como una señal más 'suave' o 'menos aguda' en el dominio temporal. A nivel perceptivo, la señal parece menos definida y su duración percibida es menor.

Por otro lado, si la frecuencia de muestreo es mayor que la frecuencia de la señal sinusoidal, se capturan múltiples muestras por ciclo de la señal, lo que permite una representación más precisa de la señal en el dominio temporal dentro del margen audible. Sin embargo, si la frecuencia de muestreo es demasiado alta, más allá de lo necesario según el teorema de Nyquist, se desperdician recursos de procesamiento y almacenamiento sin proporcionar beneficios adicionales. Además, el aliasing puede ocurrir si se presentan componentes de frecuencia fuera del rango de Nyquist y no se eliminan adecuadamente antes del muestreo.

En resumen, ajustar la frecuencia de muestreo dentro del margen audible es esencial para garantizar una representación fiel de la señal sonora. Esto afecta directamente a cómo percibimos la calidad y la definición del sonido dentro de ese margen.

2. gràfica que mostri 5 períodes del senyal i la seva transformada. Explica el resultat del apartat anterior.
Com podem veure al gràfic la forma de la ona de fx= 440 Hz a fx = 4000 Hz cambia considerablement. Abans amb un especte de ona sinusoidal y ara amb un aspecte triangular. Això es degut al "efecte aliasing".

Al aumentar la frecuencia de la nostre señal sinusoidal la fm no es lo suficentment alta per capturar correctament la forma d'ona sinusoidal.

Segons teorema Nyquist fm >= 2 fx. En el nostre cas fm/fs = 8000/4000 = 2. Per tant, a 4kHz la fx está al límit de frecuencia per tal de cumplir el teorema.

3. Modifica el programa per representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en el marge de _ a _enHz.
### 3.1 Com pots identificar l'amplitud de la sinusoide a partir de la representació de la transformada? Comprova-ho amb el senyal generat.
Al analizar la Transformada de Fourier de una señal, primero identificamos el pico más alto en el espectro, el cual corresponde a la frecuencia principal de la señal sinusoidal. La amplitud de esta sinusoide en el dominio temporal, A, se refleja en el valor del módulo del pico máximo en el espectro. Sin embargo, es importante tener en cuenta que la Transformada de Fourier de una sinusoide pura tiene dos picos simétricos, uno positivo y otro negativo, cada uno con una amplitud de A/2.

Para obtener la amplitud real de la señal en el dominio temporal a partir del módulo de la Transformada de Fourier, debemos multiplicar el valor del módulo por el número de puntos en la transformada. Esto se debe a que el módulo de la Transformada de Fourier se normaliza dividiéndolo por el número de puntos.

Además, al utilizar la fórmula en dB para el análisis de la señal, es posible observar los lóbulos de la frecuencia central y las resonancias de la sinusoide. Estos lóbulos y resonancias tienen su valor máximo de módulo en 0 dB, lo que indica su relación con la frecuencia fundamental de la señal.

Por ejemplo, si la amplitud de la señal en el dominio temporal es A=4, y el módulo del valor máximo de la señal en el dominio frecuencial es de 0 dB o 40, si aumentamos la amplitud por un factor k=10, A=40, y el módulo del valor máximo de la señal en el dominio frecuencial pasa a ser 400

Esto destaca la relación entre la amplitud de la señal y el valor máximo del módulo de la señal en el dominio frecuencial.
En resumen, al analizar la Transformada de Fourier de una señal sinusoidal, es fundamental entender cómo la amplitud y la frecuencia de la señal se reflejan en el espectro de frecuencias y cómo estos aspectos están relacionados entre sí.

4. Tria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity). Llegeix el fitxer d'àudio i comprova:
Freqüència de mostratge. Nombre de mostres de senyal.

### 4.1 Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.
### 4.2 Representa la seva transformada en dB en funció de la freqüència, en el marge 
### 4.3 Quines son les freqüències més importants del segment triat?
La més important es la freqüència de 500 Hz, corresponent a la freqüència de la sinusoide del fitxer d'audio creat
