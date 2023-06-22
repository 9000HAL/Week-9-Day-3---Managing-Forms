# A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

# First argument (required): the original string to be converted.
# Second argument (optional): a string of minor words that must always be lowercase except for the first word in the string.

#examples:
# title_case("thank goodness it is friday today","it is") => Thank Goodness it is Friday Today
# solution('a clash of KINGS', 'a an the of') => 'A Clash of Kings'
# solution('THE WIND IN THE WILLOWS', 'The In'),'The Wind in the Willows'


def solution(a_string, minor words):
    split_string - a_string.split(" ")
    for word in 