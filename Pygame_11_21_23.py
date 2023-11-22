import pygame

pygame.init()

screen = pygame.display.set_mode([800, 600])

# Load image
# https://drive.google.com/file/d/1FCWN7o8pUaxuLEoxJQzq0_CC9oWLxH1o/view
apple_img = pygame.image.load("Apple.png")
apple_rect = pygame.Rect(0, 0, 100, 100)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    apple_rect.x += 1

    screen.blit(apple_img, apple_rect)
    pygame.display.update()

pygame.quit()
