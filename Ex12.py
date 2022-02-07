import re
hand = open("mbox.txt")
nline = 0
for line in hand :
    line = line.rstrip()
    if re.search('^F.+:?', line) :
        nline = nline + 1
print("Number of email is", nline)

