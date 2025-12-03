# Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('ex02.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#Pygame incompativel com a versão que utilizo do python 3.14