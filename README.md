# SRI-2022
Elementos generales del proyecto: \
  El elegido para nuestra primera implementación fue el modelo vetorial y como colecciones de prueba se pueden utilizar Cranfield y 20Newsgroups; ambos en formato .json.\
Detalles sobre la implementación: \
   El lenguaje utilizado es python que nos ofrece como ventaja dos bibliotecas: nlkt, con múltiples opciones para el procesamiento de lenguaje(los documentos y las querys se preprocesan utilizando esta biblioteca), y sklearn, utilizado para contruir las matrices de frecuencias y de pesos, a partir de los documentos ya procesados.\
  Para la ejecución:
    En el archivo "requirements.txt" se encuentran las dependencias del proyecto.Para su instalación ejecutar, en el entorno del proyecto, el comando: \
      pip install -r requirements.txt \
  Abrir el archivo "app_test.py",dentro del código especificar la colección a usar y la query, en el archivo hay una explicación detallada de como hacer esta operación.\
  Ejecutar el archivo mediante el comando de consola:\
     python app_test.py \
  Esto devuelve un array de índices que representa el ranking de los documentos.
