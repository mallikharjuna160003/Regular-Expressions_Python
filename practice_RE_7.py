import re

urls = """

http://python-engineering.com
https://www.python-engineer.com
http://www.pyeng.net
"""
pattern = re.compile(r"https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)")
#matches = pattern.finditer(urls)
#for match in matches:
#    print(match.group())
#    print(match.group(1))

#\2 \3 are backreference groups in numeric way!!..
subbed_urls = pattern.sub(r"\2\3",urls)
print(subbed_urls)
