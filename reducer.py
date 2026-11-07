#!/usr/bin/env python3
import sys

ciudad_actual = None
total_ventas = 0

for linea in sys.stdin:
    linea = linea.strip()
    if not linea:
        continue

    try:
        ciudad, venta = linea.split("\t", 1)
        venta = int(venta)
    except ValueError:
        continue

    if ciudad_actual == ciudad:
        total_ventas += venta
    else:
        if ciudad_actual is not None:
            print(f"{ciudad_actual}\t{total_ventas}")
        ciudad_actual = ciudad
        total_ventas = venta

if ciudad_actual is not None:
    print(f"{ciudad_actual}\t{total_ventas}")
