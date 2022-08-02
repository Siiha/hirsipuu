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
    return r[random.randint(0, len(r))]
l = sana()
s = ""
y = ["_" for i in l]
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
while "".join(y)!=l and p < len(HANGMANPICS)-1:
    print("".join(y))
    s+=input("Anna kirjain. aiemmin arvatut: "+s)
    for i in range(len(l)):
        if l[i] in s:
            y[i] = l[i]
    if s[-1] not in l:
        p += 1
    print("".join(y))
    print(HANGMANPICS[p])
if p == len(HANGMANPICS)-1:
    print(HANGMANPICS[-1])
    print("".join(l))
