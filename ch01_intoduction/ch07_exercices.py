
import pytest

def the_longest_sequence(str1,str2):
    """The Longest sequence
    Args:
        values(str) : sequence to scan

    Returns:
        result(str)  : new list with the longuest sequence
    """

    return __lcs_helper(str1,str2,len(str1)-1,len(str2)-1)

def  __lcs_helper(str1,str2,pos1,pos2):
    # recursive termination
    if pos1< 0 or pos2<0:
        return ""

    if str1[pos1] == str2[pos2]:
        #recursive descent
        print("pos1",pos1)
        print("pos2",pos2)
        return __lcs_helper(str1,str2,pos1-1,pos2-1)+str1[pos1]
    else:
        # take away one of both letters and try it again but doe not belong to result
        lcs1 = __lcs_helper(str1,str2,pos1,pos2-1)
        lcs2 = __lcs_helper(str1,str2,pos1-1,pos2)

        print("lcs1",lcs1)
        print("lcs2",lcs2)
        return lcs1 if len(lcs1)>len(lcs2) else lcs2

if __name__ == "__main__":
    print(the_longest_sequence("ACGDFDGH","ABCDEFGLCV"))


        






