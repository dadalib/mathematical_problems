import math
import pytest

def is_binary_number(n):
    """Learn tocheck if it is an binary number"""
    flag= True
    i = 0
    while i< len(n) and flag:
        current_char = n[i]
        flag = (current_char =="0" or current_char =="1")
        i+=1

    return flag

def binary_to_decimal(binary):
    """Learn to convert binary to decimal"""
    if not is_binary_number(binary):
        raise ValueError(binary + " is not a binary number")
    
    decimal_value =0
    for current_char in binary:
        value = int(current_char)
        print("value",value)
        # 0*2 +1
        # 1*2 +1
        # 3*2 +1
        # 7*2 +1
        # 15*2 +1
        decimal_value = decimal_value*2 + value
        print("decimal_value",decimal_value)

    print("value",value,"decimal_value",decimal_value)
    return decimal_value

    
@pytest.mark.parametrize("n,expected",[("101",True)])
def test_is_binary_number(n,expected):
    assert is_binary_number(n) == True

def is_hex_number(number):
    for current_char in number:
        if current_char not  in "0123456789ABCDEFabcdef":
            return False

    return True

def hex_to_decimal(number):
    """How to use ord()"""
    if not is_hex_number(number):
        raise ValueError(number + "is not a hex number")

    decimal_value =0
    for current_char in number:
        if current_char.isdigit():
            value = int(current_char)

        else:
            value = ord(current_char.upper()) -ord('A')+10
            print(value)

        print("decimal value",decimal_value)
        decimal_value = decimal_value*16 + value
        print("decimal value af",decimal_value)
    

    print (decimal_value)
    return decimal_value

def separator_replace(list_words,chr_replace):
    new_string=""
    if len(list_words)<1 or type(list_words) == int:
        raise ValueError("Please entry a list")
    
    for word in list_words:
        new_string+=word+chr_replace

    print(new_string)
    return new_string


def reverse_string(word):
    """Operations with range and steps"""
    reverse_word=""
    print(len(word))
    for i in range(len(word)-1,-1,-1):
        print("i",i)
        current_char = word[i]
        print(current_char)
        reverse_word += current_char

    print(reverse_word)
    return reverse_word






        




if __name__ == "__main__":
    # binary_to_decimal("110")
    # hex_to_decimal("19")
    # separator_replace(["toto","mama"],"£££")
    reverse_string("LOLITA")

