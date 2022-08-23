import re

# split, sub
test_string = "123abc456789abc123ABC"
pattern = re.compile(r'123')
splitted = pattern.split(test_string)
print(splitted)

