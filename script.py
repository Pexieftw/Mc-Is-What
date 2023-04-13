import re
with open('message.txt') as f:
	print("".join([chr(len(x)-2) for x in re.findall('M.*?C', f.read())]))