import pygame

pygame.init()

screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

# Load image
# https://drive.google.com/file/d/1FCWN7o8pUaxuLEoxJQzq0_CC9oWLxH1o/view
apple_img = pygame.image.load("Apple.png")
apple_rect = pygame.Rect(0, 0, 100, 100)

apple_vel_x = 10
apple_vel_y = 10

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    if apple_rect.left < 0 or apple_rect.right > 800:
        apple_vel_x *= -1

    if apple_rect.top < 0 or apple_rect.bottom > 600:
        apple_vel_y *= -1

    apple_rect.x += apple_vel_x
    apple_rect.y += apple_vel_y

    screen.blit(apple_img, apple_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
