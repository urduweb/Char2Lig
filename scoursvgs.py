#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
from optparse import OptionParser

descr = "Script to simplify a directory of SVGs using Inkscape's SCOUR"
usage = "%prog -i [inputdir] -o [outputdir]"

parser = OptionParser(usage=usage, description=descr)
parser.add_option("-i", "--input",
		action="store", type="string", dest="dir_in",
		help="Directory containing source SVGs", metavar="DIR_IN")
parser.add_option("-o", "--output",
		action="store", type="string", dest="dir_out",
		help="Directory containing output SVGs", metavar="DIR_OUT")
(options, args) = parser.parse_args()

if (not options.dir_in) and (not options.dir_out):
	parser.error("Missing parameters")

SVG_DIR_IN = options.dir_in
SVG_DIR_OUT = options.dir_out

try:
	os.mkdir(SVG_DIR_OUT)
except:
	pass

logFile = open("log-scouring.txt","w")

count = 0
for filename in os.listdir(SVG_DIR_IN):
	(fname, ext) = os.path.splitext(filename)
	if ext=='.svg':
		file_in_path = os.path.join(SVG_DIR_IN,filename)
		file_out_path = os.path.join(SVG_DIR_OUT,filename)
		# Skip if file already exists
		if not os.path.isfile(file_out_path):
			count = count+1
			print "Scouring glyph number", count, fname
			r = subprocess.check_output(["python","/usr/share/inkscape/extensions/scour.py","-i",file_in_path,"-o",file_out_path])
			print r
		else:
			print "Skipping", filename
	logFile.write("Skipped {0}\n".format(filename))

logFile.close()
