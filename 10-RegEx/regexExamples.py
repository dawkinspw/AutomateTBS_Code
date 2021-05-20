import re

batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search('The Adcentures of Batwoman')

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 666-555-5555')


print(mo.group())