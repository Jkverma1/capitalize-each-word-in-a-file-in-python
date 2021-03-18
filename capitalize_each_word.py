# str "this is my first program"
f = open("file.txt","r")
content = f.read()
newcontent = content.split()
print(newcontent)
result = str()
for  i in newcontent:
    result+= i.capitalize()
    result+=" "
print(result)
f.close()
f = open("file.txt","w")
f.write(result)
    