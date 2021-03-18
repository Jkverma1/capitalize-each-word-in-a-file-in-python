# str "this is my first program"
f = open("file.txt","r")
content = f.read()
content = content.split()
result = str()
for  i in content:
    result+= i.capitalize()
    result+=" "
print(result)
f.close()
f = open("file.txt","w")
f.write(result)
    
