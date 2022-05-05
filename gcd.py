# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    while (b != 0):
        t = a       # set aside the value of a
        print("a:{} b:{} t:{}".format(a, b, t))

        a = b       # set a equal to b
        b = t % b   # remainder of divide t (which is a) by b

    return a


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
