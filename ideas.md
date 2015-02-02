# Ideas for future development #

### before doing anything fancy
* rewrite/refactor so that future modding will be easy (have "modes" and "console" with emacs-style commands and keybindings)

### do these on feature branches using git ###
* have a mode where text is printed as whole strings after pressing space or return, to display words
* more sounds: record some guitar/harmonica/flute/whatever sounds
* record voice for letters and play these instead of the generic sounds for each letter
* implement a way of manually selecting content for display (makes debugging content easier)
* use http://pygame.renpy.org/ to get this running on Android
* use mouse for drawing stuff
* piano-mode on keyboard instead of random sounds
* digramm-mode which displays every second keystroke a sequence of two letters (and similarly n-gram mode)
* use mouse for drawing digits and letters, do handwriting recognition with a neural network to replace drawn images with detected letters (to teach writing, e.g. capital letters and digits); need to choose suitable font then
* enable audio recording and playback, with pause detection to replay small snippets. May ultimately enable audio commands ("computer, pause") as well.
* after a predefined time, game stops doing anything, display fades dark red ("sleep mode")
* bind more functions directly to keys (e.g. backspace=clean, F1-F12=toggle stuff)
* have modes where only some keys print something (numbers only, letters only, non-alphanumeric only)
