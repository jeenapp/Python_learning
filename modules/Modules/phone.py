import re

pattern = re.compile(r'^(?:\+91[-.\s]?)?(?:91[-.\s]?)?\d{10}$')
number = "9074733523"
if pattern.match(number):
    print("valid")
else:
    print("invalid")

