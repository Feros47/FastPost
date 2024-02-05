import os 

listDict = []

def createPostDict(directory, listLenght):
    depth = 0
    for dirs in os.walk(directory, topdown=False):
        if depth == listLenght:
            depth = 0
            break
        for name in dirs[2]:
            if name.endswith(".md"):
                temp = {'path': name, 'description': name.replace(".md", "") + ' #tft '}
                listDict.append(temp)
    print(listDict)
    depth += 1
