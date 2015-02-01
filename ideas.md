# Ideas for future development #

### before taking it public ###
* create new images and sounds with CC licenses

### before doint anything fancy
* no sounds right now, fix that
* rewrite/refactor so that future modding will be easy (have "modes" and "console" with emacs-style commands and keybindings)
* implement a way of manually selecting content for display

### do these on feature branches using git ###
* use http://pygame.renpy.org/ to get this running on Android
* use mouse for drawing stuff
* piano-mode on keyboard instead of random sounds
* digramm-mode which displays every second keystroke a sequence of two letters (and similarly n-gram mode)
* use mouse for drawing digits and letters, do handwriting recognition with a neural network to replace drawn images with detected letters (to teach writing, e.g. capital letters and digits); need to choose suitable font then
* enable audio recording and playback, with pause detection to replay small snippets. May ultimately enable audio commands ("computer, pause") as well.
* after a predefined time, game stops doing anything, display fades dark red ("sleep mode")
* bind more functions directly to keys (spacebar=clean, enter=toggle sound)
* have modes where only some keys print something (numbers only, letters only, non-alphanumeric only)
