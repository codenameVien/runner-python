import pygame
import random

pygame.init()

# screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
floor_y = screen_height - 100

# RGB color values
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# player settings
player_size = 50

# obstacle settings
obstacle_width = 30
obstacle_x = screen_width
obstacle_velocity = 10


# game loop
def game_loop():
    # player settings
    player_x = 100
    player_y = floor_y - player_size
    max_jump_height = 110
    
    # obstacle settings
    obstacle_height = random.randint(50, max_jump_height - 20)
    obstacle_list = [pygame.Rect(obstacle_x, floor_y - obstacle_height, obstacle_width, obstacle_height)]
    
    score = 0
    run = True
    clock = pygame.time.Clock()
    player_jump = False
    jump_height = 10
    while run:
        clock.tick(60)  # 60 FPS
        screen.fill(white)
        pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))
        
        for obstacle in obstacle_list:
            pygame.draw.rect(screen, green, obstacle)
            obstacle.x -= obstacle_velocity
            if obstacle.x < -obstacle_width:
                score += 1 
                obstacle_height = random.randint(50, max_jump_height - 20)
                obstacle_list.pop(obstacle_list.index(obstacle))
                obstacle_list.append(pygame.Rect(obstacle_x, floor_y - obstacle_height, obstacle_width, obstacle_height))
        
        if player_jump:
            if jump_height >= -10:
                neg = 1
                if jump_height < 0:
                    neg = -1
                player_y -= (jump_height ** 2) * 0.5 * neg
                jump_height -= 1
            else:
                player_jump = False
                jump_height = 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_jump = True

        if player_y + player_size > floor_y:
            player_y = floor_y - player_size
        if pygame.Rect(player_x, player_y, player_size, player_size).collidelist(obstacle_list) >= 0:
            print('Game over! Your score:', score)
            run = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    game_loop()
