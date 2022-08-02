#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:14:09 2022

@author: siina
"""

import random
def sana():
    f = open("hirsipuu/kotus_sanat.txt","r")
    r = [i[:-1] for i in f.readlines()]
    return random.choice(r)
sana = sana()
koitetut = ""
y = ["_" for i in sana]
p = 0

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
while "".join(y)!=sana and p < len(HANGMANPICS)-1:
    print("".join(y))
    koitetut+=input("Anna kirjain. aiemmin arvatut: "+koitetut)
    for i in range(len(sana)):
        if sana[i] in koitetut:
            y[i] = sana[i]
    if koitetut[-1] not in sana:
        p += 1
    print("".join(y))
    print(HANGMANPICS[p])
if p == len(HANGMANPICS)-1:
    print(HANGMANPICS[-1])
    print(sana)
