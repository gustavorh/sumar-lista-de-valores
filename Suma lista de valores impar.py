# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:41:25 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""
# Este script sumará los valores de la lista con índice impar y entregará la suma en pantalla.

lista = [2, 4, 6, 8, 10, 12, 14]
suma = 0
for x in range(len(lista)):
    if x % 2 == 0:
        suma += lista[x]

print(f"La suma de los elementos impares (indices) de la lista es: {suma}")
