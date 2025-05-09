import random
import pygame

class Food:
    def __init__(self, cell_size, image, grid_width, grid_height):
        self.cell_size = cell_size
        self.image = image
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position = self._random_position()

    def _random_position(self):
        return [random.randint(0, self.grid_width - 1),
                random.randint(0, self.grid_height - 1)]

    def respawn(self, snake_body):
        while True:
            self.position = self._random_position()
            if self.position not in snake_body:
                break

    def draw(self, screen):
        x, y = self.position
        screen.blit(self.image, (x * self.cell_size, y * self.cell_size))
