def quadrant (point1, point2):
    if point1 and point2 > 0:
        return ("First Quadrant")
    elif point1 < 0 and point2 > 0:
        return ("Second Quadrant")
    elif point1 < 0 and point2 < 0:
        return ("Third Quadrant")
    elif point1 > 0 and point2 < 0:
        return ("Fourth Quadrant")
    else:
        return ("The points are in the origin")