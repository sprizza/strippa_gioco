#!usr/bin/python
# -*- coding: utf-8 -*-

import pygame, random

nero = (0, 0, 0)
rosso = (255, 0, 0)
bianco = (255, 255, 255)
verde = (0, 225, 0)
blu = (18, 10, 153)
giallo = (255, 216, 0)
pygame.init()
infoObject = pygame.display.Info()
schermo = pygame.display.set_mode((infoObject.current_w - 70, infoObject.current_h - 80))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
pygame.display.set_caption('Preso')
sfondo = pygame.image.load('sfondo4.jpg')
sfondo1 = pygame.image.load('intro.jpg')
m_gioco = pygame.mixer.Sound('inizio.wav')
preso = pygame.mixer.Sound('cattura1.wav')
morte = pygame.mixer.Sound('morte6.wav')
clock = pygame.time.Clock()
giocatore = pygame.image.load('nero1.png').convert_alpha()
giocatore.set_colorkey()
giocatore_mask = pygame.mask.from_surface(giocatore)
giocatore_Pixel = giocatore.get_rect()
giocatore_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
nemico = pygame.image.load('simpatica.png').convert_alpha()
nemico.set_colorkey()
nemico_mask = pygame.mask.from_surface(nemico)
nemico_Pixel = nemico.get_rect()
nemico_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s = pygame.image.load('simpatica1.png').convert_alpha()
s.set_colorkey()
s_mask = pygame.mask.from_surface(s)
s_Pixel = s.get_rect()
s_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s1 = pygame.image.load('simpatica2.png').convert_alpha()
s1.set_colorkey()
s1_mask = pygame.mask.from_surface(s1)
s1_Pixel = s1.get_rect()
s1_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s2 = pygame.image.load('simpatica3.png').convert_alpha()
s2.set_colorkey()
s2_mask = pygame.mask.from_surface(s2)
s2_Pixel = s2.get_rect()
s2_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s3 = pygame.image.load('simpatica4.png').convert_alpha()
s3.set_colorkey()
s3_mask = pygame.mask.from_surface(s3)
s3_Pixel = s3.get_rect()
s3_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s4 = pygame.image.load('simpatica5.png').convert_alpha()
s4.set_colorkey()
s4_mask = pygame.mask.from_surface(s4)
s4_Pixel = s4.get_rect()
s4_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s5 = pygame.image.load('simpatica6.png').convert_alpha()
s5.set_colorkey()
s5_mask = pygame.mask.from_surface(s5)
s5_Pixel = s5.get_rect()
s5_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s6 = pygame.image.load('simpatica7.png').convert_alpha()
s6.set_colorkey()
s6_mask = pygame.mask.from_surface(s6)
s6_Pixel = s6.get_rect()
s6_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s7 = pygame.image.load('simpatica8.png').convert_alpha()
s7.set_colorkey()
s7_mask = pygame.mask.from_surface(s7)
s7_Pixel = s7.get_rect()
s7_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s8 = pygame.image.load('simpatica9.png').convert_alpha()
s8.set_colorkey()
s8_mask = pygame.mask.from_surface(s8)
s8_Pixel = s8.get_rect()
s8_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s9 = pygame.image.load('simpatica10.png').convert_alpha()
s9.set_colorkey()
s9_mask = pygame.mask.from_surface(s9)
s9_Pixel = s9.get_rect()
s9_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s10 = pygame.image.load('simpatica11.png').convert_alpha()
s10.set_colorkey()
s10_mask = pygame.mask.from_surface(s10)
s10_Pixel = s10.get_rect()
s10_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s11 = pygame.image.load('simpatica12.png').convert_alpha()
s11.set_colorkey()
s11_mask = pygame.mask.from_surface(s11)
s11_Pixel = s11.get_rect()
s11_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s12 = pygame.image.load('simpatica13.png').convert_alpha()
s12.set_colorkey()
s12_mask = pygame.mask.from_surface(s12)
s12_Pixel = s12.get_rect()
s12_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s13 = pygame.image.load('simpatica14.png').convert_alpha()
s13.set_colorkey()
s13_mask = pygame.mask.from_surface(s13)
s13_Pixel = s13.get_rect()
s13_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s14 = pygame.image.load('simpatica15.png').convert_alpha()
s14.set_colorkey()
s14_mask = pygame.mask.from_surface(s14)
s14_Pixel = s14.get_rect()
s14_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s15 = pygame.image.load('simpatica16.png').convert_alpha()
s15.set_colorkey()
s15_mask = pygame.mask.from_surface(s15)
s15_Pixel = s15.get_rect()
s15_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s16 = pygame.image.load('simpatica17.png').convert_alpha()
s16.set_colorkey()
s16_mask = pygame.mask.from_surface(s16)
s16_Pixel = s16.get_rect()
s16_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s17 = pygame.image.load('simpatica18.png').convert_alpha()
s17.set_colorkey()
s17_mask = pygame.mask.from_surface(s17)
s17_Pixel = s17.get_rect()
s17_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s18 = pygame.image.load('simpatica19.png').convert_alpha()
s18.set_colorkey()
s18_mask = pygame.mask.from_surface(s18)
s18_Pixel = s18.get_rect()
s18_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s19 = pygame.image.load('simpatica20.png').convert_alpha()
s19.set_colorkey()
s19_mask = pygame.mask.from_surface(s19)
s19_Pixel = s19.get_rect()
s19_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s20 = pygame.image.load('simpatica21.png').convert_alpha()
s20.set_colorkey()
s20_mask = pygame.mask.from_surface(s20)
s20_Pixel = s20.get_rect()
s20_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
s21 = pygame.image.load('simpatica22.png').convert_alpha()
s21.set_colorkey()
s21_mask = pygame.mask.from_surface(s21)
s21_Pixel = s21.get_rect()
s21_Pixel.center = (500, 500)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
piccoloFont = pygame.font.SysFont('comicsansms', 30)
medioFont = pygame.font.SysFont('comicsansms', 50)
grandeFont = pygame.font.SysFont('comicsansms', 80)
grandissimoFont = pygame.font.SysFont('comicsansms', 160)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
def Punteggio(listainizio, listainizio2):
    if listainizio - 1 <= 20:
        testo = grandeFont.render('Punteggio: %d' % (listainizio - 1), True, rosso)
        schermo.blit(testo, [infoObject.current_w / 2 - 150, 0])
    else:
        testo = grandeFont.render('Punteggio: %d' % (listainizio - 1), True, giallo)
        schermo.blit(testo, [infoObject.current_w / 2 - 150, 0])
    record_file = open("record_gioco.txt", "r")
    record = int(record_file.read())
    record_file.close()
    testo1 = medioFont.render('Record: %d' % record, True, blu)
    schermo.blit(testo1, [infoObject.current_w / 2 - 150, 55])
    testo2 = medioFont.render('Rubati %s' % (listainizio2 - 1), True, rosso)
    schermo.blit(testo2, [infoObject.current_w / 2 - 150, 90])
    if listainizio - 1 > record:
        record_file = open("record_gioco.txt", "w")
        record_file.write('\n' + str(listainizio - 1))
        record_file.close()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
def textObbiettivo(text, color, size):
    global textSurface, grandeFont
    if size == 'piccolo':
        textSurface = piccoloFont.render(text, True, color)
    elif size == 'medio':
        textSurface = medioFont.render(text, True, color)
    if size == 'grande':
        textSurface = grandeFont.render(text, True, color)
    return textSurface, textSurface.get_rect()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def messagioSchermo(msg, color, margine_y = 0, size = 'piccolo'):
    textSurface, textRectangle = textObbiettivo(msg, color, size)
    textRectangle.center = (infoObject.current_w / 2), (infoObject.current_h / 2) + margine_y
    schermo.blit(textSurface, textRectangle)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def inizioGioco():
    ini = True
    while ini:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    m_gioco.play(-1)
                    ini = False
                if event.key == pygame.K_u:
                    pygame.quit()
                    quit()
        schermo.blit(sfondo1, [0, 0])
        messagioSchermo('Hai 60 secondi di tempo.......', verde, - 100, 'grande')
        messagioSchermo('Ciao....non e come sembra', nero, - 30, 'medio')
        messagioSchermo('..attento ci sono faccine che regalano e altre che rubano .....', nero, 10, 'medio')
        messagioSchermo('...i tuoi punti....!!!', nero, 50, 'medio')
        messagioSchermo('PS: ricordati delle faccine che ti rubano i tuoi punti....', nero, 150, 'medio')
        messagioSchermo('Premi G per giocare, premi U per uscire', nero, 100, 'medio')
        messagioSchermo('Premi spazio per mettere in pausa', nero, 210)
        messagioSchermo('Premi spazio per uscire dalla pausa', nero, 230)
        pygame.display.update()
        clock.tick(120)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def inizio():
    global testa, image_name
    global direzione
    giocatore_Pixel.center = pygame.mouse.get_pos()
    listainizio = 1
    listainizio2 = 1
    conta, text = 60, '60'.rjust(2)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    gioco = False
    gameOver = False
    while not gioco:
        while gameOver:
            schermo.blit(sfondo1, [0, 0])
            m_gioco.stop()
            messagioSchermo('NOOO.....!!!!!', nero, - 80, 'grande')
            messagioSchermo('Premi R per ripetere', nero, 30, 'medio')
            messagioSchermo('Premi U per uscire', nero, 80, 'medio')
            messagioSchermo('In 60 secondi hai recuperato: ' + str(listainizio - 1)+' Smile', nero, -20, 'medio')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        gioco = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        m_gioco.play()
                        inizio()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gioco = True
            if event.type == pygame.USEREVENT:
                conta -= 1
                text = str(conta).rjust(2)
            if conta >= 0:
                gameOver = False
            else:
                m_gioco.stop()
                morte.play()
                gameOver = True
        else:
            if conta >= 5:
                testo3 = medioFont.render('Tempo ' + str(text), True, verde)
                schermo.blit(testo3, [infoObject.current_w / 2 - 150, 120])
            elif conta <= 5:
                testo3 = grandissimoFont.render('Tempo ' + str(text), True, rosso)
                schermo.blit(testo3, [infoObject.current_w / 2 - 250, infoObject.current_h / 2])
            elif conta <= 0:
                m_gioco.stop()
                morte.play()
                gameOver = True
                pygame.display.flip()
                clock.tick(120)
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        giocatore_Pixel.center = pygame.mouse.get_pos()
        pygame.display.update()
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        schermo.blit(sfondo, [0, 0])
        schermo.blit(giocatore, giocatore_Pixel.topleft)
        schermo.blit(nemico, nemico_Pixel.topleft)
        schermo.blit(s, s_Pixel.topleft)
        schermo.blit(s1, s1_Pixel.topleft)
        schermo.blit(s2, s2_Pixel.topleft)
        schermo.blit(s3, s3_Pixel.topleft)
        schermo.blit(s4, s4_Pixel.topleft)
        schermo.blit(s5, s5_Pixel.topleft)
        schermo.blit(s6, s6_Pixel.topleft)
        schermo.blit(s7, s7_Pixel.topleft)
        schermo.blit(s8, s8_Pixel.topleft)
        schermo.blit(s9, s9_Pixel.topleft)
        schermo.blit(s10, s10_Pixel.topleft)
        schermo.blit(s11, s11_Pixel.topleft)
        schermo.blit(s12, s12_Pixel.topleft)
        schermo.blit(s13, s13_Pixel.topleft)
        schermo.blit(s14, s14_Pixel.topleft)
        schermo.blit(s15, s15_Pixel.topleft)
        schermo.blit(s16, s16_Pixel.topleft)
        schermo.blit(s17, s17_Pixel.topleft)
        schermo.blit(s18, s18_Pixel.topleft)
        schermo.blit(s19, s19_Pixel.topleft)
        schermo.blit(s20, s20_Pixel.topleft)
        schermo.blit(s21, s21_Pixel.topleft)
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        distanza = 120
        Punteggio(listainizio, listainizio2)
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx, sy = int(nemico_Pixel.left - giocatore_Pixel.left), (nemico_Pixel.top - giocatore_Pixel.top)
        x = random.randrange(infoObject.current_w - distanza)
        y = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(nemico_mask, (sx, sy)):
            nemico_Pixel.center = (x, y)
            preso.play()
            listainizio += random.randrange(0, 2)
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx1, sy1 = int(s1_Pixel.left - giocatore_Pixel.left), (s1_Pixel.top - giocatore_Pixel.top)
        x1 = random.randrange(infoObject.current_w - distanza)
        y1 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s_mask, (sx1, sy1)):
            s1_Pixel.center = (x1, y1)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx2, sy2 = int(s2_Pixel.left - giocatore_Pixel.left), (s2_Pixel.top - giocatore_Pixel.top)
        x2 = random.randrange(infoObject.current_w - distanza)
        y2 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s_mask, (sx2, sy2)):
            s2_Pixel.center = (x2, y2)
            if listainizio >= 23:
                morte.play()
                listainizio2 -= 1
                listainizio -= 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx3, sy3 = int(s3_Pixel.left - giocatore_Pixel.left), (s3_Pixel.top - giocatore_Pixel.top)
        x3 = random.randrange(infoObject.current_w - distanza)
        y3 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s_mask, (sx3, sy3)):
            s3_Pixel.center = (x3, y3)
            morte.play()
            listainizio2 -= 1
            listainizio -= 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        sx4, sy4 = int(s4_Pixel.left - giocatore_Pixel.left), (s4_Pixel.top - giocatore_Pixel.top)
        x4 = random.randrange(infoObject.current_w - distanza)
        y4 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s_mask, (sx4, sy4)):
            s4_Pixel.center = (x4, y4)
            morte.play()
            listainizio2 -= 1
            listainizio -= 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        sx5, sy5 = int(s5_Pixel.left - giocatore_Pixel.left), (s5_Pixel.top - giocatore_Pixel.top)
        x5 = random.randrange(infoObject.current_w - distanza)
        y5 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s_mask, (sx5, sy5)):
            s5_Pixel.center = (x5, y5)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        sx6, sy6 = int(s6_Pixel.left - giocatore_Pixel.left), (s6_Pixel.top - giocatore_Pixel.top)
        x6 = random.randrange(infoObject.current_w - distanza)
        y6 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s6_mask, (sx6, sy6)):
            s6_Pixel.center = (x6, y6)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        sx7, sy7 = int(s7_Pixel.left - giocatore_Pixel.left), (s7_Pixel.top - giocatore_Pixel.top)
        x7 = random.randrange(infoObject.current_w - distanza)
        y7 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(nemico_mask, (sx7, sy7)):
            s7_Pixel.center = (x7, y7)
            morte.play()
            listainizio2 -= 1
            listainizio -= 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx8, sy8 = int(s8_Pixel.left - giocatore_Pixel.left), (s8_Pixel.top - giocatore_Pixel.top)
        x8 = random.randrange(infoObject.current_w - distanza)
        y8 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(nemico_mask, (sx8, sy8)):
            s8_Pixel.center = (x8, y8)
            if listainizio >= 23:
                preso.play()
                listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx9, sy9 = int(s9_Pixel.left - giocatore_Pixel.left), (s9_Pixel.top - giocatore_Pixel.top)
        x9 = random.randrange(infoObject.current_w - distanza)
        y9 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s9_mask, (sx9, sy9)):
            s9_Pixel.center = (x9, y9)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx10, sy10 = int(s10_Pixel.left - giocatore_Pixel.left), (s10_Pixel.top - giocatore_Pixel.top)
        x10 = random.randrange(infoObject.current_w - distanza)
        y10 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s10_mask, (sx10, sy10)):
            s10_Pixel.center = (x10, y10)
            morte.play()
            listainizio2 -= 1
            listainizio -= 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx11, sy11 = int(s11_Pixel.left - giocatore_Pixel.left), (s11_Pixel.top - giocatore_Pixel.top)
        x11 = random.randrange(infoObject.current_w - distanza)
        y11 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s11_mask, (sx11, sy11)):
            s11_Pixel.center = (x11, y11)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx12, sy12 = int(s12_Pixel.left - giocatore_Pixel.left), (s12_Pixel.top - giocatore_Pixel.top)
        x12 = random.randrange(infoObject.current_w - distanza)
        y12 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s12_mask, (sx12, sy12)):
            s12_Pixel.center = (x12, y12)
            morte.play()
            listainizio2 -= 1
            listainizio -= 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx13, sy13 = int(s13_Pixel.left - giocatore_Pixel.left), (s13_Pixel.top - giocatore_Pixel.top)
        x13 = random.randrange(infoObject.current_w - distanza)
        y13 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s13_mask, (sx13, sy13)):
            s13_Pixel.center = (x13, y13)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx14, sy14 = int(s14_Pixel.left - giocatore_Pixel.left), (s14_Pixel.top - giocatore_Pixel.top)
        x14 = random.randrange(infoObject.current_w - distanza)
        y14 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s14_mask, (sx14, sy14)):
            s14_Pixel.center = (x14, y14)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx15, sy15 = int(s15_Pixel.left - giocatore_Pixel.left), (s15_Pixel.top - giocatore_Pixel.top)
        x15 = random.randrange(infoObject.current_w - distanza)
        y15 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s15_mask, (sx15, sy15)):
            s15_Pixel.center = (x15, y15)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx16, sy16 = int(s16_Pixel.left - giocatore_Pixel.left), (s16_Pixel.top - giocatore_Pixel.top)
        x16 = random.randrange(infoObject.current_w - distanza)
        y16 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s16_mask, (sx16, sy16)):
            s16_Pixel.center = (x16, y16)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx17, sy17 = int(s17_Pixel.left - giocatore_Pixel.left), (s17_Pixel.top - giocatore_Pixel.top)
        x17 = random.randrange(infoObject.current_w - distanza)
        y17 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s17_mask, (sx17, sy17)):
            s17_Pixel.center = (x17, y17)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx18, sy18 = int(s18_Pixel.left - giocatore_Pixel.left), (s18_Pixel.top - giocatore_Pixel.top)
        x18 = random.randrange(infoObject.current_w - distanza)
        y18 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s18_mask, (sx18, sy18)):
            s18_Pixel.center = (x18, y18)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx19, sy19 = int(s19_Pixel.left - giocatore_Pixel.left), (s19_Pixel.top - giocatore_Pixel.top)
        x19 = random.randrange(infoObject.current_w - distanza)
        y19 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s19_mask, (sx19, sy19)):
            s19_Pixel.center = (x19, y19)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx20, sy20 = int(s20_Pixel.left - giocatore_Pixel.left), (s20_Pixel.top - giocatore_Pixel.top)
        x20 = random.randrange(infoObject.current_w - distanza)
        y20 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s20_mask, (sx20, sy20)):
            s20_Pixel.center = (x20, y20)
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx21, sy21 = int(s21_Pixel.left - giocatore_Pixel.left), (s21_Pixel.top - giocatore_Pixel.top)
        x21 = random.randrange(infoObject.current_w - distanza)
        y21 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s21_mask, (sx21, sy21)):
            s21_Pixel.center = (x21, y21)
            preso.play()
            listainizio += 1
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        sx22, sy22 = int(s_Pixel.left - giocatore_Pixel.left), (s_Pixel.top - giocatore_Pixel.top)
        x22 = random.randrange(infoObject.current_w - distanza)
        y22 = random.randrange(infoObject.current_h - distanza)
        if giocatore_mask.overlap(s_mask, (sx22, sy22)):
            s_Pixel.center = (x22, y22)
            preso.play()
            listainizio += 1
            if listainizio >= 200:
                morte.play()
                listainizio2 -= 10
                listainizio -= 10
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        pygame.display.update()
        clock.tick(120)


clock.tick(120)
inizioGioco()
inizio()
