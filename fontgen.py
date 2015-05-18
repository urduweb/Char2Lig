#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python script to import glyphs into a font file

import fontforge
import os.path

# obtain command line arguments for 
# 1: path of the folder containing svgs
# 2: input sfd file
# 3: output font name

def createGlyph(font,glyphname):
    font.createChar(-1, glyphname)
    svgPath= 'Nafees/'+glyphname+'.svg'
    if os.path.isfile(svgPath):
        font[glyphname].importOutlines(svgPath)
    else:
        print svgPath+" is not valid.\n"

def AddGlyphs(font):
    logFile= open("log.txt","w")
    for f in os.listdir('Nafees'):
        (baseName, extName)=os.path.splitext(f)    
        logFile.write("creating glyph "+baseName+"\n")
        createGlyph(font, baseName)
    logFile.close()

def createFont(strFontName):
    tt=fontforge.open("TestFont.sfd")
    AddGlyphs(tt)
    tt.generate(strFontName)

createFont('TestFont.ttf')
