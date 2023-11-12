def findArea(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width


def findPerimeter(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return (length + width) * 2


def findVolume(length, width, height):
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Length and width and height must be non-negative.")
    return length * width * height


def findSurfaceArea(length, width, height):
    if length < 0 or width < 0:
        raise ValueError("Length and width and height must be non-negative.")
    return (length * width * 2) + (length * height * 2) + (width * height * 2)
