import pygame, sys

def main():
    pygame.init()
    # Display Creation
    DISPLAY = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption('Pongy')
    # TODO make an icon
    # pygame.display.set_icon('assets/gfx/icon.png')
    # Clock Creation
    CLOCK = pygame.time.Clock()
    # Color Constants
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    while True:
        # If the player presses the button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill(BLACK)
        # Display Update
        pygame.display.update()
        CLOCK.tick(60)

if __name__ == "__main__":
    main()