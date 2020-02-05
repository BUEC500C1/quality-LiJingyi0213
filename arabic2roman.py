def int2roman(number):
    """ Convert an integer to a Roman numeral. """

    # check the number is satify several condition 
    if not isinstance(number, type(1)):

        raise TypeError("expected integer")

    if not 0 < number < 4000:

        raise ValueError ("Argument must be between 1 and 3999")

    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)

    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')

    ans = []

    for i in range(len(ints)):

        count = int(number / ints[i])

        ans.append(nums[i] * count)

        number -= ints[i] * count

    return ''.join(ans)

# def main():
#     print(int2roman(205))

# if __name__ == '__main__':
#     main()