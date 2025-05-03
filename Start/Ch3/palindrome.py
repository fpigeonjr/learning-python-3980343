# Your task: Return a Boolean True or False value, indicating whether the string is a palindrome. A palindrome is a string that reads the same forward and backward, ignoring spaces, capitalization, and punctuation
import string

def remove_puctuation(string_in):
    return string_in.translate(string_in.maketrans('', '', string.punctuation))

def isPalindrome(teststr):
    if not (teststr.isalnum):
        return print('palindromes are not alpha numberical')

    lowerstring = teststr.lower().replace(" ", "")
    reversed_teststr = teststr.lower().replace(" ", "")[::-1]
    stripped_string = remove_puctuation(lowerstring)
    stripped_reverse_str = remove_puctuation(reversed_teststr)

    print(f'{stripped_string} is equal to {stripped_reverse_str}')
    if stripped_string == stripped_reverse_str:
        return True
    else:
        return False

print(isPalindrome("M81273498234 (*^%^"))
print(isPalindrome("tacocat"))
print(isPalindrome("Madam, I'm Adam."))
