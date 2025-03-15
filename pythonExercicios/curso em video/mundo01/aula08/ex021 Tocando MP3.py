print('\n'
      '\n'
      '==================================================\n'
      'Faça um pragra em Python que abra e reproduza o\n'
      'áudio de um arquivo MP3.\n'
      '==================================================\n'
      '')
######################################################################
######################################################################
import pygame
pygame.init()
pygame.mixer.music.load('Bad End Friends - Okabe.mp3')
pygame.mixer.music.play()
input()