# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pXBSVbUGHE1NU-Re54KNj2dv913deEn8
"""

# string a ser invertida
string = "exemplo"

# variável para armazenar a string invertida
inversao = ""

# percorre a string de trás para frente e concatena cada caractere na nova string
for i in range(len(string)-1, -1, -1):
    inversao += string[i]

# exibe a string invertida
print(inversao)

# Define o número para ser verificado
numero_verificado = 13

# Inicializa a sequência com os dois primeiros valores
sequencia = [0, 1]

# Calcula os próximos valores até chegar no número verificado ou ultrapassá-lo
while sequencia[-1] < numero_verificado:
    proximo_valor = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo_valor)

# Verifica se o número verificado está na sequência
if numero_verificado in sequencia:
    print(f'O número {numero_verificado} PERTENCE à sequência de Fibonacci!')
else:
    print(f'O número {numero_verificado} NÃO PERTENCE à sequência de Fibonacci.')