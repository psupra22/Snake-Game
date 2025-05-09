import pygame
from game import Game

def main() -> None:
    pygame.init()

    WIDTH, HEIGHT = 800, 800
    CELL_SIZE = 40

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    pygame.mixer.music.load("Sounds/music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    IMAGES = {
        name: pygame.image.load(f"Graphics/{name}.png") for name in [
            "head_up", "head_down", "head_left", "head_right",
            "body_horizontal", "body_vertical",
            "body_topleft", "body_topright",
            "body_bottomleft", "body_bottomright",
            "tail_down", "tail_left", "tail_right", "tail_up",
            "apple"
        ]
    }

    game = Game(screen, IMAGES, font, WIDTH, HEIGHT, CELL_SIZE)
    game.run(clock)

if __name__ == "__main__":
    main()
