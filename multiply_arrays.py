"""
A Method for multiplying numbers in an array, so that every number in the array
gets multiplied except the number on ith position. It returns an new aaray with
the multiplied numbers.
"""


def multiply_arr(arr: list):
    n = len(arr)
    left, right = [1] * n, [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * arr[i - 1]

    for i in range(1, n):
        right[i] = right[i - 1] * arr[::-1][i - 1]

    multiplied_arr = []
    for i in range(n):
        multiplied_arr.append(left[i] * right[::-1][i])

    return multiplied_arr


def multiply_arr_2(arr):

    n = len(arr)

    product_all = 1
    for i in range(n):
        product_all = product_all * arr[i]

    nonzero_product = 1
    for i in range(n):
        if arr[i] != 0:
            nonzero_product = nonzero_product * arr[i]

    multiplied_arr = []
    if arr.count(0) <= 1:
        for i in range(n):
            try:
                multiplied_arr.append(int(product_all / arr[i]))
            except ZeroDivisionError:
                multiplied_arr.append(nonzero_product)
    else:
        multiplied_arr = [0] * n

    return multiplied_arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(f'youtube method: \n'
          f'{multiply_arr(arr)}')
    print(f'my method: \n'
          f'{multiply_arr_2(arr)}')
