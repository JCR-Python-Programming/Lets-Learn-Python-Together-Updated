# Import the math module to invoke the square root, math.sqrt(n) function.

import math

# Python understands the Order of Operation with parentheses: n + (n + n + n) * n, n + (n + n + n) / n

BEDMAS_list = [
  2 + 2 + 2 * 6 * 2,  # index[0] = 4 + 24 = 28

  (2 + 2 + 2 * 6) * 2,  # index[1] = (16) x 2 = 32

  (2 + 2 + 2) * 6 * 2,  # index[2] = (6) x 12 = 72

  2 + (2 + 2) * 6 * 2,  # index[3] = 2 + (4) x 12 = 50

  2 + (2 + 2 * 6) * 2,  # index[4] = 2 + (14) x 2 = 30

  2 + (2 + 2 * 6 * 2),  # index[5] = 2 + (26) = 28

  2 + 2 + (2 * 6 * 2),  # index[6] = 4 + (24) = 28

# Invoke the integer, int(n) function to convert floats to integers.
# You can also invoke the float(n) function to create floating-
# point numbers, not shown here.

  int(2 + 2 + 2 * 6 / 2),  # index[7] = 4 + 6 = 10

  int((2 + 2 + 2 * 6) / 2),  # index[8] = (16) / 2 = 8

  int(2 + (2 + 2) * 6 / 2),  # # index[9] = 2 + (4) x 6 / 2 = 14

  int(2 + (2 + 2 * 6) / 2),  # index[10] = 2 + (14) / 2 = 9

  int(2 + (2 + 2 * 6 / 2)),  # index[11] = 2 + (8) = 10

  int(2 + 2 + (2 * 6 / 2)),  # index[12] = 4 + (6) = 10

# Invoke a double ** asterisk to create exponents.

  2 + 3 ** 2,  # index[13] = 2 + 9 = 11

  (2 + 3) ** 2,  # index[14] = 5 x 5 = 25

  (2 + 3 * 2) ** 2,  # index[15] = 8 x 8 = 64

  (2 + 3 * 2 ** 2) * 2,  # index[16] = (14) x 2 = 28

# Invoke the power, pow(n,n) function to create exponents.

  pow(2,2),  # index[17] = 2 x 2 = 4

  pow(2 + 3,2),  # index[18] = 5 x 5 = 25

  pow(2 + 3,1 + 1),  # index[19] = 5 x 5 = 25

# Invoke the square root, math.sqrt(n) function to find the root of
# an integer number. Invoke the integer, int(n) function to convert
# floats to integers. You can also invoke the float(n) function to
# create floating point numbers, not shown here.

  int(math.sqrt(9)),  # index[20] = 9 = 3 x 3

  int(math.sqrt(9 * 9)),  # index[21] = 81 = 9 x 9

  int(math.sqrt(16)),  # index[22] = 16 = 4 x 4

   int(math.sqrt(4 * 4))  # index[23] = 16 = 4 x 4
  ]

print('You have',len(BEDMAS_list),'list values in BEDMAS_list.')  # Count how many list values there are.

for i in BEDMAS_list:print(i)

# create a variable called 'terms' to illustrate the Order of Operation sequence.

terms = ((2 + 3) * 2 + (4 + 6) * 2) / 2 - 5

print(int(terms))  # = ((5 * 2) + (10 * 2)) / 2 = 15 - 5 = 10


terms = -5 + ((2 + 3) * 2 + (4 + 6) * 2) / 2

print(int(terms))  # = -5 + ((5 * 2) + (10 * 2)) / 2 = -5 + 15 = 10
