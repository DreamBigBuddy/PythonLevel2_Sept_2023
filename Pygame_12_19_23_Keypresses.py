import pygame

pygame.init()

screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

apple_img = pygame.image.load("Apple.png")
apple_rect = pygame.Rect(0, 0, 100, 100)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        # Keypress events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                apple_rect.y -= 5

            if event.key == pygame.K_DOWN:
                apple_rect.y += 5

            if event.key == pygame.K_LEFT:
                apple_rect.x -= 5

            if event.key == pygame.K_RIGHT:
                apple_rect.x += 5

    screen.fill((255, 255, 255))

    screen.blit(apple_img, apple_rect)
    pygame.display.update()

pygame.quit()
