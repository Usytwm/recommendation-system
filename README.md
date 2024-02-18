# Sistema de Recomendación de Libros

# Informe de Proyecto

## Autores

- [Brian Ameht Inclan Quesada](https://github.com/Usytwm)
- [Eric Lopez Tornas](https://github.com/EricTornas)

## Descripción del Problema

El proyecto busca desarrollar un sistema de recomendación de libros que pueda sugerir libros similares a uno dado, basado en las reseñas y títulos de los libros. Esto se orienta a mejorar la experiencia de los usuarios en plataformas de lectura, ofreciéndoles opciones personalizadas acorde a sus intereses.

## Consideraciones Tomadas

Durante el desarrollo se consideró:

- La importancia de un preprocesamiento eficiente del texto para mejorar la calidad de las recomendaciones.
- La elección del modelo TF-IDF para la vectorización del texto y la descomposición SVD para reducir la dimensionalidad.
- La necesidad de calcular la similitud del coseno para identificar libros con contenido similar.
- La escalabilidad y eficiencia del sistema al manejar grandes conjuntos de datos.

## Ejecución del Proyecto

Para ejecutar el sistema de recomendación, sigue los siguientes pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/recommendation-system.git
   cd recommendation-system
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el startup.bat
   ```bash
   startup.bat
   ```

## Explicación de la Solución

El sistema se compone de varios módulos:

- Preprocesamiento: Utiliza PreprocessingUtils para limpiar y preparar los datos de texto, eliminando caracteres no deseados y normalizando el texto.

- Modelo TF-IDF: Convierte el texto en vectores numéricos que representan la importancia de las palabras en los documentos, utilizando TfidfModel.

- Modelo de Similitud: Emplea SimilarityModel para calcular la similitud entre libros usando el kernel lineal sobre los vectores TF-IDF.

- Sistema de Recomendación: RecommendationSystem utiliza el modelo de similitud para encontrar y recomendar libros similares basándose en un título específico.

- El flujo del sistema inicia con la carga de datos, seguido por el preprocesamiento, la vectorización TF-IDF, el cálculo de similitudes y, finalmente, la generación de recomendaciones.

## Insuficiencias y Mejoras Propuestas

El sistema actual, aunque funcional, podría mejorar en aspectos como:

- Integración de un componente de aprendizaje automático para ajustar las recomendaciones basadas en retroalimentación del usuario.
- Expansión del conjunto de datos para incluir más características de libros, como género o autor, para afinar las recomendaciones.
- Optimización de la eficiencia en el manejo de grandes volúmenes de datos.

## Dependencias del Proyecto

Las dependencias están listadas en requirements.txt, generado con el siguiente comando:

```bash
pip freeze > requirements.txt
```
