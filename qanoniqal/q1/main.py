# from collections import Counter
# c = Counter(['eggs', 'palms'])
# print(c['bcon'])

from typing import List, Optional


def solve(input: str) -> Optional[List[str]]:
    dictionary = []
    lines_input = input.split('\n')
    for line in lines_input:
        words_list = line.split(' ')
        dictionary += words_list
    print(dictionary)
    return None


test = """ladder came tape soon leader acme RIDE lone Dreis peat
ScAlE orb eye Rides dealer NotE derail LaCeS drIed
noel dire Disk mace Rob dries"""
# solve(test)


def word_possibles(word):
    out_put = []
    letters = [letter for letter in word]
    for i in range(len(word)):
        possible = letters.pop(i) + ''.join(letters)
        out_put.append(possible)
        letters = [letter for letter in word]
    return out_put


print(word_possibles('the'))


