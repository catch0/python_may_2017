list=['dallas','Texas',30,40]
newstring=''
runsum=0
for i in list:
    print type(i)
    if type(i)==str:
        newstring+=str(i)
    elif type(i)==int:
        runsum=runsum+i
print (newstring)
print (runsum)
        