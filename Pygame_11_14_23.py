import pygame

pygame.init()

screen = pygame.display.set_mode([800, 600])

# Load image
# https://drive.google.com/file/d/1FCWN7o8pUaxuLEoxJQzq0_CC9oWLxH1o/view
apple_img = pygame.image.load("Apple.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
