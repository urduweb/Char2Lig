#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fontforge
import os.path
from optparse import OptionParser

descr = "Python script to generate a font file by importing glyphs"
usage = "%prog -d <glyphsdir> -o <fontname> [options]"

parser = OptionParser(usage=usage, description=descr)
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
parser.add_option("--emsize",
		action="store", type="int", dest="emsize",
		help="em size of the font (default=1000)", metavar="EMSIZE", default=1000)
(options, args) = parser.parse_args()

if not options.glyphdir:
	parser.error("No glyph directory specified")
if not options.font_out:
	parser.error("No output font name specified")

def createGlyph(font,glyphname, glyphformat):
	font.createChar(-1, glyphname)
	svgPath= os.path.join(options.glyphdir, glyphname+glyphformat)
	if os.path.isfile(svgPath):
		font[glyphname].importOutlines(svgPath)
	else:
		print svgPath, "is not a valid path.\n"

def AddGlyphs(font, logfile):
	for f in os.listdir(options.glyphdir):
		(baseName, extName)=os.path.splitext(f)	
		print "Creating glyph", baseName
		logfile.write("Creating glyph {0}\n".format(baseName))
		createGlyph(font, baseName, extName)
	print "Finished adding glyphs"

def createFont(strFontName):
	logFile= open(options.logfile,"w")
	if options.font_in:
		tt=fontforge.open(options.font_in)
	else:
		tt=fontforge.font(options.font_out)
	print "Adding Glyphs"
	AddGlyphs(tt, logFile)
	print "Setting font em size from", tt.em, "to", options.emsize
	tt.em = options.emsize
	logFile.write("Font em size set to {0}\n".format(tt.em))
	print "Generating font"
	tt.generate(strFontName)
	print "Done"
	logFile.close()

createFont(options.font_out+'.'+options.outformat)
