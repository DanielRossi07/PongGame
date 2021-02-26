import pygame, sys, random

# General setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 840
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong do Rossix')

# Game Objects
ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20, 20)
left_player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
right_player = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Colors
dark_grey = (51, 51, 51)
light_grey = (192, 192, 192)

# Game Variables
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

left_player_speed = 0
right_player_speed = 0

left_score = 0
right_score = 0

# Timer Variables


# Fonts
score_font = pygame.font.SysFont('comicsans', 40)


def handle_visuals():
    global left_score, right_score

    screen.fill(dark_grey)
    pygame.draw.rect(screen, light_grey, left_player)
    pygame.draw.rect(screen, light_grey, right_player)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    screen.blit(score_font.render(str(left_score), True, light_grey), ((screen_width/2) - 30, (screen_height/2) - 20))
    screen.blit(score_font.render(str(right_score), True, light_grey), ((screen_width/2) + 15, (screen_height/2) - 20))
    screen.blit(score_font.render(str(ball_speed_x), True, light_grey), (10, 10))
    screen.blit(score_font.render(str(ball_speed_y), True, light_grey), (10, 30))


def handle_left_player_movement():
    left_player.y += left_player_speed
    if left_player.top <= 0:
        left_player.top = 0
    if left_player.bottom >= screen_height:
        left_player.bottom = screen_height


def handle_right_player_movement():
    right_player.y += right_player_speed
    if right_player.top <= 0:
        right_player.top = 0
    if right_player.bottom >= screen_height:
        right_player.bottom = screen_height


def handle_ball_movement():
    global ball_speed_x, ball_speed_y, left_score, right_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Handles collision (Screen)
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        right_score += 1
        ball_restart()

    if ball.right >= screen_width:
        left_score += 1
        ball_restart()

    # Handles collision (Players)
    if ball.colliderect(left_player) or ball.colliderect(right_player):
        ball_speed_x *= -1

    # Increases ball speed every 5 seconds


def ball_restart():
    global ball_speed_x, ball_speed_y

    # Restart ball speed to normal
    ball_speed_x = 5
    ball_speed_y = 5
    # Replace ball to initial position
    ball.update(screen_width / 2, screen_height / 2, 20, 20)
    # Wait to restart
    pygame.time.delay(500)
    # Random selects a side to start
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))
    # Restart add_ball_speed_time


def main():
    global left_player_speed, right_player_speed, right_player, left_player

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Check if key pressed
            if event.type == pygame.KEYDOWN:
                # Handle left player movement
                if event.key == pygame.K_DOWN:
                    left_player_speed += 7
                if event.key == pygame.K_UP:
                    left_player_speed -= 7
                # Handle right player movement
                if event.key == pygame.K_s:
                    right_player_speed += 7
                if event.key == pygame.K_w:
                    right_player_speed -= 7
            # Check if key not pressed
            if event.type == pygame.KEYUP:
                # Handle left player movement
                if event.key == pygame.K_DOWN:
                    left_player_speed -= 7
                if event.key == pygame.K_UP:
                    left_player_speed += 7
                # Handle right player movement
                if event.key == pygame.K_s:
                    right_player_speed -= 7
                if event.key == pygame.K_w:
                    right_player_speed += 7

        # Game Logic
        handle_left_player_movement()
        handle_right_player_movement()
        handle_ball_movement()
        # Visual
        handle_visuals()

        # Updating Window
        pygame.display.flip()
        clock.tick(60)

    # Ending program
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
