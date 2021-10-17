def addToArrayForm(kl,num):
    s=[str(i) for i in kl]
    new=int("".join(s))

    m=new+num
    print(m)
    ls=[int(i) for i in str(m)]
    return(ls)

kl = [1,2,0,0]
num= 34

print(addToArrayForm(kl,num))