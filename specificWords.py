for line in open("demo.txt"):
    for word in line.split():
        if(word.endswith('ing')):
            print(word)
