import pygame

class Snake:
    def __init__(self, cell_size, images):
        self.cell_size = cell_size
        self.images = images
        self.reset()

    def reset(self):
        self.body = [[3, 5], [2, 5], [1, 5]]
        self.direction = "RIGHT"
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1
        elif self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1

        new_head = [head_x, head_y]

        if new_head in self.body:
            return False

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

        return True

    def check_collision(self, width, height):
        head_x, head_y = self.body[0]
        return (
            head_x < 0 or head_x >= width or
            head_y < 0 or head_y >= height
        )

    def eat(self):
        self.grow = True

    def set_direction(self, new_direction):
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def draw(self, screen):
        for i, segment in enumerate(self.body):
            x, y = segment
            if i == 0:
                img = self.images[f"head_{self.direction.lower()}"]
            elif i == len(self.body) - 1:
                prev_x, prev_y = self.body[i - 1]
                dx, dy = x - prev_x, y - prev_y
                img = self._get_tail_image(dx, dy)
            else:
                img = self._get_body_image(i)
            screen.blit(img, (x * self.cell_size, y * self.cell_size))

    def _get_tail_image(self, dx, dy):
        if dx == 1:
            return self.images["tail_right"]
        elif dx == -1:
            return self.images["tail_left"]
        elif dy == 1:
            return self.images["tail_down"]
        else:
            return self.images["tail_up"]

    def _get_body_image(self, i):
        x, y = self.body[i]
        prev_x, prev_y = self.body[i - 1]
        next_x, next_y = self.body[i + 1]
        dx1, dy1 = prev_x - x, prev_y - y
        dx2, dy2 = next_x - x, next_y - y

        if dx1 == dx2:
            return self.images["body_vertical"]
        elif dy1 == dy2:
            return self.images["body_horizontal"]
        elif (dx1 == -1 and dy2 == -1) or (dx2 == -1 and dy1 == -1):
            return self.images["body_topleft"]
        elif (dx1 == 1 and dy2 == -1) or (dx2 == 1 and dy1 == -1):
            return self.images["body_topright"]
        elif (dx1 == -1 and dy2 == 1) or (dx2 == -1 and dy1 == 1):
            return self.images["body_bottomleft"]
        else:
            return self.images["body_bottomright"]
