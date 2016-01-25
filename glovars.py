# --coding: utf-8--
import pygame

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
BLUE  = (  0,   0, 255)
DEEPBLUE = (44, 27, 174)
DEEPERBLUE = (22, 18, 58)
ORANGE= (255, 140,   0)
PRESSORANGE = (205, 90, 0)
LIGHTBLUE = (173, 216, 230)
INDIANRED = (205, 92, 92)
DARKINDIAN = (110, 50, 50)
DARKGREEN = (28, 71, 21)
GRAYGREEN = (128, 172, 121)
GRAY = (64, 64, 64)
BACKGROUNDGRAY = (104, 103, 111)
DEEPGREEN = (15, 52, 15)
BGCOLOR = BACKGROUNDGRAY
TAB_ON = GRAYGREEN
TAB_OFF = DEEPGREEN
BUTTONS = DEEPBLUE
BUTTONPRESSED = DEEPERBLUE

MENUS = 5 # The number of tabs

morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
          'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
          'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
          'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
          'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
          'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
          '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
          '0': '-----', ' ': '',
        }

latin = {k: v for v, k in morse.iteritems()} # creates and inverse dictionary.

#MODALIDAD = 'morse'

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
MARGIN_A = 20
MARGIN_B = 10
MARGIN_C = 5
morsechar = 25
line_height = 25
TEXTWIDTH = 300
TEXTHEIGHT = 300
TABGAP = 10
TABAREA = (MARGIN_A, 80, 600, 380) # la zona principal de trabajo

FPS = 30
FPSCLOCK = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Yo soy la Morse")

#currentTab = 'escribe'
# que_letra = 0 # en que letra va el codigo morse
secciones = ['instrucciones', 'practica', 'tablas', 'escribe', 'historia']
#global MODALIDAD
