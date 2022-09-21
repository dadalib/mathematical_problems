import numbers
from re import X
import pytest
import math


from operator import index
from unicodedata import digit
from math import remainder


value_to_text_mapping = {
    0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR",
    5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"
}


def number_as_txt(n):
    remainder = n%10
    value_to_txt = ""

    if remainder == 0:
        value_to_txt = "ZERO"
        print(value_to_txt)

    if remainder == 1:
        value_to_txt = "ONE"
        print(value_to_txt)
 
def calc(m,n):
    return m*n //2%7

def basic_operations(n,m):
    multiply= m*n
    divide = multiply//2
    remainder = divide%7

    print("multiply",multiply,divide,"divide",remainder,"remainder")

    
    return multiply,divide,remainder

def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive):
    """Count and sum all divisible number by 2 or 7 of a number"""
    count = 0 
    sum = 0

    for i in range(1,max_exclusive):
        print("i",i)
        if i%2 ==0 or i%7==0:
            count +=1
            sum +=i

        print("count:",count)
        print("sum",sum)

def even_or_odd(n):

    if n%2 ==0:
        print(n,"pair")

    else:
        print(n,"odd")

@pytest.mark.parametrize("m,n,expected",[(6,7,0),(3,4,6),(5,5,5)])
def test_cal(m,n,expected):
    assert calc(m,n) == expected

def digit_as_text(n):
    print (value_to_text_mapping[n % 10])
    return value_to_text_mapping[n % 10]

def number_as_text(n):
    """Cast number as txt"""
    value=""
    remaining_value = n
    while remaining_value >0:
        remainder_as_text = digit_as_text(remaining_value % 10)
        print("Text",remainder_as_text)
        remaining_value = int(remaining_value/10)
        print("Value",remaining_value)
        value = remainder_as_text +" "+value

    print(value.strip())
    return value.strip()


def number_as_text_short(n):
    value=""
    for ch in str(n):
        value += digit_as_text(int(ch)) + " "

    return value.strip()

@pytest.mark.parametrize("n,expected",[(7,"SEVEN"),(42,"FOUR TWO")])   
def test_number_as_text_short(n,expected):
    assert number_as_text_short(n)==expected


def calc_perfect_numbers(number):
    # always divisible by 1
    sum_of_multipliers =1

    for i in range(2,int(number/2)+1):
        if number %i == 0:
            print(i)
            sum_of_multipliers +=i

    print(sum_of_multipliers == number)
    return sum_of_multipliers == number


def calc_primes_up_to(max_value):
    # initally mark all values as potential prime number
    is_potentially_prime = [True for _ in range(1,max_value +2)]

    # start at 2 optimise going by half
    for number in range(2,max_value //2 +1):
        if is_potentially_prime[number]:
            erase_multiples_of_current(is_potentially_prime,number)

    return (build_primes_list(is_potentially_prime))

def erase_multiples_of_current(values,number):
    for n in range(number + number,len(values),number):
        values[n] = False
        print("Eliminating:",n)

def build_primes_list(is_potentially_prime):
    primes = []
    for number in range(2, len(is_potentially_prime)):
        if is_potentially_prime[number]:
            primes.append(number)

    return primes

def calc_primes_up_to_v2(max_value):
    is_potentially_prime = [True for _ in range(1, max_value + 2)]

    for number in range(2, int(max_value / 2) + 1):
        if is_potentially_prime[number]:
            erase_multiples_of_current(is_potentially_prime, number)

    # mark values 0 and 1 as no prime number
    is_potentially_prime[0:2] = False, False

    # merging / selection of values
    # return list(itertools.compress(range(len(is_potentially_prime)),
    #                                is_potentially_prime))

def calc_check_sum(digits):
    if not digits.isdigit():
        raise ValueError("illegal chars: nNo allow only digits")
    crc = 0
    number_list = []
    for i, current_char in enumerate(digits):
        value = (int(current_char))*(i+1)
        number_list.append(value)
        crc += value

    print(number_list,crc,crc%10)
    return int(crc%10)

def solve_quadratic_simple():
    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                if a*a +b*b == c*c:
                    print("a=",a,"/b=",b,"/c=",c)


def solve_quadratic_simple_shorter():
    return[(a,b,c) for a in range(1,100) for b in range(1,100)
                    for c in range(1,100) if a*a+b*b == c*c]

def solve_quadratic():
    for a in range(1,100):
        for b in range(1,100):
            c = int(math.sqrt(a*a + b*b))
            if a*a + b*b == c*c:
                print("a=",a,"/b=",b,"/c=",c)

def cubic():
    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                for d in range(1,100):
                    if a*a +b*b == c*c +d*d:
                        print('a',a,'b',b,'c',c,'d',d)

def cubic_shorter():
    x=[(a,b,c,d) for a in range(1,100)
                        for b in range(1,100)
                        for c in range(1,100)
                        for d in range(1,100)
                        if a*a +b*b == c*c +d*d]
    print(x,type(x))
    return x

def armstrong_numbers():
    numbers = [(x,y,z) for x in range(1,9)
                            for y in range(1,9)
                            for z in range(1,9)
                            if x*100 + y*10 +z == pow(x,3) + pow(y,3) + pow(z,3)]
    
    print (len(numbers),numbers)
    return numbers

def factorial(n):
    if n<0:
        raise ValueError("n must b >=0")
    if n==0 or n==1:
        return 1
    print(n*factorial(n-1))
    return n*factorial(n-1)

@pytest.mark.parametrize("n,expected",[(5,120)])
def test_factorial(n,expected):
    assert factorial(n)==expected

def factorial_shorter(n):
    pass
    # return functoools.reduce(lambda n_1,n:n_1*n,range(1,n+1) )

def sum_of(n):
    if n <=0:
        raise ValueError("n must be >=1")

    # recursive termination
    if n == 1:
        return 1
    
    # recursive descent
    print (n+ sum_of(n-1))
    return n+ sum_of(n-1)

def is_palindrome_simple_recursive(values):
    if len(values) <= 1:
        return True

    left =0
    right =len(values) -1

    if values[left] == values[right]:
        # attention: end is exclusive
        remainder = values[left +1 : right]
        print (remainder)

        # recursive descent
        return is_palindrome_simple_recursive(remainder)

    return False

def fib_iterative(n):
    if n <=0:
        raise ValueError("n must be >=1")

    if n==1 or n==2:
        return 1

    fib_n_2 = 1
    fib_n_1 = 1

    for _ in range(2,n):
        print("index",_)
        fib_n = fib_n_1 + fib_n_2
        print("fib_n",fib_n)
        fib_n_2 = fib_n_1
        print("fib_n_2",fib_n_2)
        fib_n_1 = fib_n
        print("fib_n_1",fib_n_1 )

    print(fib_n)
    return fib_n

@pytest.mark.parametrize("n,expected",[(4,3)])
def test_fib_iterative(n,expected):
    assert fib_iterative(n)==expected

def count_digits(value):
    if value <0:
        raise ValueError("value must be >=0")

    if value <10:
        return 1
    
    print (count_digits(value // 10)+1)
    return count_digits(value // 10)+1
    
def gcd(a,b):
    if b == 0:
        print(a)
        return a

    print(gcd(b,a%b))
    return gcd(b,a%b)

# Recursivity
def reverse_string(text):
    """ Recursivite as a while loop"""
    if len(text)<1:
        print("text",text)
        return text

    first_char = text[0]
    print(first_char)
    remaining = text[1:]
    print( remaining)


    return  reverse_string(remaining) +first_char

@pytest.mark.parametrize("text,expected",[("BA","AB")])  
def test_reverse_string(text,expected):
    assert reverse_string(text) == expected

def sum_helper(values,pos):
    if pos >= len(values):
        return 0

    return values[pos] + sum_helper(values,pos+1)


def sum_reverse(values):
    return sum_helper(values,0)

@pytest.mark.parametrize("values,expected",[(([1,2,3,-7],-1))])
def test_sum_reverse(values,expected):
    assert  sum_reverse(values)==expected

def to_binary(n):
    if n<0:
        raise ValueError("n must be >0")

    if n<=1:
        return str(n)

    remainder,last_digit =divmod(n,2)
    print("remainder",remainder,last_digit,"last digit")
    return to_binary(remainder) + str(last_digit)

@pytest.mark.parametrize("values,expected",[(14,"1111")])
def test_to_binary(values,expected):
    assert to_binary(values) == expected



def number_is_power_of_2(n):
    """
    Recursivity
    """
    if n< 2:
        return n == 1

    if n % 2 != 0:
        return False

    return number_is_power_of_2(n//2)

def power_of(value,exponent):

    if exponent <0:
        assert ValueError("Exponent must be >0")

    if exponent == 0:
        return 1

    if exponent == 1:
        return value


    return value*power_of(value,exponent-1) 

def power_of_iterative(value,exponent):
    result = 1
    while exponent > 0:
        result *=value
        exponent -=1

    print (result)
    return result



 


if __name__ == "__main__":
    # number_as_txt(10)
    # calc_sum_and_count_all_numbers_div_by_2_or_7(8)
    # basic_operations(5,5)
    # number_as_text(68)
    # number_as_text_short(65)
    # calc_primes_up_to(11)
    # build_primes_list(42)
    # calc_check_sum("345")
    # solve_quadratic_simple_shorter()
    # cubic_shorter()
    # armstrong_numbers()
    # factorial_shorter(5)
    # factorial(5)
    #  sum_of(4)
    #is_palindrome_simple_recursive(53)
    #fib_iterative(3)
    # count_digits(123)
    # gcd(42,7)
    # reverse_string("lolita")
    # sum_reverse([1,3,4,5])
    # to_binary(14)
    # power_of(2,4)
    # number_is_power_of_2(13)
    power_of_iterative(4,3)
 

