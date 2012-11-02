  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo
  I I I I I I I      8     8   8           8     8     o  8    8
  I  \ `+' /  I      8         8           8     8        8    8
   \  `-+-'  /       8         8           8      ooooo   8oooo
    `-__|__-'        8         8           8           8  8
        |            8     o   8           8     o     8  8
  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8

Welcome to GNU CLISP 2.44 (2008-02-02) <http://clisp.cons.org/>

Copyright (c) Bruno Haible, Michael Stoll 1992, 1993
Copyright (c) Bruno Haible, Marcus Daniels 1994-1997
Copyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998
Copyright (c) Bruno Haible, Sam Steingold 1999-2000
Copyright (c) Sam Steingold, Bruno Haible 2001-2008

Type :h and hit Enter for context help.

[1]> (+ 5 5)

10
[2]> (defun hello-world () (format t "hellp"))

HELLO-WORLD
[3]> (hello-world)
hellp
NIL
[4]> (hello-world)
hellp
NIL
[5]> (hello-world)  C-c C-c
*** - READ-LINE: Ctrl-C: User break
The following restarts are available:
ABORT          :R1      Abort main loop
Break 1 [6]> :r1

[7]> (hello-world)
hellp
NIL
[8]> ,

*** - READ: comma is illegal outside of backquote
The following restarts are available:
ABORT          :R1      Abort main loop
Break 1 [9]> :r1

[10]> :

:||
[11]> 