# Given an integer n, if n%3 print Fizz, if n%5 print Buzz, if n%3 and n%5 print FizzBuzz, else print n

def fizz_buzz(n : int) -> str:
    result = ''
    if n % 3 == 0:
        result += 'Fizz'
    if n % 5 == 0:
        result += 'Buzz'
    if result == '':
        return str(n)
    else:
        return result

def test():
    assert fizz_buzz(3) == 'Fizz'
    assert fizz_buzz(5) == 'Buzz'
    assert fizz_buzz(15) == 'FizzBuzz'
    assert fizz_buzz(4) == '4'
    assert fizz_buzz(-5) == 'Buzz'
    assert fizz_buzz(3.14) == '3.14'
    # assert fizz_buzz('Ioana') == 'Fizz'

def main():
    test()
    try:
        n = int(input())
        print(fizz_buzz(n))
    except ValueError:
        print('Please enter an integer')


if __name__ == '__main__':
    main()