#!/bin/bash
# A simple Bash Shell Script to generate glyphs from a file of ligatures.
# It uses pango library to draw graphics.
# Author: Sawood Alam
# Organization: UrduWeb (urduweb.org/mehfil)
# Idea: Mohammad Saad
# Licence: GNU/GPL
# Initial Release: March 3rd, 2010

# USAGE:
# 
# 1: If default ligature file exists
# >> ./liggen.sh
# 
# 2: If custom ligature file is passed
# >> ./liggen.sh input/file/path
# 
# 3: If custom output format (extension) is desired
# >> ./liggen.sh input/file/path ext
# 
# 4: If custom output directory is desired
# >> ./liggen.sh input/file/path ext outpu/directory/path

# Config variables
FILE="ligatures.txt" # Default ligature file (one ligature per line text file)
FONT="Nafees" # Default font
EXT="svg" # Default output extension
OPDIR="$EXT/$FONT" # Default output directory
DPI=3000 # Default resolution

# Temporary variables
CNT=0 # Ligature counter
TEMP="" # Temporary ligature translitration

# Lookup array to translate roman equivalent name of the ligature file
declare -A LOOKUP

LOOKUP[أ]="P"
LOOKUP[إ]="M"
LOOKUP[آ]="A"
LOOKUP[ا]="a"
LOOKUP[ب]="b"
LOOKUP[پ]="p"
LOOKUP[ت]="t"
LOOKUP[ٹ]="T"
LOOKUP[ث]="C"
LOOKUP[ج]="j"
LOOKUP[چ]="c"
LOOKUP[ح]="H"
LOOKUP[خ]="K"
LOOKUP[د]="d"
LOOKUP[ڈ]="D"
LOOKUP[ذ]="Z"
LOOKUP[ر]="r"
LOOKUP[ڑ]="R"
LOOKUP[ز]="z"
LOOKUP[ژ]="X"
LOOKUP[س]="s"
LOOKUP[ش]="x"
LOOKUP[ص]="S"
LOOKUP[ض]="J"
LOOKUP[ط]="v"
LOOKUP[ظ]="V"
LOOKUP[ع]="e"
LOOKUP[غ]="G"
LOOKUP[ف]="f"
LOOKUP[ق]="q"
LOOKUP[ک]="k"
LOOKUP[گ]="g"
LOOKUP[ل]="l"
LOOKUP[م]="m"
LOOKUP[ن]="n"
LOOKUP[ں]="N"
LOOKUP[و]="w"
LOOKUP[ؤ]="W"
LOOKUP[ہ]="o"
LOOKUP[ۃ]="O"
LOOKUP[ۂ]="7"
LOOKUP[ھ]="h"
LOOKUP[ء]="I"
LOOKUP[ئ]="u"
LOOKUP[ی]="i"
LOOKUP[ي]="B"
LOOKUP[ے]="y"
LOOKUP[ـ]="Y"
LOOKUP[ ٰ]="1"
LOOKUP[ ٖ]="2"
LOOKUP[ ّ]="3"
LOOKUP[ ً]="4"
LOOKUP[ ٍ]="5"
LOOKUP[ َ]="6"
LOOKUP[ ِ]="8"
LOOKUP[ ُ]="9"
LOOKUP[ ٗ]="0"
LOOKUP[ٔ]="E"
LOOKUP[ٓ]="F"
LOOKUP[ ْ]="Q"
LOOKUP[٘]="U"

# Process starting timestamp
START=$(date +%s)

# Dynamic ligature translitration for output file naming
transliterate(){
  lig=$1
  TEMP=""
  for i in $(seq 0 $((${#lig} - 1))); do
    if [ ${LOOKUP[${lig:$i:1}]} != "" ]
    then
      T="${LOOKUP[${lig:$i:1}]}"
    else
      echo "Character ${lig:$i:1} is missing in lookup!"
      T="-"
    fi
    TEMP=$TEMP$T
  done
  return 1
}

# All the magic of generating graphics happens here
printLigature(){
  lig=$1
  CNT=`expr $CNT + 1`
  echo "> $CNT : processing $lig"
  transliterate $lig
  pango-view --text="$lig" --font="$FONT" --dpi=$DPI --language=ur --rtl -q --output="$OPDIR/$TEMP.$EXT"
}

# Override default input file name if a file is passed as first argument
if [ "$1" != "" ]
then
  FILE="$1"
fi

# Override default output file extension if a second argument is passed
if [ "$2" != "" ]
then
  EXT="$2"
  OPDIR="$EXT/$FONT"
fi

# Override default output directory if a third argument is passed
if [ "$3" != "" ]
then
  OPDIR="$3"
fi

# Validating input file
if [ ! -f $FILE ]
then
  echo "$FILE does not exists, please check the file name."
  exit 1
elif [ ! -r $FILE ]
then
  echo "$FILE can not read, please check the permissions."
  exit 2
fi

# Creating output directory if it does not exist
if [ ! -d "$OPDIR" ]
then
  mkdir "$OPDIR" -p
fi

# Reading from the input file line by line and send it to printLigature magical procedure
while read -r line
do
  printLigature $line
done <"$FILE"

# Process ending timestamp
END=$(date +%s)

echo "$CNT ligatures converted in `expr $END - $START` seconds."

exit 0
