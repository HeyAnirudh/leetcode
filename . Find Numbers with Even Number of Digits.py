#lt=[12,12,333,1234,34545]
#print(len(str(lt[2])))
def findNumbers(lt):
    count=0
    for i in range(0,len(lt)):
        if len(str(lt[i]))%2==0:
            count+=1
    return count
lt=[12,345,2,6,7896]
print(findNumbers(lt))