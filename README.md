#  Snake Game (made with only tkinter)
<a href="https://en.wikipedia.org/wiki/Snake_(video_game_genre)">Snake</a> is a game from my childhood (the 1980s). I wanted to learn about the `tkinter` library in Python, so I decided to use it to make Snake as a challenge.

## Necessary Software
They're coded in Python 3.10. It's a very simple program though, so I imagine it would work on earlier 3.x versions. The `tkinter` library is the standard GUI library for Python, so it should install with Python itself.

## Game Play
The arrow keys are bound to the `Change_Direction(evt)` function. It's very intuitive. Just like the original Snake game, your snake grows as you eat apples. Don't run into the wall or your own snake body, otherwise it's game over.

## Room for Improvement
The code is pretty barebones, but mostly functional. The only issue I've found is that, if you press multiple arrow keys too quickly, the snake will not respond to the intermediate presses. It can pass back over itself without ending the game.

## License
This code is under the <a href="https://github.com/ScienceAsylum/Farkle-Probability/blob/main/LICENSE">GNU General Public License v3.0</a>.
