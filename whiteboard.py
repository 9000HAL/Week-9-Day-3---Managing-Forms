# A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

# First argument (required): the original string to be converted.
# Second argument (optional): a string of minor words that must always be lowercase except for the first word in the string.

#examples:
# title_case("thank goodness it is friday today","it is") => Thank Goodness it is Friday Today
# solution('a clash of KINGS', 'a an the of') => 'A Clash of Kings'
# solution('THE WIND IN THE WILLOWS', 'The In'),'The Wind in the Willows'


def solution(a_string, minor_words):
    split_string = a_string.split(" ")

    new_list = []
    new_list.append(split_string[0].capitalize())
    #print(split_string)

    for word in split_string[1:]:
        if word.lower() not in minor_words.lower().split(" "):
            word = word.capitalize()
            new_list.append(word)
        #print(word)
        else:
            new_list.append(word)

    #print(new_list)
    return " ".join(new_list)

print(solution("thank goodness it is friday today","it is"))








#gabe re-create whiteboard:



