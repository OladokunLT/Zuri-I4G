def read_file(filename):
    open_file = open(filename, "r")
    readfile = open_file.read()
    # print(readfile)
    #split_text = readfile.split()
    # count = {}
    # for i in split_text:
    #     if i in count:
    #         count[i]  += 1
    #     else:
    #         count[i] = 1 
    # print (count)
    return readfile

def count_content ():
    text = read_file("story.txt")
    text.split()
    count = {}
    for i in text.split():
        # print (count[i])
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print (count)
count_content()