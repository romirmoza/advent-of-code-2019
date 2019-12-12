if __name__ == '__main__':
    l = 6
    b = 25
    size = l * b

    file = open('day8_input.txt', 'r')
    image = list(map(int, list(file.read().strip())))
    min_zeroes = size
    for i in range(len(image) // size):
        layer = image[i * size : (i+1) * size]
        zeroes = sum([1 for pixel in layer if not pixel])
        if zeroes < min_zeroes:
            min_zeroes = zeroes
            min_zero_layer = layer
            ones_times_two = sum([1 for pixel in layer if pixel == 1]) \
                            * sum([1 for pixel in layer if pixel == 2])
    print('1s x 2s in the layer with least zeroes = {}'.format(ones_times_two))
