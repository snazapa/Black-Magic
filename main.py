import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode(size=(640, 300))

    # define a variable to control the main loop
    running = True

    image = pygame.image.load("Paul_Benis.png")

    # main loop
    while running:
        screen.blit(image, (50,50))
        pygame.display.flip()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

if __name__=="__main__":
    main()
