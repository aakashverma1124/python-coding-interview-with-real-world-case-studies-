from typing import List, Tuple
from collections import defaultdict

class Pair:
    def __init__(self, index: int, word: str):
        self.index = index
        self.word = word

class PossibleMatches:
    def __init__(self):
        self.character_map = defaultdict(list)

    def find_possible_matches(self, S: str, words: List[str]) -> int:
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            self.character_map[ch] = []

        for word in words:
            self.character_map[word[0]].append(Pair(0, word))

        num_of_students = 0
        for index in range(len(S)):
            lst = self.character_map[S[index]]
            self.character_map[S[index]] = []
            for pair in lst:
                if pair.index + 1 == len(pair.word):
                    num_of_students += 1
                else:
                    pair.index += 1
                    self.character_map[pair.word[pair.index]].append(pair)

        return num_of_students

if __name__ == "__main__":
    # Driver code
    pm = PossibleMatches()
    plagiarised = "abcde"
    students = ["a","bb","acd","ace"]
    print(f"The content was copied from {pm.find_possible_matches(plagiarised, students)} students")

    plagiarised = "dsahjpjauf"
    students = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    print(f"The content was copied from {pm.find_possible_matches(plagiarised, students)} students")