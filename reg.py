import re
pattern = 'A'
string = "A00"
match = re.match(pattern,string)
if match:
    print("Successfull")
