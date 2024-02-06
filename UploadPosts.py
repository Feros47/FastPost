from instagrapi import Client
from FindPosts import createPostDict
import os
import time

cl = Client()
cl.login("Lucidityy4", "Cdu79wqs.123")


def uploadInstaPosts(listDisct):
    reelsDict = listDisct
    for post in reelsDict:
        file_path = post['path']
        # Assuming you want to include tags as hashtags in the caption
        caption = post['description'] + ' '.join(['#' + "tag "])  # Adjust tags as needed
        # Call clip_upload with the correct parameters
        cl.clip_upload(file_path, caption)
    time.sleep(10)
    movePosts(reelsDict['path'], "posted")

from instagrapi import Client
from FindPosts import createPostDict
import os
import time

cl = Client()
cl.login("Lucidityy4", "Cdu79wqs.123")


def uploadInstaPosts(listDisct):
    reelsDict = listDisct
    for post in reelsDict:
        file_path = post['path']
        # Assuming you want to include tags as hashtags in the caption
        caption = post['description'] + ' '.join(['#' + "tag "])  # Adjust tags as needed
        # Call clip_upload with the correct parameters
        cl.clip_upload(file_path, caption)
    time.sleep(3)
    movePosts(reelsDict, "posted")

def movePosts(listDict, directory):
    for post in listDict:
        try:
            new_path = directory + "/" + post['path'].split("/")[-1]
            os.rename((post['path']), new_path)
        except Exception as e:
            print(f"Error moving {post['path']} to {new_path}: {e}")



def uploadPosts(directory, listLength):
    listDict = createPostDict(directory, listLength)
    uploadInstaPosts(listDict)

uploadPosts(".", 1)
