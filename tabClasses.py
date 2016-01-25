#--coding: utf-8--
import pygame
from glovars import *
from collections import OrderedDict

class Tab(object):
    MODALIDAD = 'morse'
    # Necesito unas variables que tengan las medidas de cada elemento de
    # cada pestaña.
    def __init__(self):
        tabWidth = 550
        #self.MODALIDAD = 'morse'

    def clickableAreas(self):
        return self.btnlist

    def buttonPushed(self, key):
        pass


# This function manages the text in the program
class WriteTab(Tab):
    def __init__(self):
        Tab.__init__(self)
        self.clack_button = (514, 94, 95, 95)
        self.enter_button = (514, 210, 50, 30)
        self.delete_button = (569, 210, 40, 30)
        self.btnlist = \
                     [self.clack_button, self.enter_button, self.delete_button]

    def drawTextAreas(self, which='both'): # draws a white space for putting
                                            # text when textEditor tab is on
        x_a = 30
        x_b = 30
        y_a = 90
        y_b = 270
        width = 470
        height = 175
        if which == 'up':
            self.drawUpperTextArea()
        elif which == 'down':
            self.drawLowerTextArea()
        elif which == 'both':
            self.drawUpperTextArea()
            self.drawLowerTextArea()


    def drawUpperTextArea(self):
        x_a = 30
        x_b = 30
        y_a = 90
        y_b = 270
        width = 470
        height = 175
        pygame.draw.rect(DISPLAYSURF, TAB_OFF,
                        (x_a-1, y_a-1, width+1, height+1), 2)
        pygame.draw.rect(DISPLAYSURF, WHITE,
                        (x_a, y_a, width, height))


    def drawLowerTextArea(self):
        x_a = 30
        x_b = 30
        y_a = 90
        y_b = 270
        width = 470
        height = 175
        pygame.draw.rect(DISPLAYSURF, TAB_OFF,
                        (x_b-1, y_b-1, width+1, height+1), 2)
        pygame.draw.rect(DISPLAYSURF, WHITE,
                        (x_b, y_b, width, height))


    def enterClicked(self):
        #print "%%%%%%%%%%%%%%%%%%%%in enterClicked"
        pass

    def clackClicked(self):

        print "in clackClicked, MODALIDAD = ",Tab.MODALIDAD
        if Tab.MODALIDAD == 'morse':
            print "jaajaja"
            Tab.MODALIDAD = 'latin'
        elif Tab.MODALIDAD == 'latin':
            print "jojojo"
            Tab.MODALIDAD = 'morse'


    def eraseClicked(self):
        #print "%%%%%%%%%%%%%%%%%%%%%in eraseClicked"
        pass

    def buttonPushed(self, button_number):       #, MODALIDAD='latin'):
        if button_number == 0:
            self.clackClicked()
        elif button_number == 1:
            self.enterClicked()
        elif button_number == 2:
            self.eraseClicked()


    def drawButtons(self, pressed=-1):
        border = 2
        j = 0
        for i in self.btnlist:
            pygame.draw.rect(DISPLAYSURF, DARKINDIAN, (i[0] - border,
            i[1] - border, i[2] + border * 2,
            i[3] + border * 2))
            if pressed == j:
                self.buttonPushed(j)
                pygame.draw.rect(DISPLAYSURF, BUTTONPRESSED, (i[0],
                i[1], i[2], i[3]))
            else:
                pygame.draw.rect(DISPLAYSURF, BUTTONS, (i[0],
                i[1], i[2], i[3]))
            j += 1




    # This function will save the texts the user make. I'll try to use
    # code from the hacker's book about recognizing the user by his uid
    def saveFile(self, user=None):
        pass

class TablaTab(Tab):
    def __init__(self):
        self.btnlist = ""

    def drawSurface(self):
        pass

    def writeTable(self, morse):
        left = 80
        top =  100
        flag = False
        font = pygame.font.Font('freesansbold.ttf', 20)
        numbers = []
        letters = []
        sort = OrderedDict(sorted(morse.items()))
        for b, c in sort.items():
            try:
                int(b)
                numbers.append([b, c])
            except:
                letters.append([b, c])
        letters.extend(numbers)
        letters.remove([' ', ''])
        for k, v in letters:

            if top >= 400:
                top = 100
                left += 120
                flag = True

            if flag == True and k.isdigit():
                top = 100
                #left += 120
                flag = False

            char = font.render("%s    %s" % (k, v), True, BLACK)
            char_rect = char.get_rect()
            char_rect.topleft = (left, top)
            DISPLAYSURF.blit(char, char_rect)
            #print "left", left
            #print "top", top
            top += 24

class InstructTab(Tab):
    def __init__(self):
        self.instrucciones = ''' Oprime la flecha derecha para escribir en clave morse. Si lo presionas rapido, resultara en punto, presionas durante mas tiempo, resultara linea. Para aprender a escribir las letras en clave morse, checa la pestana de "tablas" y forma frases. Para  borrar, oprime la tecla "delete". Esto borrara todos los fragmentos de la letra. Repite hasta que termines tu mensaje. Presiona el boton grande para cambiar de morse a alfabeto o de alfabeto a morse.'''
        self.btnlist = ""

    def writeMsg(self):
        texto = self.instrucciones # syntactic sugar
        left = 60
        top = 90
        letra = pygame.font.Font('freesansbold.ttf', 15)
        print "len instrucciones = ", len(texto)
        inicio = 0
        fin = 75

        while fin <= len(texto):
            print "len(instrucciones) = ", len(texto)
            print "fin = ", fin

            while not any(signo in texto[fin] for signo in['.', ',', ' ']):
                fin -= 1
            fin += 1

            mes = letra.render(texto[inicio:fin], True, BLACK)
            mes_rect = mes.get_rect()
            mes_rect.topleft = (left, top)
            DISPLAYSURF.blit(mes, mes_rect)
            inicio = fin
            fin += 75
            top += 20

        # rebobinamos para imprimir el último trozo te texto.
        fin -= 75
        mes = letra.render(texto[fin:], True, BLACK)
        mes_rect = mes.get_rect()
        mes_rect.topleft = (left, top)
        DISPLAYSURF.blit(mes, mes_rect)

class Button(WriteTab):
    def __init__(self, ):
        pass
