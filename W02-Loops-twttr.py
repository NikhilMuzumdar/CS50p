tweet = input("Input: ")
vovels = ["a","e","i","o","u",]
output = ""

for l in tweet:
    if l.lower() in vovels:
        pass
    else:
        output += l

print(f"Output: {output}")

