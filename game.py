#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:14:09 2022

@author: siina
"""

import random
def sana(x="kotus_sanat.txt"):
    f = open("hirsipuu/"+x,"r")
    r = [i[:-1] for i in f.readlines()]
    return random.choice(r)


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
#sana = sana()
koitetut = ""

p = 0
if int(input("Oletus:0, Oma sanasto:1 : ")):
    sana=sana(input("Anna tiedoston nimi: "))
else:
    sana=sana()
y = ["_" for i in sana]
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
