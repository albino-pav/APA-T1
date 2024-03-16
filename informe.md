# RESPOSTES PRACTICA 1:

# Maider Duró
# Victoria Blanco 


## 1. Reprodueix l'exemple fent servir diferents freqüències per la sinusoide. Al menys considera 4 kHz, a banda d'una freqüència pròpia en el marge audible. Comenta els resultats.

En términos de percepción auditiva, cuando la frecuencia de una señal sinusoidal aumenta, la señal se vuelve más aguda y su duración percibida es menor. Este efecto se refleja en la representación digital de la señal cuando la frecuencia de muestreo se ajusta a la frecuencia de la señal

Cuando la frecuencia de muestreo es igual a la frecuencia de la señal sinusoidal en el margen audible, se produce lo que se conoce como aliasing. Esto ocurre porque el teorema de muestreo de Nyquist-Shannon establece que para evitar el aliasing, la frecuencia de muestreo debe ser al menos el doble de la frecuencia más alta presente en la señal que se está muestreando.

Si la frecuencia de muestreo es igual a la frecuencia de la señal sinusoidal, solo se captura una muestra de la señal por ciclo, lo que resulta en una señal muestreada que parece tener una frecuencia más baja de lo que realmente es. Esto puede percibirse como una señal más 'suave' o 'menos aguda' en el dominio temporal. A nivel perceptivo, la señal parece menos definida y su duración percibida es menor.

Por otro lado, si la frecuencia de muestreo es mayor que la frecuencia de la señal sinusoidal, se capturan múltiples muestras por ciclo de la señal, lo que permite una representación más precisa de la señal en el dominio temporal dentro del margen audible. Sin embargo, si la frecuencia de muestreo es demasiado alta, más allá de lo necesario según el teorema de Nyquist, se desperdician recursos de procesamiento y almacenamiento sin proporcionar beneficios adicionales. Además, el aliasing puede ocurrir si se presentan componentes de frecuencia fuera del rango de Nyquist y no se eliminan adecuadamente antes del muestreo.

En resumen, ajustar la frecuencia de muestreo dentro del margen audible es esencial para garantizar una representación fiel de la señal sonora. Esto afecta directamente a cómo percibimos la calidad y la definición del sonido dentro de ese margen.


## 2. gràfica que mostri 5 períodes del senyal i la seva transformada. Explica el resultat del apartat anterior.


Com podem veure al gràfic la forma de la ona de fx= 440 Hz a fx = 4000 Hz cambia considerablement. Abans amb un especte de ona sinusoidal y ara amb un aspecte triangular. Això es degut al "efecte aliasing".

Al aumentar la frecuencia de la nostre señal sinusoidal la fm no es lo suficentment alta per capturar correctament la forma d'ona sinusoidal.

Segons teorema Nyquist fm >= 2 fx.
En el nostre cas fm/fs = 8000/4000 = 2.
Per tant, a 4kHz la fx está al límit de frecuencia per tal de cumplir el teorema.


## 3. Modifica el programa per representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en el marge de _ a _enHz.

    ### 3.1 Com pots identificar l'amplitud de la sinusoide a partir de la representació de la transformada? Comprova-ho amb el senyal generat.

    
Al analizar la Transformada de Fourier de una señal, primero identificamos el pico más alto en el espectro, el cual corresponde a la frecuencia principal de la señal sinusoidal. La amplitud de esta sinusoide en el dominio temporal, 
A, se refleja en el valor del módulo del pico máximo en el espectro. Sin embargo, es importante tener en cuenta que la Transformada de Fourier de una sinusoide pura tiene dos picos simétricos, uno positivo y otro negativo, cada uno con una amplitud de A/2.

Para obtener la amplitud real de la señal en el dominio temporal a partir del módulo de la Transformada de Fourier, debemos multiplicar el valor del módulo por el número de puntos en la transformada. Esto se debe a que el módulo de la Transformada de Fourier se normaliza dividiéndolo por el número de puntos.

Además, al utilizar la fórmula en dB para el análisis de la señal, es posible observar los lóbulos de la frecuencia central y las resonancias de la sinusoide. Estos lóbulos y resonancias tienen su valor máximo de módulo en 0 dB, lo que indica su relación con la frecuencia fundamental de la señal.

Por ejemplo, si la amplitud de la señal en el dominio temporal es A=4, y el módulo del valor máximo de la señal en el dominio frecuencial es de 0 dB o 40, si aumentamos la amplitud por un factor k=10, A=40, y el módulo del valor máximo de la señal en el dominio frecuencial pasa a ser 400


1.   Esto destaca la relación entre la amplitud de la señal y el valor máximo del módulo de la señal en el dominio frecuencial.

En resumen, al analizar la Transformada de Fourier de una señal sinusoidal, es fundamental entender cómo la amplitud y la frecuencia de la señal se reflejan en el espectro de frecuencias y cómo estos aspectos están relacionados entre sí.


## 4. Tria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity). Llegeix el fitxer d'àudio i comprova:

Freqüència de mostratge.
Nombre de mostres de senyal.

    ### 4.1 Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.
    ### 4.2 Representa la seva transformada en dB en funció de la freqüència, en el marge 
    ### 4.3 Quines son les freqüències més importants del segment triat?

La més important es la freqüència de 500 Hz, corresponent a la freqüència de la sinusoide del fitxer d'audio creat