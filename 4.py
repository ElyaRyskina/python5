from translate import Translator
translator= Translator(from_lang="english",to_lang="russian")


with open("file4.txt", encoding='utf-8') as file:
    text = file.readlines()
    for i in text:
        string = i.split()
        name = string[0]
        print(name)
        name = translator.translate(name)
        print(name)
        with open("file4a.txt", "a", encoding='utf-8') as file2:
            file2.write(name + string[1] + string[2]+ "\n")
