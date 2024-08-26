def count_word(filename):
    word_count = {}
    words=open(filename).read()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1    
    return word_count
def sorted_count(word_count):
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1])
    return sorted_word_count
filename = 'C:\\Users\\yedhu\\OneDrive\\Desktop\\new.txt'
print(count_word(filename))
print(sorted_count(count_word(filename)))

