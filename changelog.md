# Changelog Bot 50Cent

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