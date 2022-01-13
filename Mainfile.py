import pygame
import sys
import os
from random import *
from pytmx import *

pygame.init()
size = width, height = 450, 450
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adventure strategy")


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл '{fullname}' не найден")
        sys.exit()
    return pygame.image.load(fullname)


class Worker(pygame.sprite.Sprite):
    steps = [load_image(f"{i}.png") for i in range(8)]

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Worker.steps[0]
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = randrange(height - self.rect[3])

    def update(self):
        # сюда таймер
        self.rect = self.rect.move(5, 0)
        self.image = self.steps[(self.steps.index(self.image) + 1) % 8]


def main():
    tile_size = 30
    map = load_pygame(f'maps/some.tmx')
    all_sprites = pygame.sprite.Group()
    for _ in range(2):
        Worker(all_sprites)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(40):
                    Worker(all_sprites)
        screen.fill((255, 255, 255))
        for x in range(width // tile_size):
            for y in range(height // tile_size):
                image = map.get_tile_image(x, y, 0)
                screen.blit(image, (tile_size * x, tile_size * y))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(12)  # переделать смену кадров по таймеру
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
