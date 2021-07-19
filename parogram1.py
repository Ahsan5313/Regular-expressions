import re

pattern = r"color"
if re.match(pattern, "color and my favourite color is red"):
    print('Match')

else:
    print('Not Match')

if re.search(pattern, 'i am color and my favourite color is red'):
    print('Match')

else:
    print('Not Match')

print(re.findall(pattern, 'I am form color and my favourite color is re'))
