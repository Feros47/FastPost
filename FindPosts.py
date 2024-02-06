import os 


def createPostDict(directory, listLength):
    listDict = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(".mp4"):
                if len(listDict) < listLength:
                    temp = {'path': os.path.join(root, name), 'description': name.replace(".mp4", "") + ' #tft '}
                    listDict.append(temp)
                else:
                    return listDict
    return listDict