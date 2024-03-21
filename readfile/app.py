try: 
    f = open("chinh.txt", "r") 
    # list_content = f.read()
    list_content = f.readlines()
    print(type(list_content))
    i = 1
    for content in list_content: 
        print(str(i) + " : " + content)
        i+=1
    # print(content)
    # --> read file
    # f = open("chinh.txt", "a")
    #--> write file(appending)
    # f.write("Write file with Python 2!\n")
    # f.write("Write file with Python 3!\n")
    # f.write("Write file with Python 4!")
    
    # print(f.read())
except Exception as e:
    print(e)
finally:
    f.close()