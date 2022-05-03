with open('my_file.txt') as fh:
    text = fh.read()
    count = 0
    for line in text:
        for word in line:
            if word.isupper():
                count +=1
            else:
                count += 0
    print(count)