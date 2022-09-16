import pytest

def reverse_string(text):
    # recursive termination
    if len(text) <=1:
        return text

    first_char = text[0]
    print("Frist char",first_char)
    remaining = text[1:]
    print("Remaining",remaining)
    # recursive descent
    return reverse_string(remaining) + first_char

def reverse_string_short(text):
    return text if len(text) <=1 else reverse_string_short(text[1:]) +text[0]

def count_substrings(text, value_to_find):
    if len(text) < len(value_to_find):
        return 0

    count=0
    remaining=""

    # does the text start with the search string?
    if text.startswith(value_to_find):
        # match : continue the search for the found
        # term after the location where it was found
        remaining = text[len(value_to_find):] 
        print("TOTO  ",remaining)
        count = 1

    else:
        # remove first character and search again
        remaining = text[1:]
        print("TATA  ",remaining)

    # recursive descent

    return count_substrings(remaining,value_to_find)+ count

def count_substring_short(text,value_to_find):
    return 0 if len(text) < len(value_to_find) else \
        (1 if text.startswith(value_to_find) else 0) + \
            count_substring_short(text[1:],value_to_find)


if __name__ == "__main__":
    count_strings =count_substring_short("hahpddpffsfpfsfsdfpf", "pf")
    print(count_strings)



