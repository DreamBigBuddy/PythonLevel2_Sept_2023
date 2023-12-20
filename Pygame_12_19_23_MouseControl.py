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

        # This will move the apple to where your mouse
        # clicks on the screen
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            apple_rect.x = pos[0] - apple_rect.width/2
            apple_rect.y = pos[1] - apple_rect.height/2

    # This will always move the apple to where your mouse
    # is on the screen, even if you do not click
    # Comment these 3 lines or the 3 lines in the
    # conditional above to see the difference
    pos = pygame.mouse.get_pos()
    apple_rect.x = pos[0] - apple_rect.width/2
    apple_rect.y = pos[1] - apple_rect.height/2

    # Makes the apple fall to the bottom of the screen
    if apple_rect.bottom < 600:
        apple_rect.y += 1

    screen.fill((255, 255, 255))

    screen.blit(apple_img, apple_rect)
    pygame.display.update()

pygame.quit()
