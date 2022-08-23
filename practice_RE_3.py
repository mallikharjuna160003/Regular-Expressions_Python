import re
#grouping and conditions
test_string = """
Mr Simpson
hello world
1223
2020-05-20
Mrs Simpson
Mr. Brown
Ms Smith
Mr.
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""

#pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s\w+')
pattern = re.compile(r'([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)')
matches = pattern.finditer(test_string)
for match in matches:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
