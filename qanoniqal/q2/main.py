from typing import List, Optional
import itertools


def word_possibles(word):
    """to generate a list of the different possibilities of a given word"""
    letters = [letter for letter in word]
    possibles = [''.join(list(possible_word)) for possible_word in itertools.permutations(letters)]
    return list(set(possibles))


def solve(input: str) -> Optional[List[str]]:
    out_put = []
    domain_dictionary = []
    lines_input = input.split('\n')
    for line in lines_input:
        words = line.split(' ')
        domain_dictionary += words
    lower_domain_dictionary = [dict_word.lower() for dict_word in domain_dictionary]
    for word_item in domain_dictionary:
        count = 0
        possibles = word_possibles(word_item)
        for i in possibles:
            if i.lower() in lower_domain_dictionary:
                count += 1
        if count == 1:
            out_put.append(word_item)
    return sorted(out_put)


test = """ladder came tape soon leader acme RIDE lone Dreis peat
ScAlE orb eye Rides dealer NotE derail LaCeS drIed
noel dire Disk mace Rob dries"""

print(solve(test))
