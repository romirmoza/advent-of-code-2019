import numpy as np
from matplotlib import pyplot as plt

def layer_with_min_zeroes(image):
    min_zeroes = size
    for i in range(len(image) // size):
        layer = image[i * size : (i+1) * size]
        zeroes = sum([1 for pixel in layer if not pixel])
        if zeroes < min_zeroes:
            min_zeroes = zeroes
            min_zero_layer = layer
    return min_zero_layer

def decoded_message(image):
    message = []
    for i in range(size):
        while image[i] == 2:
            i += size
        message.append(image[i])
    message = np.asarray(message)
    message = message.reshape(l, b)
    return message

if __name__ == '__main__':
    l = 6
    b = 25
    size = l * b

    file = open('day8_input.txt', 'r')
    image = list(map(int, list(file.read().strip())))

    min_zero_layer = layer_with_min_zeroes(image)
    ones_times_two = sum([1 for pixel in min_zero_layer if pixel == 1]) \
                    * sum([1 for pixel in min_zero_layer if pixel == 2])

    print('1s x 2s in the layer with least zeroes = {}'.format(ones_times_two))

    message = decoded_message(image)

    print('decoded message = {}'.format(message))
    plt.imshow(message, cmap='gray')
    plt.show()
