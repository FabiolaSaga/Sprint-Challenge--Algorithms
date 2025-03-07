'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    char1 = 't'
    char2 = 'h'

    if len(word) <= 1:
        return 0

    if word[0] == char1:
        if word[1] == char2:
            return 1 + count_th(word[2:])

    return count_th(word[1:])
