#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
parser.add_option("-l", "--log",
		action="store", type="string", dest="logfile",
		help="Log file", metavar="LOG_FILE", default="log.txt")
parser.add_option("-t", "--type",
		action="store", type="string", dest="outformat",
		help="File type of generated font. e.g., sfd or ttf", metavar="OUT_FORMAT", default="sfd")

(options, args) = parser.parse_args()

if not options.glyphdir:
	raise ValueError("No glyph directory specified")
if not options.font_out:
	raise ValueError("No output font name specified")

def createGlyph(font,glyphname, glyphformat):
	font.createChar(-1, glyphname)
	svgPath= os.path.join(options.glyphdir, glyphname+glyphformat)
	if os.path.isfile(svgPath):
		font[glyphname].importOutlines(svgPath)
	else:
		print svgPath, "is not a valid path.\n"

def AddGlyphs(font):
	logFile= open(options.logfile,"w")
	for f in os.listdir(options.glyphdir):
		(baseName, extName)=os.path.splitext(f)	
		print "Creating glyph", baseName
		logFile.write("Creating glyph "+baseName+"\n")
		createGlyph(font, baseName, extName)
	logFile.close()

def createFont(strFontName):
	if options.font_in:
		tt=fontforge.open(options.font_in)
	else:
		tt=fontforge.font(options.font_out)
	AddGlyphs(tt)
	tt.generate(strFontName)

createFont(options.font_out+'.'+options.outformat)
