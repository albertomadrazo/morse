# --coding: utf-8--
# TODO:
# Resolver handleClicks, tal vez romper la función en varias.
# cada botón debe ser independiente y dibujarse independientemente. No hacer un
# set de botones, sino hacerlos todos separados, para poner y quitar los botones
# a mi conveniencia. Eso supongo que sería un diseño más ortogonal.

# que imprima multiples líneas. Tal vez hacer un scroll(creo que esta aplicación
# hubiera sido más sencilla con el Tkinter, pero he aprendido mucho así.)


import pygame, sys, time, string
from pygame.locals import *
from glovars import *
from textClasses import *
from tabClasses import *

pygame.init()
tab = Tab()
wr_text = Text()
all_tabs = Tab()
wr_tab = WriteTab() # a new instance of WriteTab class
wr_instruct = InstructTab()
tb_tab = TablaTab()
###################                main()             ##########################
def main():
    #tab.MODALIDAD = 'latin'
    letterValue = 97
    numberValue = 48
    keyboardVals = {}
    for c in string.lowercase:
        keyboardVals[c] = letterValue
        letterValue += 1

    for c in range(10):
        keyboardVals[c] = numberValue
        numberValue += 1

    keyboardVals[' '] = 32
    keyboardKeys = {k: v for v, k in keyboardVals.iteritems()}

    whichButtonPressed = -1 # button pressed in the 'escribe' tab
    DISPLAYSURF.fill(BGCOLOR)
    mousex, mousey = None, None
    tab_medidas = drawAllTabs()

    currentTab = 'escribe'
    drawChosenTab(whichButtonPressed, currentTab) # here we draw our initial status

    global tabs
    tabs = { 'instrucciones': tab_medidas[0],
             'practica':      tab_medidas[1],
             'tabla':         tab_medidas[2],
             'escribe':       tab_medidas[3],
             'historia':      tab_medidas[4],
           }

    pressTime = 0
    idle_clack = 0
    stringMorse = ''
    stringLatin = '' #global
    #MODALIDAD #MODALIDAD = 'morse' # En qué estamos. De morse a latin o de
    #latin a morse. # on click button switch between morse and latin while
    while True: # main game loop
        if idle_clack > 0 and tab.MODALIDAD == 'morse':
            if (time.time()) - idle_clack >= 1:
                stringMorse += '|'
                traduce(stringMorse, tab.MODALIDAD)
                idle_clack = 0

        actionAreas = manageTabs(currentTab) #wr_tab.clickableAreas()

        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                exit_program()

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    pressTime = time.time()
                    idle_clack = 0

                if (event.key > 96 and event.key < 123 \
                                  or event.key > 47 and event.key < 58 \
                                  or event.key == 32 )\
                                  and tab.MODALIDAD == 'latin':
                    character = keyboardKeys[event.key]
                    stringLatin = writeLatin(stringLatin, character)
                    traduce(stringLatin, tab.MODALIDAD)

            elif event.type == KEYUP:

                if event.key == K_ESCAPE:
                    exit_program()

                if event.key == K_RIGHT and tab.MODALIDAD == 'morse':

                    releaseTime = time.time()
                    # idle_clack = 0 # tal vez esto esta sobrando.
                    if releaseTime - pressTime <= 0.20:
                        stringMorse = dot(stringMorse)
                    elif releaseTime - pressTime > 0.20 \
                         and releaseTime - pressTime <= 0.75:
                        stringMorse = line(stringMorse)

                    idle_clack = time.time()

                elif event.key == K_BACKSPACE and currentTab =='escribe':
                    if tab.MODALIDAD == 'morse':
                        stringMorse = erase(stringMorse)
                        write(stringMorse)
                        traduce(stringMorse, tab.MODALIDAD)
                        stringMorse += '|'
                    elif tab.MODALIDAD == 'latin':
                        stringLatin = eraseLatinLetters(stringLatin)
                        write(stringLatin)
                        traduce(stringLatin, tab.MODALIDAD)

            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                whichButtonPressed, currentTab = handleClicks(mousex, mousey,   actionAreas, currentTab, whichButtonPressed)

        FPSCLOCK.tick(FPS)
        pygame.display.update()
        #print "OOOOOOOO", currentTab
        #print "actionAreas = ", actionAreas
######################        END OF MAIN        ###############################

def manageTabs(currentTab):
    if currentTab == 'instrucciones':
        #print currentTab
        return
    elif currentTab == 'practica':
        #print currentTab
        return
    elif currentTab == 'tablas':
        #print currentTab
        return
    elif currentTab == 'escribe':
        #print "ja, ich bin chingon"
        return wr_tab.clickableAreas()
    elif currentTab == 'historia':
        #print currentTab
        return


def handleClicks(mousex, mousey, actionAreas, currentTab, whichButtonPressed):
    for key, val in tabs.iteritems(): # tabs is a global dictionary
        #print "-" * 20
        #print "actionAreas in handleClicks = ",actionAreas
        #print "key in handleClicks = ", key
        #print "val in handleClicks = ", val
        mouse_position = pygame.Rect(val)
        pygame.Rect(val)
        if mouse_position.collidepoint(mousex, mousey):
            currentTab = key
            key = drawChosenTab(whichButtonPressed, key)
            print "in handleClicks, key = ",key
            return -1, currentTab
    whichButtonPressed = 0
    for value in actionAreas: # where in the tab can I click.
        mouse_position = pygame.Rect(value)
        if mouse_position.collidepoint(mousex, mousey):
            manageClickableAreas(currentTab, whichButtonPressed)
            drawChosenTab(whichButtonPressed, currentTab) ### QUÉ MIERDA HACE UN DEFAULT AQUÍ???
            return whichButtonPressed, currentTab
        whichButtonPressed += 1
    return -1, currentTab

def manageClickableAreas(tab, whichButtonPressed):
    if tab == 'instrucciones':
        pass
    elif tab == 'practica':
        pass
    elif tab == 'tabla':
        pass
    elif tab == 'escribe':
        print "=========================hier ",wr_tab.drawButtons(whichButtonPressed)
        wr_tab.drawButtons(whichButtonPressed)
    elif tab == 'historia':
        pass


def drawAllTabs():
    tab_pos = 30
    tab_size = []
    # don't forget to use an assert here.
    tab_width = (WINDOWWIDTH - MARGIN_A * 2) / MENUS - TABGAP
    for i in range(MENUS):
        what_tab = (tab_pos, 60, tab_width, 20)
        pygame.draw.rect(DISPLAYSURF, TAB_OFF, what_tab)
        tab_pos += tab_width + TABGAP
        tab_size.append(what_tab)
        wr_text.textOnTab(secciones[i], tab_size[i], 'off')
    return tab_size


def drawChosenTab(whichButtonPressed, tab_choice):
    tab_size = drawAllTabs()
    pygame.draw.rect(DISPLAYSURF, TAB_ON, TABAREA)

    if tab_choice == 'instrucciones': # edit this so it's totally customizable
        pygame.draw.rect(DISPLAYSURF, TAB_ON, tab_size[0])
        wr_text.textOnTab('instrucciones', tab_size[0], 'on')
        wr_instruct.writeMsg()
        #currentTab = wr_instruct.clickableAreas()
        print "wr_tab.clickableAreas() ", wr_instruct.clickableAreas()

    if tab_choice == 'practica':
        pygame.draw.rect(DISPLAYSURF, TAB_ON, tab_size[1])
        wr_text.textOnTab('practica', tab_size[1], 'on')
        #currentTab = wr_practica.clickableAreas()
        #print "wr_tab.clickableAreas() ", wr_practica.clickableAreas()


    elif tab_choice == 'tabla':
        pygame.draw.rect(DISPLAYSURF, TAB_ON, tab_size[2])
        wr_text.textOnTab('tabla', tab_size[2], 'on')
        tb_tab.writeTable(morse)
        #currentTab = tb_tab.clickableAreas()
        print "tb_tab.clickableAreas() ", tb_tab.clickableAreas()

    elif tab_choice == 'escribe':
        pygame.draw.rect(DISPLAYSURF, TAB_ON, tab_size[3])
        wr_text.textOnTab('escribe', tab_size[3], 'on')
        wr_tab.drawTextAreas()
        wr_tab.drawButtons(whichButtonPressed)
        #currentTab = wr_tab.clickableAreas()
        print "$$$$$$$$$$$  wr_tab.clickableAreas() ", wr_tab.clickableAreas()
        #print currentTab

    elif tab_choice == 'historia':
        pygame.draw.rect(DISPLAYSURF, TAB_ON, tab_size[4])
        wr_text.textOnTab('historia', tab_size[4], 'on')
        #currentTab = wr_instruct.clickableAreas()

    return tab_size


def exit_program():
    pygame.quit()
    sys.exit()


def line(stringMorse):
    stringMorse += '-'
    write(stringMorse)
    return stringMorse


def dot(stringMorse):
    stringMorse += '.'
    write(stringMorse)
    return stringMorse

def writeLatin(stringLatin, character):
    stringLatin += character
    write(stringLatin)
    return stringLatin

def write(cadena, translated=False):
    blanks = WriteTab() # create a temporary class for drawing the blanks

    if translated == False:
        x = 35
        y = 95
        text_size  = 25
        blanks.drawTextAreas('up')
    elif translated == True:
        x = 35
        y = 275
        text_size = 35
        blanks.drawTextAreas('down')
    cadena2 = ''

    for i in cadena:
        if i == ' ':
            print "Si lo hay"
        if i == '|':
            cadena2 += '&' # oder hier
        else:
            cadena2 += i

    font = pygame.font.Font('freesansbold.ttf', text_size)
    listaDeSignos = [' '] if (Tab.MODALIDAD == 'morse') else [' ', ',', '.']
    print "cadena2 = ", cadena2
    print "len(cadena2) = ", len(cadena2)
    print "listaDeSignos = ", listaDeSignos
    if len(cadena2) >= 40:
        wr_text.formatText2(cadena2, font, x, y, 40)
    else:
        texto = font.render(cadena2, True, BLACK)
        text_rect = texto.get_rect()
        text_rect.topleft = (x, y)
        DISPLAYSURF.blit(texto, text_rect)


def traduce(stringToTrans, MODALIDAD):          #, MODALIDAD='latin'):
    letrasTraducidas = ''
    if MODALIDAD == 'morse':
        formatString = stringToTrans.split('|')
        for letra in formatString:
            if letra in morse.values():
                letrasTraducidas += latin[letra]
            else:
                letrasTraducidas += '*'

        #write(letrasTraducidas, True)
    elif MODALIDAD == 'latin':
        for letra in stringToTrans:
            if letra in latin.values():
                letrasTraducidas += ' '
                letrasTraducidas += morse[letra]
            else:
                print "No hay esa letra"

    write(letrasTraducidas, True)



def erase(stringToErase):
    a = 1 # count the iterations to cut when necessary
    if stringToErase == '':
        return stringToErase

    if stringToErase[0] != '|':
        stringToErase = '|' + stringToErase

    if stringToErase[-1] == '|' and len(stringToErase) > 1:
        stringToErase = stringToErase[:-1]

    for i in reversed(stringToErase):
        if len(stringToErase) == 0:
            break

        if i == '|':
            stringToErase = stringToErase[:-a]
            break
        a += 1

    return stringToErase


def eraseLatinLetters(stringToErase):
    print stringToErase
    stringToErase = stringToErase[:-1]

    return stringToErase

if __name__ == '__main__':
    main()
