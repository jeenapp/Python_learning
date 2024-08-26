def find_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return anagram_dict

words = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
print(find_anagrams(words).values())

