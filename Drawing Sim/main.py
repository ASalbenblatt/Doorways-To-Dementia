from classesAndFunctions import *

screen.fill([255, 255, 255])

frame: int = 0

offset: vector = randomOffset()
currentLine: lines = lines(mouseToScreen(pygame.mouse.get_pos(), offset))

while(True):
    delta = timer.tick(frameRate)

    frame += 1

    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    if pygame.mouse.get_pressed()[0]:
        currentLine.addPoint(mouseToScreen(pygame.mouse.get_pos(), offset))

    #-----------------Keep this section last-------------------------------------
    pygame.display.flip()  #updates the screen

    '''
    Keys:
    q - quit
    r - reset
    '''

    if keys[pygame.K_r]:
        screen.fill([255, 255, 255])

    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            currentLine.draw(screen)

        if event.type == pygame.MOUSEBUTTONDOWN:
            offset = randomOffset()
            currentLine = lines(mouseToScreen(pygame.mouse.get_pos(), offset))

        
        #----------Keep this section last-------------------------
        if keys[pygame.K_q] or event.type == pygame.QUIT:
            pygame.display.quit()
            break
    else:
        continue  # Continue if the inner loop wasn't broken.
    break  # Inner loop was broken, break the outer.