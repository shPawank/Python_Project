#Regular Expressions in python

import re
pattern= r"expression"
text="The cat is in the hat."

matches=re.findall(pattern, text)

print(matches)