import re

def make_slug(name):
    slug = re.sub(r'[^\w\s-]', '', name) 
    slug = re.sub(r'[-\s]+', '-', slug)   
    slug = slug.strip('-')
    return slug

print(make_slug("hello world"))
print(make_slug("hello  world!"))
print(make_slug(" --hello-  world--"))
