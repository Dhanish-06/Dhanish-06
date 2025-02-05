f = open("C:\\Users\\D6\\Desktop\\Startup\\git programs\\wordcount.txt", "r")
data = f.read()
f.close()

word_list = data.split()
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1


for key, value in word_count.items():
    print(f"{key} occurs : {value}")
