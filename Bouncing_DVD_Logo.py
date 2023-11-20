import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

WIDTH, HEIGHT =bext.size()
WIDTH -= 1

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLOURS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT    = 'ur'
UP_LEFT     = 'ul'
DOWN_RIGHT  = 'dr'
DOWN_LEFT   = 'dl'
DIRECTIONS  = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

COLOUR = 'colour'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    logos = {}
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOUR: random.choice(COLOURS)}),
                      X: random.randit(1, WIDTH - 4),
                      X: random.randit(1, HEIGHT - 4),
        if logos[-1][X] % 2 == 1:
              logos[-1][X] -= 1

    cornerBounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            originalDirection = logo[DIR]

            if logo[X] == o and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                    cornerBouces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                  logo[DIR] = UP_RIGHT
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                  logo[DIR] = DOWN_LEFT
                  cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                  logo[DIR] = DOWN_LEFT
                  cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                  logo[DIR] = UP_LEFT
                  cornerBounces += 1
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                    