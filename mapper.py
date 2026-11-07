#!/usr/bin/env python3
import sys
import csv

lector = csv.reader(sys.stdin)

for fila in lector:
    if len(fila) != 4:
        continue

    producto, ciudad, cantidad, venta = fila

    if producto.strip().lower() == "producto":
        continue

    try:
        ciudad = ciudad.strip()
        valor_venta = int(venta.strip())
        print(f"{ciudad}\t{valor_venta}")
    except ValueError:
        continue
