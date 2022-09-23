import math
from multiprocessing.sharedctypes import Value
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


def reverse_short(word):
    reversed_text = word[::-1]
    print("reverse text", reversed_text)
    reversed_text = "".join(reverse_string(word))

    print (reversed_text)
    return reversed_text

def is_palindrome(word):
    reverse_word = word[::-1]
    flag = False
    print("reverse_word",reverse_word)
    print("word",word)
    if word.upper() == reverse_word.upper():
        flag =True
        return flag
    return flag

@pytest.mark.parametrize("word,expected",[("Otto",True)])
def test_is_palindrome(word,expected):
    assert is_palindrome(word) == expected  

def remove_duplicate(word):

    result = ""
    already_seen = set()

    for current_char in word:
        if not current_char.lower() in already_seen:
            already_seen.add(current_char.lower())
            result += current_char

    print(result)
    return result

def capitalise(word):
     title_word = word.title()

     print (title_word)
     return title_word 

def capitalise_some_words(words,expection):

    if len(expection)<0:
        raise ValueError("Enter a list of expetion")

    result =[]
    for word_ex in expection:
        for word in words:

            if word_ex.lower() == word.lower():
                result.append(word_ex.lower())
            result.append(word.upper())

    print (result)
    return result

def compare_len_strings(word_one,word_two):
    if len(word_one)>len(word_two):
        return True

    return False

@pytest.mark.parametrize("word_one,word_two,expected",[("ADFD","AB",True)])
def test_compare_len_strings(word_one,word_two,expected):
    assert compare_len_strings(word_one,word_two)==True

def print_tower(height):
    draw_top(height)
    draw_slices(height)
    draw_bottom(height)

def draw_top(height):
    print(" "*(height + 1) +'|')

def draw_bottom(height):
    print("-" *((height + 1) * 2 + 1))

def draw_slices(height):
    for i in range(height-1,-1,-1):
        value = height-i
        print("value",value)
        padding = i+1
        print("padding",padding)
        print(" " * padding + "#" * value + "|" + "#" * value)


if __name__ == "__main__":
    # binary_to_decimal("110")
    # hex_to_decimal("19")
    # separator_replace(["toto","mama"],"£££")
    # reverse_string("LOLITA")
    # reverse_short("AMO")
    # is_palindrome("Otto")
    # remove_duplicate("lalaLO")
    # capitalise("word in war")
    # capitalise_some_words(["this","is","my","word"],["is","my"])
    print_tower(4)



