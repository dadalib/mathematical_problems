import math
from unittest import result
import pytest
import sys


def find_common(values1,values2):
    results = {}
    populate_from_collection1(values1,results)
    mark_if_also_in_second(values2,results)

    return remove_all_just_in_first(results)

def  populate_from_collection1(values1,results):
    for elem1 in values1:
        print("elem1",elem1)
        results[elem1] = 1
        print("results1",results)

def mark_if_also_in_second(values2,results):
    for elem2 in values2:
        if elem2 in results:
            print("elem2",elem2)
            results[elem2] +=1
            print("results2",results)

def remove_all_just_in_first(results):
    final_result = set()
    for key, value in results.items():
        if value >= 2:
            final_result.add(key)

    print(final_result)
    return final_result

def find_common_short(values1,values2):
    print(set(values1).intersection(values2))
    return set(values1).intersection(values2)

class Stack:
    def __init__(self):
        self.__values = []

    def push(self,elem):
        self.__values.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackIsEmptyException()

        return self.__values.pop()

    def peek(self):
        if self.is_empty():
            raise StackIsEmptyException()

        return self.__values[-1]

    def is_empty(self):
        return len(self.__values)==0 

    def list_words(self):
        return self.__values

    

class StackIsEmptyException(Exception):
    pass

def reverse_values(values):
    revers_list = values[::-1]
    print(revers_list)
    return revers_list

def reverse_long(values):

    result =[]
    
    for i in range(len(values)-1,-1,-1):
        # start at the l ast position
        result.append(values[i])
    return result

def remove_duplicates(values):
    result = []
    found_numbers = set()

    for elem in values:
        if elem not in found_numbers:
            found_numbers.add(elem)
            print("found numbers",found_numbers)
            result.append(elem)

    return result

def longest_sequence(values):
    if len(values) == 0:
        return values
    
    longest =(0,0)
    start_current =0
    end_curent = 0

    for end_current in range(1,len(values)):
        print("range", range(1,len(values)))
        print("for end_current",end_current )
        print("values[end_curent]",values[end_curent])
        print("values[end_curent -1]",values[end_curent-1])
        print("=======================")
        if values[end_curent] < values[end_curent-1]:
            print("range", range(1,len(values)))
            print("for end_current",end_current )
            print("values[end_curent]",values[end_curent])
            print("values[end_curent -1]",values[end_curent-1])
            print("/////////////////////////////////")
            if end_curent - start_current > len(longest):
                longest = (start_current, end_current)
                print("longest",longest)
                print("start_current",start_current)
            start_current = end_current
            print("start_current,end_current",start_current)

    if end_current - start_current > len(longest):
        longest = (start_current, end_current)
        print("the longest",longest)

    
    
    print( values[longest[0] : longest[1]])
    return values[longest[0] : longest[1]]

def pascal(n):
    result =[]
    __pascal_helper(n,result)
    return result

def __pascal_helper(n,results):
    if n == 1:
        results.append([1])
    else:
        # recursive descent
        print("n-1",n -1)
        print("results",results)
        previous_line = __pascal_helper(n -1,results)
        print("Prev line",previous_line )

        # calculate based on previous line
        current_line = __calc_line(previous_line)
        results.append(current_line)
        print("HERE")
        print("Results", results)


    return results[n-1]

def __calc_line(previous_line):
    current_line = [previous_line[i] + previous_line[i + 1]
                    for i in range(len(previous_line) - 1)]

    print("Current line",current_line)
                    

    return [1] + current_line + [1]

def print_pascal(n):
    for line in pascal(n):
        print(line)

def list_add(values1,values2):
    result = []
    carry = 0

    for i in range(len(values1)-1,-1,-1):
        print(values1[i])
        print(values2[i])
        sum = values1[i] + values2[i] + carry
        print("Sum",sum%10)
        result.insert(0, sum % 10)

        carry = 1 if sum >= 10 else 0

    # add a 1 at the front of a carryover
    if carry == 1:
        # aad it first
        result.insert(0, 1)


    return result

def reverse_list_values(values):
    reverse_list = values[::-1]
    return reverse_list

def merge_values(values1,values2):
    """Merging two list values in an ascending """
    sort_value1 = sorted(values1)
    sort_values2 =  sorted(values2)
    merge_list = sorted(sort_value1 + sort_values2)
    return merge_list 

def merge_values_long(values1,values2):
    pos1 =0
    pos2 =0
    result = []

    while pos1 < len(values1) and pos2 < len(values2):
        value1 = values1[pos1]
        value2 = values2[pos2]

        if value1 < value2:
            result.append(value1)
            pos1+=1

        else:
            result.append(value2)
            pos2+=1
    
    return

def generate_following_values(current_value,sequence_length):
    result = []
    predefined_values =  ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]

    if type(current_value) == int():

        while sequence_length > 0:
            result.append(current_value)
            current_value +=1
            sequence_length -=1

        return result
    else:
        
        while sequence_length >0:
            for index,day in enumerate(predefined_values):
                if current_value == day:
                    print("day",day)
                    result.append(day)
                    sequence_length-=1
                elif current_value != day and len(result)!=0:
                    result.append(predefined_values[index])
                    sequence_length-=1
        return result







if __name__ =="__main__" : 
    # find_common_short([1,2,3,4,52],[1,7,52])
    # stack = Stack()
    # stack.push("first")
    # print("PEEK : " + stack.peek())
    # stack.push("second")
    # stack.push("three")
    # print("POP : " + stack.pop())
    # print("ISEMPTY: " + str(stack.is_empty()))
    # print("List of words"+str(stack.list_words()) )
    # reverse_values([1,45,3])
    # reverse_long([1,45,3])
    # print(remove_duplicates([1,2,3,3,4,5]))
    # print(print_pascal(6))
    # sum_list = list_add([1, 2, 3], [4, 5, 6])
    # print( sum_list)
    # print(reverse_list_values(sum_list))
    # print(merge_values([4,20,12],[1,2,9,3]))
    # print(generate_following_values("FRIDAY",3))
    print(generate_following_values("Friday",6))


