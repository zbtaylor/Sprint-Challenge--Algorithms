'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # while letters remain
    if len(word) > 0:
        # look for bigram "th"
        if word[:2] == "th":
            # if found, add 1 and recursively call count_th,
            # passing in word[2:] to remove the 'th' from the string
            return 1 + count_th(word[2:])
        else:
            # if not found, add 0 and recursively call count_th,
            # passing in  word[1:] to remove the first letter from the string
            return 0 + count_th(word[1:])
    # add 0 when no letters remain
    else:
        return 0
