import re


# Check to see if two provided strings are anagrams of eachother. One string is an anagram
# of another if it uses the same characters in the same quantity. Only consider characters,
# not spaces or punctuation. Consider capital letters to be the same as lower case
def anagrams(str1, str2):
    """ simple, including special characters """
    return sorted(str(str1).lower()) == sorted(str(str2).lower())


def anagrams_no_special_chars(str1, str2):
    """ no special characters """
    str1 = re.sub('[^a-zA-Z]+', '', str1.lower())
    str2 = re.sub('[^a-zA-Z]+', '', str2.lower())
    return sorted(str1) == sorted(str2)


# Given a string, return true if the string is a palindrome or false if it is not.
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


# Given an integer, return an integer that is the reverse ordering of numbers.
def reverse_int(num):
    return int(str(num)[::-1])


# Given a string, return the character that is most commonly used in the string.
def find_common_char_simple_way(sentence):
    str(sentence)
    common_char = ""
    count = 0
    for char in sentence:
        if sentence.count(char) > count:
            common_char = char
            count = sentence.count(char)
    return [common_char, count]


def fizz_buzz(max_range):
    fizz = "Fizz"
    buzz = "Buzz"

    for n in range(1, max_range + 1):
        if n % 15 == 0:
            print(fizz + buzz)
        elif n % 3 == 0:
            print(fizz)
        elif n % 5 == 0:
            print(buzz)
        else:
            print(n)


# Given an array and chunk size, divide the array into many subarrays where each subarray is of length size
def array_chunking(arr, size):
    chunked = []
    for i in range(0, len(arr), size):
        chunked.append(arr[i:i + size])
    return chunked


# Write a function that accepts a positive number N. The function should console log
# a step shape with N levels using the # character.
def staircase_left(step):
    for stairs in range(1, step + 1):
        print('#' * stairs)


def staircase_right(step):
    for stairs in range(1, step + 1):
        print(' ' * (step - stairs) + '#' * stairs)


# Write a function that returns the number of vowels used in a string.
# Vowels are the characters 'a', 'e', 'i', 'o', and 'u'.
def vowels_counter(string):
    """with loop"""
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char in vowel:
            count += 1
    return count


def vowels_counter_regex(string):
    """with regex"""
    vowels = re.findall('[aeiou]', string, re.IGNORECASE)
    return len(vowels)


# Write a function that accepts a string. The function should capitalize the first letter
# of each word in the string then return the capitalized string.
def capitalize(string):
    return string.title()


# Given a string, return a new string with the reversed order of characters
def reverse_string(string):
    return string[::-1]


# Print out the n-th entry in the fibonacci series.
def fibonacci(num, a=0, b=1, sequence=[]):
    if b < num:
        sequence.append(b)
        a, b = b, a + b
    else:
        return sequence
    return fibonacci(num, a, b, sequence)
