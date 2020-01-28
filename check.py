def check_name():
    print("Enter the name to be searched in the File: ")
    name = input()
    name1= name.lower()
    file = open(r"D:\Sharv\JAVA\\1.txt", 'r')
    read = file.readlines()
    file.close()
    isname = False
    for i in read:
        L = i.split()
        y = len(L)
        for i in range(y):
            word = L[i].lower()
            if name1 == word:
                isname = True




    if isname :
        print("Entered name is present in the file")
    else:
        print("Name entered not present in the file")


