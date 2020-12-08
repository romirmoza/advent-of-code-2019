from collections import defaultdict

def calculate_fuel_req(module):
    return (module // 3) - 2

def product_of_two_given_sum(report, sum):
    entries = defaultdict(int)
    for x in report:
        entries[x] = 1
        if entries[sum-x]:
            product2 = x * (sum-x)
            return product2

def product_of_three_given_sum(report, sum):
    for r in report:
        entries = defaultdict(int)
        for x in report:
            entries[x] = 1
            if entries[sum-x-r]:
                product3 = r * x * (sum-x-r)
                return product3

if __name__ == '__main__':
    file = open('day1_input.txt', 'r')
    report = list(map(int, file.read().split()))

    sum = 2020
    product2 = product_of_two_given_sum(report, sum)
    product3 = product_of_three_given_sum(report, sum)

    print('Product of the 2 entries = {}'.format(product2))
    print('Product of the 3 entries = {}'.format(product3))
