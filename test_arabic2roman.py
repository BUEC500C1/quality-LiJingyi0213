from arabic2roman import int2roman

import pytest

def test_int2roman():

  num=[1, 2, 3, 4, 10, 50, 90, 755]

  roman= ["I", "II", "III", "IV", "X", "L", "XC", "DCCLV"]

  for i in range(len(num)):

    assert int2roman(num[i])== roman[i]

# def main():
#   test_int2roman()



# if __name__ == '__main__':
#   main()
