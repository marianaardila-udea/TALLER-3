# Taller 3

**Nombre:**  Mariana Ardila Alvarez 
**Grupo:** 3

## 1. Descripción del proyecto
La aplicación en Python permite leer automáticamente cualquier carpeta con archivos DICOM, extraer todos los metadatos pedidos que son necesarios para el analisis e identificacion de cada archivo, calcular la intensidad promedio de píxeles y generar un archivo CSV.
Se realizó de forma directa ya que en las indicaciones asi lo pedia, por lo que, si se desea analizar una carpeta diferente a la que se pone por defecto en la terminal se debe poner: python procesador_dicom.py nombrecarpeta, en mi caso para los datos que se analizaron es datos1 (carchivos obtenidos de clase teorica de DICOM) 

## 2. DICOM vs HL7
Ambos estándares son cruciales porque permiten que diferentes sistemas de salud "hablen el mismo idioma", facilitando el intercambio seguro de información clínica entre hospitales, clínicas, laboratorios y otros proveedores.

DICOM
-Se enfoca específicamente en imágenes médicas (radiografías, tomografías, resonancias, ecografías)
-Define cómo se capturan, almacenan, transmiten y visualizan las imágenes
-Incluye no solo la imagen en sí, sino también metadatos clínicos asociados (datos del paciente, parámetros del estudio, información del equipo)

HL7 
-Abarca información clínica general: historias clínicas, resultados de laboratorio, órdenes médicas, datos administrativos, facturación
-Se centra en la estructura y semántica de los mensajes entre sistemas de información hospitalarios
-Facilita la integración entre sistemas heterogéneos (HIS, LIS, farmacia, etc.)

Diferencias:

DICOM es un estándar especializado y vertical para el dominio específico de la imagenología médica, mientras que HL7 es un estándar horizontal y generalista que cubre prácticamente todos los aspectos del flujo de información clínica y administrativa en salud.

En la práctica, ambos coexisten: DICOM gestiona las imágenes en el PACS (Picture Archiving and Communication System), mientras HL7 comunica esas imágenes con el resto del ecosistema hospitalario (HIS, EHR).

## 3. Relevancia del análisis de intensidades
El análisis de la distribución de intensidades (por ejemplo, mediante histogramas) es fundamental porque permite:
-Identificar características del tejido: tejidos como hueso, grasa, aire o lesiones tienen rangos específicos de intensidad.
-Evaluar la calidad de la imagen: distribuciones anómalas pueden indicar ruido, mala exposición o errores de adquisición.
-Definir umbrales para segmentación: muchos algoritmos dependen de rangos de intensidad para separar estructuras anatómicas.
-Detectar artefactos o valores atípicos: intensidades inesperadas pueden señalar artefactos metálicos, movimiento, etc.
-Normalizar imágenes antes de análisis avanzado: ajustar contraste, corregir intensidades o estandarizar cortes mejora modelos posteriores.

## 4. Dificultades y herramientas
Durante el proyecto se presentaron varias dificultades:
-Variabilidad entre archivos DICOM (diferentes modalidades, fabricantes o estructuras internas).
-Valores inconsistentes en algunos metadatos que generan warnings o requieren manejo especial.
-Diferencias en dimensiones, spacing y orientación entre estudios.
-Gestión de carpetas con múltiples series y subseries.
-Necesidad de visualizar datos volumétricos de forma adecuada.
Las herramientas de Python (como pydicom, numpy, matplotlib, SimpleITK y pandas) fueron esenciales porque:
-Facilitan la lectura y manipulación flexible de archivos DICOM, tambien permiten realizar cálculos numéricos rápidos sobre matrices de imagen, además ofrecen métodos para preprocesamiento, visualización y análisis estadístico.

En conjunto, Python permitió integrar lectura, análisis, visualización y preprocesamiento en un flujo de trabajo unificado y reproducible.
