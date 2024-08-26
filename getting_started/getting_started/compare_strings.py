def istrcmp(s1, s2):
    s1_up = s1.upper()
    s2_up = s2.upper()
    return s1_up==s2_up


print(istrcmp('python', 'Python'))
print(istrcmp('LaTeX', 'Latex'))
print(istrcmp('a', 'b'))
