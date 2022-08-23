import re



""" Task 9
test_string = "hello 123"
#pattern = re.compile(r'[_?\d]')
pattern = re.compile(r'\d{1,3}')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
"""


""" Task 8
test_string = "hello 123_ heyho hohey"
pattern = re.compile(r'[a-zA-Z0-9]')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
"""

""" Task 7

test_string = "123abc4567abc123ABC."
pattern = re.compile(r'^123') #begins with
matches = pattern.finditer(test_string)
# group, start, end, span
for match in matches:
    print("Span:",match.span(),"Start:", match.start(),"End:", match.end(),"Group:",match.group())
    
test_string = "123abc4567abc123ABC."
pattern = re.compile(r'ABC$') #ends with
matches = pattern.finditer(test_string)
# group, start, end, span
for match in matches:
    print("Span:",match.span(),"Start:", match.start(),"End:", match.end(),"Group:",match.group())
"""

""" Task 6
test_string = "123abc4567abc123ABC."
pattern = re.compile(r'.') # "\." for "."
matches = pattern.finditer(test_string)
# group, start, end, span
for match in matches:
    print("Span:",match.span(),"Start:", match.start(),"End:", match.end(),"Group:",match.group())
"""


""" Task 5
test_string = "123abc4567abc123ABC"
pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)
# group, start, end, span
for match in matches:
    print(match.span(), match.start(), match.end(),match.group())

"""


""" Task 4
test_string = "123abc4567abc123ABC"
pattern = re.compile(r'abc')
matche = pattern.search(test_string)
#match(), search(), findall()
print(matche)
"""

""" Task 3
test_string = "123abc4567abc123ABC"
pattern = re.compile(r'123')
match = pattern.match(test_string)
#match(), search(), findall()
print(match)
# outputs the find starting match
"""

""" Task 2
test_string = "123abc4567abc123ABC"
pattern = re.compile(r'abc')
matches = pattern.findall(test_string)
#finds all the match sub-strings and make a list
#match(), search(), findall()
for match in matches:
    print(match)

"""

""" Task 1
test_string = "123abc4567abc123ABC"
pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)
#match(), search(), findall()
for match in matches:
    print(match)
output:
two match objects
"""
