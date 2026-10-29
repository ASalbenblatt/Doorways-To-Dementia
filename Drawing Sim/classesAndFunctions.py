from vectorMath import *

def mouseToScreen(mouse: vector, offset: vector) -> vector:
    return add(add(scaleBy(mouse, 1/screenScaleFactor), (scaleBy(screen.get_size(), 1/(2*screenScaleFactor)))), offset)

def randomOffset() -> vector:
    return (uniform(-1, 1)*screen.get_width()/(2*screenScaleFactor), uniform(-1, 1)*screen.get_height()/(2*screenScaleFactor))

class lines:
    def __init__ (self, initialPosition: vector) -> None:
        self.points: list[vector] = [initialPosition]

    def addPoint (self, position: vector) -> None:
        if distanceBetween(self.points[-1], position) >= distanceBetweenPoints:
            self.points.append(position)

    def draw (self, screen) -> None:
        if self.points.__len__() >= 2:
            pygame.draw.lines(screen, lineColor, False, self.points, lineThickness)
