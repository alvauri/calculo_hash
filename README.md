# calculo_hash
Explicación simple de un hash y un ejemplo sencillo en python 

# TITULO: Calculo de Hash

Motivo: Anteriormente habia escuchado el termino de hash sin embargo no sabia que existian distintos algoritmos para calcularlos y las distintas caracteristicas que poseen cada uno de ellos. Es un tema que me intereso investigue varias fuentes y desarrolle un programa que calcule 

Objetivo: A continuación se hará una breve introdución al tema de hash, explicaré los principales y también sus caracteristicas. Luego pretendo hacer un ejemplo en código python de como calcular un hash usando el algoritmo SHA-256.

Bueno empezamos con la pregunta 
## ¿Que es un hash? 
Una hash es una función matemática que toma como entrada (como un archivo, una cadena de texto u otros datos) y produce una cadena de caracteres alfanumericos de longitud fija. Esa cadena de caracteres se llama "hash" o "digest". Los algoritmos hash son diseñados para ser unidireccionales, lo que significa que es muy dificil o practicamente imposible recrear la entrada original a partir del hash.

## Aplicaciones
Los hashes tienen varias aplicaciones importantes en la informatica, incluyendo:

1. **Verificacion de la intergridad**
2. **Constraseñas y autentificación**
3. **Almacenamiento seguro**
4. **Criptografia**
5. **Comparación eficiente**

## Colisiones
Es improtante destacar que aunque los hashes son utiles en muchos aspectos, no son totalmente aprueba de colisiones.

¿Que es una colisión?
Una colisión ocurre cuando dos entradas diferentes producen el mismo hash. Los algoritmos hash modernos están diseñados para minimizar el riesgo de colisiones, pero aún así es posible. Por esta razón es importante utilizar algoritmos seguros y adecuados para el propósito previsto.

## Principales algoritmos

Existen varios algoritmos que son ampliamente utilizados, cada uno con sus propias caracteristicas y aplicaciones. A continuación se listan los algoritmos hash más comunes.

1. **MD5 (Message-Digest Algorithm 5):** Fue uno de los algoritmos de hash más populares, pero se ha vuelto inseguro debido a vulnerabilidades que permiten colisiones. Ya no se recomienda su uso en aplicaciones de seguridad.

2. **SHA-1 (Secure Hash Algorithm 1):** Al igual que MD5, SHA-1 también ha sido considerado inseguro debido a vulnerabilidades y ataques exitosos. Su uso se desaconseja para aplicaciones sensibles a la seguridad.

3. **SHA-256, SHA-384, SHA-512 (Secure Hash Algorithm 2):** Estos son miembros de la familia SHA-2 y ofrecen niveles más altos de seguridad que MD5 y SHA-1. Son ampliamente utilizados en aplicaciones de seguridad, incluyendo criptografía y verificación de integridad.

4. **SHA-3 (Secure Hash Algorithm 3):** Diseñado para ser más resistente a ataques criptográficos avanzados, SHA-3 es la última incorporación a la familia de algoritmos de hash seguros. Aunque es relativamente nuevo, está ganando aceptación en aplicaciones de seguridad.

5. **Bcrypt:** Aunque no es estrictamente un algoritmo de hash, Bcrypt es un algoritmo de hashing de contraseñas que incorpora salting (añadir datos aleatorios a la entrada antes de calcular el hash) y una cantidad configurable de rondas de procesamiento. Es ampliamente utilizado para almacenar contraseñas de manera segura.

6. **Argon2:** Otro algoritmo de hash de contraseñas que se considera muy seguro. Fue el ganador del concurso Password Hashing Competition y se recomienda para aplicaciones que requieren almacenamiento seguro de contraseñas.

7. **Whirlpool:** Un algoritmo de hash diseñado para ser resistente a ataques criptográficos y con un tamaño de hash más grande que otros algoritmos, lo que lo hace adecuado para ciertos casos de uso.

Es importante elegir el algoritmo de hash adecuado según la aplicación y el nivel de seguridad requerido. En general, se recomienda utilizar algoritmos de hash más seguros y robustos, como SHA-256 o SHA-3, en lugar de algoritmos más antiguos y vulnerables como MD5 y SHA-1. Además, para almacenar contraseñas, es preferible utilizar algoritmos específicos de hash de contraseñas como Bcrypt o Argon2, ya que están diseñados para proteger contra ataques de fuerza bruta y otras amenazas.


A continuación voy a explicar como crear un algoritmo del tipo SHA-256 en python.

# Algoritmo SHA-256
El algoritmo SHA-256 es conocido por ser resistente a una amplia gama de ataques criptográficos, incluyendo colisiones y preimágenes. Esto significa que es extremadamente difícil encontrar dos mensajes diferentes que produzcan el mismo hash o encontrar un mensaje que genere un hash específico.

## Ejemplo de como calcular una algoritmo SHA-256 en python

Usaremos la biblioteca **haslib** 
