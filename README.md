# **Proyecto M4: Pokédex con Python**

## **Descripción**
Este proyecto consiste en la creación de una Pokédex interactiva que utiliza la API de [PokeAPI](https://pokeapi.co/). El programa permite consultar información detallada sobre cualquier Pokémon, mostrar datos clave como habilidades, movimientos, tipos, peso y tamaño, además de descargar y visualizar la imagen del Pokémon. También ofrece la funcionalidad de guardar esta información en un archivo JSON para su uso posterior.

## **Contenido**
Este repositorio incluye los siguientes archivos y carpetas:
- **`pokedex.py`**: Código principal que implementa las funcionalidades de la Pokédex.
- **`pokedex/`**: Carpeta que almacena los archivos JSON generados por el programa. Cada archivo contiene la información detallada de un Pokémon consultado.
- **`history.csv`**: Archivo que guarda el historial de búsquedas realizadas.
- **`README.md`**: Archivo de documentación que explica el propósito, funcionalidades y uso del proyecto.

## **Funcionalidades**
1. **Consulta de Información de Pokémon**:
   - Permite buscar un Pokémon por su nombre o su número.
   - Muestra los siguientes datos:
     - Nombre.
     - Peso (en hectogramos).
     - Tamaño (en decímetros).
     - Habilidades (máximo 2).
     - Movimientos (máximo 5).
     - Tipos.
   - Descarga y muestra la imagen del Pokémon.

2. **Almacenamiento de Datos**:
   - Guarda los datos del Pokémon en un archivo JSON dentro de la carpeta `pokedex`.
   - El archivo se nombra de acuerdo con el nombre del Pokémon.

3. **Historial de Consultas**:
   - Crea un archivo `history.csv` que registra todas las búsquedas realizadas con los datos básicos del Pokémon.

4. **Validación de Entradas**:
   - Verifica que el nombre del Pokémon sea válido.
   - Notifica al usuario si el Pokémon no existe o si hay problemas con la conexión.

5. **Interfaz Interactiva**:
   - Permite al usuario realizar consultas de manera sencilla desde la terminal.

## **Interacción**
1. Introduce el nombre o el número del Pokémon que deseas buscar (en minúsculas).
2. Observa la información detallada del Pokémon en la terminal.
3. La imagen del Pokémon se abrirá en el visor de imágenes predeterminado.
4. Los datos se guardarán automáticamente en la carpeta `pokedex`.

### **Salir del programa**
- Escribe `salir` cuando quieras terminar.

## **Reflexión**
El desarrollo de este proyecto permitió reforzar las siguientes habilidades:
- Uso de APIs REST mediante peticiones HTTP con la librería `requests`.
- Validación y manejo de excepciones para asegurar una experiencia de usuario robusta.
- Organización y manipulación de datos en formatos estructurados como JSON.
- Manejo de imágenes con la librería `Pillow` para abrir y guardar imágenes descargadas.
- Implementación de buenas prácticas de programación.

Este proyecto no solo consolidó los conceptos de programación adquiridos durante el módulo, sino que también fue una excelente oportunidad para explorar la integración de APIs en proyectos reales.

## **Contribuciones**
Si deseas mejorar este proyecto o añadir nuevas funcionalidades, no dudes en realizar un **pull request**. ¡Tu ayuda será bienvenida!

## **Licencia**
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.

## **Contacto**
Si tienes dudas o sugerencias, puedes contactarme en:
- **LinkedIn**: [Fabiola Gómez](https://www.linkedin.com/in/fabiola-gomez-576784269)
- **Instagram**: [@fabiolagmz09](https://www.instagram.com/fabiolagmz09/)
