
import os
import random

from actor import Actor
from artifact import Artifact
from cast import Cast

from director import Director

from keyboard_service import KeyboardService
from video_service import VideoService

from color import Color
from point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the player

    x = int(MAX_X / 2)
    y = int(575)
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("players", player)
    
    # create the gems
  
    text = "*"
    x = random.randint(0, COLS - 1)
    y = random.randint(0, ROWS - 1)
    position = Point(x, y)
    position = position.scale(CELL_SIZE)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = Color(r, g, b)
    
    gem = Artifact()
    gem.set_text(text)
    gem.set_font_size(FONT_SIZE)
    gem.set_color(color)
    gem.set_position(position)
    cast.add_actor("gems", gem)

# create the rocks

    text = "o"    
    x = random.randint(1, COLS - 1)
    y = random.randint(1, ROWS/2)
    position = Point(x, y)
    position = position.scale(CELL_SIZE)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = Color(r, g, b)
    
    rock = Artifact()
    rock.set_text(text)
    rock.set_font_size(FONT_SIZE)
    rock.set_color(color)
    rock.set_position(position)
    cast.add_actor("rocks", rock)
    
    # start the game

    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()