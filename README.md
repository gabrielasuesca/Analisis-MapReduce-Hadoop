# Análisis de ventas mediante Apache Hadoop y MapReduce

## Descripción
Proyecto académico que procesa un conjunto pequeño de transacciones de ventas para calcular el valor total vendido por ciudad mediante Hadoop Streaming y programas Mapper y Reducer desarrollados en Python.

## Tecnologías
- Apache Hadoop 3.5.0
- Hadoop Streaming 3.5.0
- Python 3
- HDFS
- Ubuntu sobre WSL (entorno utilizado en la práctica)

## Archivos
- `mapper.py`: lee el CSV, omite el encabezado y emite pares ciudad–valor de venta.
- `reducer.py`: suma los valores agrupados por ciudad.
- `ventas.csv`: conjunto de datos de ejemplo.
- `README.md`: documentación del proyecto.

## Datos de entrada
| Producto | Ciudad | Cantidad | Venta |
|---|---|---:|---:|
| Laptop | Bogotá | 2 | 2500000 |
| Monitor | Medellín | 3 | 1200000 |
| Teclado | Bogotá | 5 | 350000 |

## Lógica de procesamiento
1. **Mapper:** lee cada fila del CSV y emite `ciudad<TAB>venta`.
2. **Shuffle and Sort:** Hadoop agrupa y ordena las claves.
3. **Reducer:** suma los importes de cada ciudad.
4. **Salida:** escribe los totales en HDFS.

## Prueba local
Desde el directorio del proyecto:
```bash
cat ventas.csv | python3 mapper.py | sort | python3 reducer.py
```

Salida esperada:
```text
Bogotá    2850000
Medellín  1200000
```

## Ejecución con Hadoop Streaming
La práctica ejecutó Hadoop Streaming usando el archivo de entrada en HDFS:
- Entrada: `/mapreduce/ventas_input/ventas.csv`
- Salida: `/mapreduce/ventas_output`

El trabajo terminó correctamente y se verificó el contenido de `part-*` en HDFS.

**Nota sobre el entorno:** el registro de ejecución identificó `LocalJobRunner`; por tanto, la ejecución se realizó en modo local de un solo nodo. No se evaluó el rendimiento de un clúster multinodo.

## Resultados
| Ciudad | Ventas totales |
|---|---:|
| Bogotá | 2850000 |
| Medellín | 1200000 |
| **Total general** | **4050000** |

Los resultados coinciden con la agregación por ciudad recuperada de la práctica previa con Spark.

## Alcance y limitaciones
El archivo contiene tres transacciones y dos ciudades. Los resultados describen únicamente estos registros y no permiten generalizar tendencias comerciales.

## Autora
Gabriela Suesca Castillo  
Universidad de Cundinamarca  
Asignatura: Big Data
