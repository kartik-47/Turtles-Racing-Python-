import turtle
import time
import random

WIDTH, HEIGHT = 500, 500 # const. values
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'cyan', 'brown']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2-10)?: ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric...Try Again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2 to 10')

def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1) # this will decides the spacing btw the turtles
    for i, color in enumerate(colors): #enumerate basically gives the index and the value
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90) # default position is right
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20) # this will set the position of the turtles through the x,y coordinates
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_screen(): # where all the setup related to turtle screen is
    screen = turtle.Screen() # creates the screen
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!') # to change the title of the screen

racers = get_number_of_racers()
init_screen()

random.shuffle(COLORS)
colors = COLORS[:racers] # this will select the unique colors to the racers as per the numbers given
winner = race(colors)
print("The winner is the turtle with color:",winner)
time.sleep(5)
