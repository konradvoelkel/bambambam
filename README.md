# Bam Bam Bam
Teach toddlers human-computer interaction.

Or: let them safely play with your computer.

![Screenshot from 16.02.2014](/web/screenshot-2014-02-16-medium.png?raw=true "Screenshot")

This is an almost-rewrite fork of the earlier "Bam Bam" game, which contained different graphics and sounds (with unclear licensing). This game contains only public domain graphics and sounds.

## Installation

Open a fresh terminal.

Run
`git clone https://github.com/konradvoelkel/bambambam.git`
in the folder where you want to have a folder `bambambam` with the game in it.

Then you can either be a developer and run
`python2 setup.py develop`
`python2 src/bambambam.py`

or you just want to play, then you run
`python2 setup.py install`
and hope for the best, which is that
`bambambam`
is now a working command on your machine.
Maybe there will even be some menu entry somewhere.

OK, let's be honest, only the developer mode works at the moment.

## Remarks

Someone should really write better installation instructions, including how to install a working Pygame package (the only requirement) and running this on OSX or Windows.
Recommendation: use Python2, where Pygame is a lot easier to install. The code runs on Python2 and Python3.

See also a companion blogpost:
http://www.konradvoelkel.com/homepage/project-ideas/bambam-to-lisp/

Beta-testers, co-developers, idea-givers and creators of content (images&sounds) are very welcome.

May be important to know: typing "quit" closes the program.
