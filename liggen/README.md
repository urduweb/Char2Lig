# Ligature Generator (LigGen)

A simple Bash Shell Script to generate glyphs from a file of ligatures. It uses pango library to draw graphics.

Script          | LigGen
----------------|------------------------------
Author          | Sawood Alam
Organization    | UrduWeb (urduweb.org/mehfil)
Idea            | Mohammad Saad
Licence         | GNU/GPL
Initial Release | Wednesday, March 3, 2010

## USAGE

Reads from a simple text file containing one ligature per line.

```bash
# If default ligature file exists
$ ./liggen.sh

# If custom ligature file is passed
$ ./liggen.sh input/file/path

# If custom output format (extension) is desired
$ ./liggen.sh input/file/path ext

# If custom output directory is desired
$ ./liggen.sh input/file/path ext outpu/directory/path
```

## Package

This package includes this README.md file, a LICENSE file, executable shell script liggen.sh, an example ligature file ligature.txt, a long list of Urdu ligatures urdu_total.txt, and svg graphics folder for those ligatures in the example file.

## TODO

- [ ] Extract Urdu to Roman character mapping in a seprate file.
- [ ] Switch based parameters to override defaults.
