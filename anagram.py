from typing import List


def find_anagrams(word: str, candidates: List) -> List:
    """Return a list of anagrams for a word based on a list of potential candidate words."""
    anagrams = []
    word_list = (list(word.lower()))
    lower_candidates = [i.lower() for i in candidates]

    for k in range(0, len(lower_candidates)):
        lst = list(lower_candidates[k])
        lst.sort()
        word_list.sort()
        if lst == word_list and word.lower() != candidates[k].lower():
            anagrams.append(candidates[k])

    return anagrams
