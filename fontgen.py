#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Python script to generate a font file using imported glyphs
# Font can be started from scratch or
# Glyphs can be imported into an already existing font file

import fontforge
import os.path
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-d", "--dir",
		action="store", type="string", dest="glyphdir",
		help="Directory containing glyphs to import", metavar="DIR")
parser.add_option("-i", "--in",
		action="store", type="string", dest="font_in",
		help="Input font file (optional)", metavar="FONT_IN")
parser.add_option("-o", "--out",
		action="store", type="string", dest="font_out",
		help="Output font name", metavar="FONT_OUT")

(options, args) = parser.parse_args()

if not options.glyphdir:
	raise ValueError("No glyph directory specified")
if not options.font_out:
	raise ValueError("No output font name specified")

def createGlyph(font,glyphname):
	font.createChar(-1, glyphname)
	svgPath= options.glyphdir+'/'+glyphname+'.svg'
	if os.path.isfile(svgPath):
		font[glyphname].importOutlines(svgPath)
	else:
		print svgPath+" is not a valid path.\n"

def AddGlyphs(font):
	logFile= open("log.txt","w")
	for f in os.listdir(options.glyphdir):
		(baseName, extName)=os.path.splitext(f)	
		logFile.write("Creating glyph "+baseName+"\n")
		createGlyph(font, baseName)
	logFile.close()

def createFont(strFontName):
	if options.font_in:
		tt=fontforge.open(options.font_in)
	else:
		tt=fontforge.font(options.font_out)
	AddGlyphs(tt)
	tt.generate(strFontName)

createFont(options.font_out+'.ttf')
