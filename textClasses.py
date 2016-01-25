#--coding: utf-8--
# “It is a good rule after reading a new book, never to allow yourself
# another new one till you have read an old one in between.”
import pygame
from glovars import *
from tabClasses import *

class Text(object):
    def __init__(self):
        self.parte = ''
        self.letra = [[]]
        self.palabra = ['']
        self.enunciado = ['']
        self.texto = ['']
        self.traducido = ''
        self.cadena_trad = ''
        self.cadena_morse = ''
        self.cadena_latin = ''

    def write(self, cadena, character='', translated=False):
        blanks = WriteTab() # create a temporary class for drawing the blanks

        if translated == False:
            x = 35
            y = 95
            text_size  = 25
            blanks.drawTextEdit('up')
        elif translated == True:
            x = 35
            y = 275
            text_size = 35
            blanks.drawTextEdit('down')

        cadena += character
        font = pygame.font.Font('freesansbold.ttf', text_size)
        texto = font.render(cadena, True, BLACK)
        text_rect = texto.get_rect()
        text_rect.topleft = (x, y)
        DISPLAYSURF.blit(texto, text_rect)

        return cadena


    def erase(self, text, cadena, translated=False):
        # En esta clase tengo que apretar el boton de borrar.

        pass

    def translate(self, text):
        traducido = ''
        for letra in text:
            if letra in morse.values():
                traducido += latin[letra]
            else:
                traducido += '*'
        return traducido


    def textOnTab(self, text, position, status='off'):
        if status == 'on':
            status = BLACK
        else:
            status = GRAY

        font = pygame.font.Font('freesansbold.ttf', 15)
        message = font.render(text, True, status)
        mess_rect = message.get_rect()
        mess_rect.topleft = (position[0] + 5, position[1])
        DISPLAYSURF.blit(message, mess_rect)

    def formatText2(self, text, letra, left, top, charsInLine):
        inicio = 0
        fin = charsInLine

        while True:
            if inicio > len(text):
                break

            message = letra.render(text[inicio:fin], True, BLACK)
            messageRect = message.get_rect()
            messageRect.topleft = (left, top)
            DISPLAYSURF.blit(message, messageRect)
            inicio = fin
            fin += charsInLine
            top += 20

        fin -= charsInLine
        message = letra.render(text[inicio:fin], True, BLACK)
        messageRect = message.get_rect()
        messageRect.topleft = (left, top)
        DISPLAYSURF.blit(message, messageRect)


    def formatText(self, \
                text, listaDeSignos, letra, left, top, charsInLine, areaHeight):

        inicio = 0
        fin = charsInLine
        print "aqui"
        while True:
            if inicio > len(text):
                break
            print "YES"
            while not any(signo in text[fin] for signo in listaDeSignos):
                fin -= 1
            fin += 1

            message = letra.render(text[inicio:fin], True, BLACK)
            messageRect = message.get_rect()
            messageRect.topleft = (left, top)
            DISPLAYSURF.blit(message, messageRect)
            inicio = fin
            fin += charsInLine
            top += 20

        fin -= areaWidth
        message = letra.render(text[inicio:fin], True, BLACK)
        messageRect = message.get_rect()
        messageRect.topleft = (left, top)
        DISPLAYSURF.blit(message, messageRect)
        print "saliendo"

