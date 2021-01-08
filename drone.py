import pygame


class Drone:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.display_width = 780
        self.display_height = 780

    def drone_move(self, move_distace, direction):
        if direction == pygame.K_LEFT and self.x > 0:
            self.x -= move_distace
        if direction == pygame.K_RIGHT and self.x < self.display_width-self.size:
            self.x += move_distace
        if direction == pygame.K_DOWN and self.y < self.display_height-self.size:
            self.y += move_distace
        if direction == pygame.K_UP and self.y > 0:
            self.y -= move_distace

    # issue here
    def is_step_valid(self, direction):
        if direction == pygame.K_LEFT and self.x > 0:
            return True
        if direction == pygame.K_RIGHT and self.x < self.display_width-self.size:
            return True
        if direction == pygame.K_DOWN and self.y < self.display_height-self.size:
            return True
        if direction == pygame.K_UP and self.y > 0:
            return True
