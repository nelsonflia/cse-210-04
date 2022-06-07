

import pyray
from point import Point
import random
from artifact import Artifact
from color import Color


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.score = 0
        self.total_score = 0 
        
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        cast1 = cast
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast1)
            self._do_updates(cast1)
            self._do_outputs(cast1)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")
        
        velocity = self._keyboard_service.get_direction()
        if velocity._y == 0:        
            player.set_velocity(velocity)
                

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
                
        pyray.draw_text(f'SCORE: {self.total_score}', 5,5,30,(255,180,80)) 
        
        player = cast.get_first_actor("players")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for gem in gems:
            gem.set_velocity(Point(0,1))
            gem.move_next(max_x, max_y)
            if len(gems) < 10:
                text = "*"
                
                x = random.randint(0, 59)
                y = random.randint(0, 39)
                position = Point(x, y)
                position = position.scale(15)

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = Color(r, g, b)
            
                new_gem = Artifact()
                new_gem.set_text(text)
                new_gem.set_font_size(30)
                new_gem.set_color(color)
                new_gem.set_position(position)
                cast.add_actor("gems", new_gem)
                
            if player.get_position().equals(gem.get_position()):
                cast.remove_actor("gems", gem)
                self.total_score = self.total_score +1 
                if self.total_score < 0:
                    self.total_score = 0
                
        for rock in rocks:
            rock.set_velocity(Point(0,1))
            rock.move_next(max_x, max_y)
            
            if len(rocks) < 10:
                text = "o" 
                      
                x = random.randint(1, 59)
                y = random.randint(1, 20)
                position = Point(x, y)
                position = position.scale(15)

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = Color(r, g, b)
                
                new_rock = Artifact()
                new_rock.set_text(text)
                new_rock.set_font_size(30)
                new_rock.set_color(color)
                new_rock.set_position(position)
                cast.add_actor("rocks", new_rock)
            if player.get_position().equals(rock.get_position()):
                cast.remove_actor("rocks", rock)
                self.total_score = self.total_score -1
                
                
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
        