def formatText(text, left, top, areaWidth, areaHeight):
    inicio = 0
    fin = areaWidth

    while fin <= len(texto):
        while not any(signo in text[fin] for signo in listaDeSignos):
            fin -= 1
        fin += 1

        message = letra.render(texto[inicio:fin], True, BLACK)
        messageRect = message.get_rect()
        messageRect.topleft = (left, top)
        DISPLAYSURF.blit(message, messageRect)
        inicio = fin
        fin += areaWidth
        top += 20

    fin -= areaWidth
    message = letra.render(texto[inicio:fin], True, BLACK)
    messageRect = message.get_rect()
    messageRect.topleft = (left, top)
    DISPLAYSURF.blit(message, messageRect)
