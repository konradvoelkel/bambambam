#!/usr/bin/python3
#
# Bam Bam Bam (c) 2013-2015 Konrad Voelkel
#
#    http://www.konradvoelkel.com
#    forked from Bam Bam version 0.4
#     (c) 2007-2008 Don Brown
#     (c) 2010 Spike Burch <spikeb@gmail.com>
#    licensed under GPL3 or later
#    some pictures taken from Tango Project
#    some audio taken from pdsounds.org
#    all sounds and images are licensed as public domain.
#
#TODO write a README on installing this and the goals
# * main goal for now: teach toddlers human-computer-interaction in a fun way
# * to run this on python3, it may be easiest to fetch pygame from source
# * but it should run on python2 (>=2.7) just as well.

import sys
import os
import os.path
import itertools
from random import choice, randint
import string
import pygame
from pygame.locals import * 

PROG_DIR = "/usr/share/bambam/data"
USER_DIR = os.path.expanduser("~/.bambambam")
PROBABILITY_CLEARSCREEN = 10 # in %

with open(os.path.join(PROG_DIR,"colors.txt")) as f:
    COLORS = eval("[" + f.read() + "]")

class NoneSound:
    def play(self):
        pass

getAbsolutePath = lambda name : os.path.join(PROG_DIR, 'data', name)
is_alpha = lambda key : key < 255 and (str.isalnum(chr(key)))
getFileNamesFromFolder = lambda path, extension : sum([[os.path.join(root,file) for file in files if file[-(1+len(extension)):].upper()=="."+extension.upper()] for (root, dirs, files) in os.walk(path, followlinks=True)],[])

class BamBamBam():

    # Load image from path
    @classmethod
    def load_image(cls, path):
        try:
            image = pygame.image.load(path)
        except pygame.error as message:
            raise SystemExit(message)
        image = image.convert_alpha()
        return image

    # Load sound file from path
    @classmethod
    def load_sound(cls, path):
        if not pygame.mixer:
            return NoneSound()
        try:
            sound = pygame.mixer.Sound(path)
        except pygame.error as message:
            raise SystemExit(message)
        return sound

    # Processes events
    def inputEvents(self, events):
        for event in events: 
            if event.type == QUIT: 
                sys.exit(0)
            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                if(not "clearnever" in self.history):
                    if randint(0, 100) < PROBABILITY_CLEARSCREEN:
                        self.clearScreen()
                if(not "nosound" in self.history):
                    self.play_sound()
                if event.type == MOUSEBUTTONDOWN or not(is_alpha(event.key)):
                    if(not "nopic" in self.history):
                        self.print_image()
                else:
                    self.history += chr(event.key)
                    if(not "noletter" in self.history):
                        self.print_letter(event.key)
                if("showhist" in self.history):
                    self.clearScreen()
                    self.print_string(self.history[-100:].encode("utf-8"))
                if("quit" in self.history):
                    sys.exit(0)
                if("killhist" in self.history):
                    self.history = ""
                if(self.history[-8:] == "clearnow"):
                    self.clearScreen()

    def play_sound(self):
        if(self.sounds):
            choice(self.sounds).play()

    # Prints an image at a random location
    def print_image(self):
        if(self.images):
            img = choice(self.images)
            imgSize = (img.get_width(), img.get_height())
            scaleFactor = randint(1,4)
            img = pygame.transform.scale(img, [imgSize[i] // scaleFactor for i in (0,1)])
            (w,h) = (randint(0, self.screenSize[i]-imgSize[i]) for i in (0,1))
            self.screen.blit(img, (w, h))
            pygame.display.flip()

    # Prints a letter at a random location
    def print_letter(self, key):
        font = pygame.font.Font(None, randint(32,512))
        text = font.render(chr(key).upper(), 1, choice(self.colors))
        textpos = text.get_rect()
        center = (textpos.width // 2, textpos.height // 2)
        (textpos.centerx, textpos.centery) = (randint(0+center[i], self.screenSize[i]-center[i])
                                              for i in (0,1))
        self.screen.blit(text, textpos)
        pygame.display.flip()

    # Prints a string
    def print_string(self, string):
        font = pygame.font.Font(None, 32)
        text = font.render(string, 1, choice(self.colors))
        textpos = text.get_rect()
        self.screen.blit(text, textpos)
        pygame.display.flip()

    def clearScreen(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def init(self):
        self.screenSize = (screenwidth, screenheight) = (800, 600) # changes later in code
        self.history = ""
        if not pygame.font: print('Warning, fonts disabled')
        if not pygame.mixer: print('Warning, sound disabled')
        pygame.init() 
        pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
        pygame.display.set_caption('Bam Bam Bam') 
        self.screen = pygame.display.get_surface() 
        self.screenSize = (self.screen.get_width(), self.screen.get_height()) 
        self.background = pygame.Surface(self.screen.get_size(), flags=SRCALPHA)
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        self.clearScreen()
        self.colors = COLORS
        self.sounds = [BamBamBam.load_sound(path)
                       for path in itertools.chain(getFileNamesFromFolder(PROG_DIR,"ogg"),
                                                   getFileNamesFromFolder(USER_DIR,"ogg"))]
        self.images = [BamBamBam.load_image(path)
                       for path in itertools.chain(getFileNamesFromFolder(PROG_DIR,"png"),
                                                   getFileNamesFromFolder(USER_DIR,"png"))]

    def main(self):
        self.init()
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            self.inputEvents(pygame.event.get())

if(__name__ == "__main__"):
    BamBamBam().main()
