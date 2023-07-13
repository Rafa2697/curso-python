#faça um porgrama um python que abra e reproduza o audio de um arquivo em mp3.

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()