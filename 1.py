fail = open("new_f.txt", 'a')
while True:
    string = input()
    if string == '':
        break
    fail.write(string + "\n")
fail.close()
