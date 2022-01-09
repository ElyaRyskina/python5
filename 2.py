file = open('file2.txt', "r")
text = file.readlines()
print(len(text))
for i in range(0, len(text)):
    string = text[i]
    string = string.split()
    print(len(string))
fail.close()


