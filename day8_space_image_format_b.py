import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    l = 6
    b = 25
    size = l * b

    file = open('day8_input.txt', 'r')
    image = list(map(int, list(file.read().strip())))

    message = []
    for i in range(size):
        while image[i] == 2:
            i += size
        message.append(image[i])

    message = np.asarray(message)
    message = message.reshape(l, b)
    print('decoded message = {}'.format(message))

    plt.imshow(message, cmap='gray')
    plt.show()
