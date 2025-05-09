import pygame
from snake import Snake
from food import Food
from ui import UI

class Game:
    def __init__(self, screen, images, font, width, height, cell_size):
        self.screen = screen
        self.images = images
        self.font = font
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid_width = width // cell_size
        self.grid_height = height // cell_size
        self.ui = UI(screen, font)
        self.snake = Snake(cell_size, images)
        self.food = Food(cell_size, images["apple"], self.grid_width, self.grid_height)
        self.score = 0
        self.state = "MENU"

    def run(self, clock):
        while True:
            self._handle_events()
            if self.state == "GAME":
                self._update()
            self._draw()
            pygame.display.flip()
            clock.tick(5)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if self.state == "MENU" and event.key == pygame.K_SPACE:
                    self._start_game()
                elif self.state == "GAME_OVER":
                    if event.key == pygame.K_r:
                        self._start_game()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                elif self.state == "GAME":
                    if event.key == pygame.K_UP:
                        self.snake.set_direction("UP")
                    elif event.key == pygame.K_DOWN:
                        self.snake.set_direction("DOWN")
                    elif event.key == pygame.K_LEFT:
                        self.snake.set_direction("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.set_direction("RIGHT")

    def _start_game(self):
        self.snake.reset()
        self.food.respawn(self.snake.body)
        self.score = 0
        self.state = "GAME"

    def _update(self):
        if not self.snake.move() or self.snake.check_collision(self.grid_width, self.grid_height):
            self.state = "GAME_OVER"
            return

        if self.snake.body[0] == self.food.position:
            self.snake.eat()
            self.score += 1
            self.food.respawn(self.snake.body)

    def _draw(self):
        self._draw_background()
        if self.state == "MENU":
            self.ui.draw_menu(self.width, self.height)
        elif self.state == "GAME":
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.ui.draw_score(self.score, self.width)
        elif self.state == "GAME_OVER":
            self.ui.draw_game_over(self.score, self.width, self.height)

    def _draw_background(self):
        light = (170, 215, 81)
        dark = (162, 209, 73)
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                color = light if (row + col) % 2 == 0 else dark
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color, rect)
