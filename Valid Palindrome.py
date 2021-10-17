s = "race a car"
char='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
ne=s
def palin(str):
    global char
    global ne
    for i in char:
        if i in ne:
            ne=ne.replace(i,"")

    if ne.lower()==ne[::-1].lower():
        return "true"
    else:
        return "false"
print(palin(s))