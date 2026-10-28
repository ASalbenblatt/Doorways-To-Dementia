from classes import *

screen.fill([255, 255, 255])

while(True):
    delta = timer.tick(frameRate)

    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    #-----------------Keep this section last-------------------------------------
    pygame.display.flip()  #updates the screen

    '''
    Keys:
    q - quit
    '''
    for event in events:

        
        #----------Keep this section last-------------------------
        if keys[pygame.K_q] or event.type == pygame.QUIT:
            pygame.display.quit()
            break
    else:
        continue  # Continue if the inner loop wasn't broken.
    break  # Inner loop was broken, break the outer.