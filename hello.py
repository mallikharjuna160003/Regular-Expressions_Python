import re

test_string = "123abc456789abc123ABC"

# pattern = re.compile(r"abc")
# matches = pattern.finditer(test_string)

matches = re.finditer(r"abc",test_string)
for match in matches:
    print(match)
