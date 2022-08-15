# Changelog Bot 50Cent

## Versión 2.2.4 - 15/08/2022
- ##### Se agregó el link que se utiliza para loguarse en MongoDB al archivo info.json.

## Versión 2.2.3 - 11/08/2022
- ##### Se agregaron nuevas imagenes.

## Versión 2.2.2 - 28/07/2022
- ##### Se cambió la implementación de la espera para que a partir de que se sube una foto se empiecen a contar las 2 horas, en vez dar la posibilidad de subir una foto por cada ventana de 2 horas, pudiendo postear, por ejemplo, a las 11:40 y a las 12:00 cuando se renueva la ventana, generando muchos posteos seguidos.
- ##### Se añadió el tiempo de ultimo posteo a MongoDB.

## Versión 2.2.1 - 27/07/2022
- ##### Ahora el bot espera 2 horas para poder postear un nuevo meme, se hizo esto para evitar que se suba varias veces en la mísma hora cuando el precio fluctua mucho.

## Versión 2.2 - 22/07/2022
- ##### Se implementó MongoDB como base de datos de donde se obtienen los datos actualizados para solucionar las limitaciones de Heroku. (Gracias @octokerbs)

## Versión 2.1 - 21/07/2022
- ##### Se detectó que en Heroku si el programa se reinicia los cambios efectuados sobre los archivos desaparecen, por lo tanto ahora el programa obtiene datos no constantes de una API propia.
### To-Do
 - ##### Implementar la actualización de la API de forma manual, por ahora solo funciona cambiando los valores manualmente.

## Versión 2.0 - 19/07/2022
- ##### Ahora el bot actualiza el meme cada vez que el valor del dolar cambia, no simplemente a la misma hora todos los dias.
- ##### Overhaul al sistema de generación de imagenes, ahora el texto ocupa un espacio proporcional al tamaño de la imagen.
- ##### Reestructuración de los archivos para mejor entendibilidad.
- ##### Añadida una nueva imagen para más variedad.

## Versión 1.4 - 14/07/2022
- ##### Se migraron todas las llamadas posibles a la API 2.0 de Twitter. (La única pendiente es la llamada para subir imagenes que no existe un equivalente en la versión 2.0).
- ##### Optimizaciones varias de código.

## Versión 1.3 - 11/07/2022
- ##### Añadida función para poder contestar tweets, si un usuario menciona al bot con su arroba y el mensaje contiene el hashtag #dolar el bot genera una imagen y la responde.
- ##### Optimizaciones varias de código.

## Versión 1.2 - 10/07/2022
- ##### Añadidas varias imagenes nuevas.
- ##### Implementada una función que cicla entre imagenes para nunca elegir la misma imagen que el dia anterior.
- ##### Se hizo más ancho el outline del texto.

## Versión 1.1 - 10/07/2022
- ##### Implementada automatización del bot y añadidos archivos necesarios para que el bot corra sobre Heroku.
- ##### Las Keys ahora se obtienen de el archivo 'keys.json' en lugar de estar pegadas en el código.

## Versión 1.0 - 09/07/2022
- ##### Release Inicial, el bot es completamente funcional.
### To-Do
 - ##### Falta implementar la automatización para no tener que disparar la subida de la imagen manualmente.