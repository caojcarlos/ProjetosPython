#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 07:12:03 2020

@author: Jose Carlos Nunes

Objetivo: Programa Basico para jogo de Adivinhacao
"""
import random
import os

sorteado = random.randrange(1,100)

print(sorteado)

jogador = int(input('Digite um numero entre [1, 100]: '))

erro = 0

while (jogador != sorteado):
    if (jogador < sorteado):
        print('O numero é maior')
    elif (jogador > sorteado):
        print('O numero e menor')
    else:
        break
    erro += 1
    jogador = int(input('Tente novamente, digite um numero entre [1, 100]: '))    

print ('Parabens voce acertou em {}'. format(str(erro + 1)))
    