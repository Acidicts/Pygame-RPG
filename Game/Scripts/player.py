import pygame
from pygame.math import Vector2
from Game.utils.settings import TILE_SIZE
from Game.utils.utils import Animation


class Player:
    def __init__(self, x, y, game):
        self.img_num = 0
        self.img = game.assets["player"]["player"][self.img_num].convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE_SIZE, TILE_SIZE))

        self.rect = self.img.get_rect()
        self.vector = Vector2(self.rect.center)

        self.rect.x = x
        self.rect.y = y

        self.game = game
        self.action = {
            "idle": ([0, 1, 2, 3, 4, 5], False),
            "left": ([6, 7, 8, 9, 10, 11], True),
            "right": ([6, 7, 8, 9, 10, 11], False),
            "up": ([30, 31, 32, 33, 34, 35], False),
            "down": ([18, 19, 20, 21, 22, 23], False),
            "right_down": ([24, 25, 26, 27, 28, 29], False),
            "right_left": ([24, 25, 26, 27, 28, 29], True),
            "up_left": ([30, 31, 32, 33, 34, 35], True),
            "up_right": ([30, 31, 32, 33, 34, 35], False),
        }

        self.animation = None
        self.frames = None

        self.mode = "idle"
        self.change_mode(self.mode)

    def update(self):
        self.control()
        self.draw()
        self.animation.update()

    def draw(self):
        self.img = self.animation.img()
        self.game.win.blit(self.img, self.vector)

    def control(self):
        keys = pygame.key.get_pressed()

        movement = [0, 0]

        if keys[pygame.K_w]:
            movement[1] -= 5

        if keys[pygame.K_s]:
            movement[1] += 5

        if keys[pygame.K_a]:
            movement[0] -= 5

        if keys[pygame.K_d]:
            movement[0] += 5

        if movement[0] > 0 and movement[1] > 0:
            if self.mode != "right_down":
                self.change_mode("right_down")

        if movement[0] < 0 and movement[1] < 0:
            if self.mode != "up_left":
                self.change_mode("up_left")

        if movement[0] > 0 > movement[1]:
            if self.mode != "up_right":
                self.change_mode("up_right")

        if movement[0] < 0 < movement[1]:
            if self.mode != "right_left":
                self.change_mode("right_left")

        if movement[0] == 0 and movement[1] == 0:
            if self.mode != "idle":
                self.change_mode("idle")

        if movement[0] > 0 == movement[1]:
            if self.mode != "right":
                self.change_mode("right")

        if movement[0] < 0 == movement[1]:
            if self.mode != "left":
                self.change_mode("left")

        if movement[1] > 0 == movement[0]:
            if self.mode != "down":
                self.change_mode("down")

        if movement[1] < 0 == movement[0]:
            if self.mode != "up":
                self.change_mode("up")

        self.vector += movement

        self.vector.normalize()

    def change_mode(self, mode):
        mode = mode.lower()
        self.mode = mode

        self.frames = [self.game.assets["player"]["player"][i] for i in self.action[mode][0]]
        self.animation = Animation(self.game, self.frames, 3, True, self.action[mode][1])
