# this program will calculate the area of a rectangle

def rectarea(l, w):
    """ A function that will calculate the area of a rectangle """
    if l < 0 or w < 0:
        raise ValueError('Rectangle sides cannot be less than 0.')
    return l * w

def main():
    l = float(input('Enter the length of the rectangle: '))
    w = float(input('Enter the width of the rectangle: '))
    print('The area of the rectangle is', rectarea(l, w), 'square units.')

#main()

