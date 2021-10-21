import pygame, sys

def main():
    pygame.init()
    # Display Creation
    DISPLAY = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Pongy')
    # Loading and Displaying of Icon
    displayIcon = pygame.image.load('assets/gfx/icon.png')
    pygame.display.set_icon(displayIcon)
    # Clock Creation
    CLOCK = pygame.time.Clock()

    while True:
        # If the player presses the button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill((0, 0, 0))
        # Update Display
        pygame.display.flip()
        CLOCK.tick(60)

if __name__ == "__main__":
    main()
