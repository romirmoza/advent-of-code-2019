from itertools import cycle, islice
from fractions import gcd

def FFT(signal, base_pattern, phases):
    signal_length = len(signal)
    for phase in range(phases):
        next_signal = []
        for position in range(signal_length):
            pattern = [val for val in base_pattern for _ in (range(position+1))]
            pattern_length = len(pattern)
            pattern = list(islice(cycle(pattern), signal_length+1))
            pattern.pop(0) # offset
            next_signal.append(abs(sum([s*p for s, p in zip(signal, pattern)])) % 10)
        signal = next_signal
    return signal

def FFT_last_digits(signal, base_pattern, phases, repeat, output):
    offset = int(''.join(map(str, signal[:7])))
    digits_from_end = len(signal) * repeat - offset # Number of digits from the end the output is at
    repeated_length = ((digits_from_end // len(signal)) + 1) * len(signal)
    signal = list(islice(cycle(signal), repeated_length))
    signal = signal[-digits_from_end:]
    for phase in range(phases):
        sum_signal = sum(signal)
        next_signal = []
        for i in range(digits_from_end):
            next_signal.append(abs(sum_signal) % 10)
            sum_signal -= signal[i]
        signal = next_signal
    return next_signal[:output]

if __name__ == '__main__':
    file = open('day16_input.txt', 'r')
    signal = list(map(int, list(file.read())))
    base_pattern = [0, 1, 0, -1]
    phases = 100

    signal_length = len(signal)
    base_pattern_length = len(base_pattern)

    final_signal = FFT(signal, base_pattern, phases)

    repeat = 10000
    output = 8 # Number of digits in the output
    final_signal2 = FFT_last_digits(signal, base_pattern, phases, repeat, output)

    print('First 8 digits of signal after 100 phases of FFT = {}'.format(''.join(map(str, final_signal[:8]))))
    print('First 8 digits of signal after 100 phases of FFT = {}'.format(''.join(map(str, final_signal2))))
