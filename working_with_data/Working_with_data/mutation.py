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

word = "hello"
print('helo' in mutate(word))
print('cello' in mutate(word))
print('helol' in mutate(word))
