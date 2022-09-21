def extract_digit(number):
    remaining_value = number
    while remaining_value>0:
        digit = remaining_value %10
        print("digit",digit)
        remaining_value = remaining_value//10
        print("remaining_value",remaining_value)
        print("BOOM",digit,end='')
    print()

def count_digits(number):
    count=0
    remaining_value = number
    while remaining_value>0:
        remaining_value = remaining_value//10
        print(remaining_value)
        count +=1

    print(count)
    return count

# Prime number
def is_prime(potentially_prime):

    for i in range(2,potentially_prime// 2+1):
        print(potentially_prime// 2+1)
        if potentially_prime % i ==0:
            print("False")
            return False
         
    print("True")
    return True


if __name__ == "__main__":
    # count_digits(12342342324646)
    # extract_digit(126)
    is_prime(10)
    #double_it = lambda x:x*2
    # print(double_it(2))


