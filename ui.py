import pygame

class UI:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def draw_score(self, score, width):
        text = self.font.render(f"{score}", True, (255, 255, 255))
        self.screen.blit(text, (width - 40, 10))

    def draw_menu(self, width, height):
        self._draw_centered("SNAKE", 72, (0, 255, 0), width, height, -60)
        self._draw_centered("Press SPACE to Start", 36, (255, 255, 255), width, height, 0)

    def draw_game_over(self, score, width, height):
        self._draw_centered("GAME OVER", 72, (255, 0, 0), width, height, -60)
        self._draw_centered(f"Final Score: {score}", 36, (255, 255, 255), width, height, 0)
        self._draw_centered("Press R to Restart or ESC to Quit", 36, (255, 255, 255), width, height, 40)

    def _draw_centered(self, text, size, color, width, height, offset_y=0):
        font = pygame.font.Font(None, size)
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=(width // 2, height // 2 + offset_y))
        self.screen.blit(surf, rect)
