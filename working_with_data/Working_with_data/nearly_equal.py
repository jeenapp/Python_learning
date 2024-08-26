def mutate(word):
    mutations = set()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(word) + 1):
        for char in letters:
            mutated_word = word[:i] + char + word[i:]
            mutations.add(mutated_word)
    for i in range(len(word)):
        mutated_word = word[:i] + word[i+1:]
        mutations.add(mutated_word)
    for i in range(len(word)):
        for char in letters:
            if word[i] != char:
                mutated_word = word[:i] + char + word[i+1:]
                mutations.add(mutated_word)
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            mutated_word = word[:i] + word[i + 1] + word[i] + word[i + 2:]
            mutations.add(mutated_word)    
    return list(mutations)
def nearly_equal(a,b):
    print(b in mutate(a))
nearly_equal('python', 'perl')
nearly_equal('perl', 'pearl')
nearly_equal('python', 'jython')
nearly_equal('man', 'woman')
