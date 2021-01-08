import pygame
from drone import *
from man import *

pygame.init()
font = pygame.font.Font('arial.ttf', 15)

# rgb colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
screen_width = 780
screen_height = 780

BLOCK_VELOCITY = 20

# initialize man and drone
drone = Drone(20, screen_height-40, BLOCK_SIZE, RED)
man = Man(BLOCK_SIZE, BLUE1)
man_x, man_y = man.place_man(drone.x, drone.y, screen_width, screen_height)

pygame_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Blocks')


game_exit = False
steps = 0
time = 0
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            time += 1
            drone.drone_move(BLOCK_VELOCITY, event.key)

            if drone.is_step_valid(event.key):
                steps += 1

            # man move
            if time % 2:
                man_x, man_y = man.move_man(man_x, man_y, 0, 'left')
        # if drone.x > screen_width - BLOCK_SIZE or drone.x < 0 or drone.y > screen_height - BLOCK_SIZE or drone.y < 0:
        #     game_exit = True

        # drone moves 20 pixel in 1 sec
        # man moves 20 pixel in 2 sec

    pygame_display.fill(BLACK)

    pygame.draw.rect(pygame_display, drone.color, [
                     drone.x, drone.y, drone.size, drone.size])
    pygame.draw.rect(pygame_display, man.color, [
                     man_x, man_y, man.size, man.size])

    ############## DISPLAY INFO ##############
    drone_text = font.render("DRONE_X: " + str(drone.x) +
                             " DRONE_Y: " + str(drone.y), True, WHITE)
    pygame_display.blit(drone_text, [0, 0])

    person_text = font.render("PERSON_X: " + str(man_x) +
                              " PERSON_Y: " + str(man_y), True, WHITE)
    pygame_display.blit(person_text, [0, 17])

    if drone.x == man_x and drone.y == man_y:
        found_text = font.render("PERSON FOUND", True, WHITE)
        pygame_display.blit(found_text, [0, 34])

    steps_text = font.render(
        "STEPS = " + str(steps), True, WHITE)
    pygame_display.blit(steps_text, [580, 0])

    time_text = font.render("TIME = " + str(time), True, WHITE)
    pygame_display.blit(time_text, [580, 20])
    ############## DISPLAY INFO ##############

    pygame.display.update()
