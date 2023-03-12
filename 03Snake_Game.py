import turtle
import random


WIDTH = 500
HEIGTH = 500
DELAY = 100  # milisecinds
FOOD_SIZE = 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    'left': (-20, 0),
    'right': (20, 0)
}


def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

# Game Loop


def game_loop():
    stamper.clearstamps()  # remove existing stamps made by stamper

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]
    # Check for Collision
    if new_head in snake or new_head[0] < -WIDTH / 2 or new_head[0] > WIDTH / 2 or new_head[1] < -HEIGTH / 2 or new_head[1] > HEIGTH / 2:
        reset()
    else:
        # Add new head to snake body
        snake.append(new_head)
        # Check Collision
        if not food_collision():
            snake.pop(0)       # keep snake same length unless fed.

        # Draw snake for the first time
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Refresh Screen
        screen.title(f'Snake Game. SCORE = {score}')
        screen.update()

        # Rinse and Repeat
        turtle.ontimer(game_loop, DELAY)


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(-WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(-HEIGTH / 2 + FOOD_SIZE, HEIGTH / 2 - FOOD_SIZE)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2-y1) ** 2 + (x2-x1) ** 2) ** 0.5  # Pythgoreas Theorem
    return distance

# REseting a Game


def reset():
    global score, snake, snake_direction, food, food_pos
    # Create a Snake as a list of coordinate sets
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    score = 0
    game_loop()


# Screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGTH)  # set dimension of screen
screen.title("Snake")
screen.bgcolor("cyan")
screen.tracer(0)  # remove animation


# Event Hanlders
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")
screen.onkey(go_down, "Down")

# create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()


# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE/20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)


# # Draw snake for the first time . Not required
# for segment in snake:
#     stamper.goto(segment[0], segment[1])
#     stamper.stamp()

# Set animation in motion
reset()

turtle.done()
