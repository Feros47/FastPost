from FindPosts import createPostDict
from YoutubeUpload import main as youtube_upload
import os
from InstaUpload import instaUpload as cl
import time

def uploadInstaPosts(listDisct):
    reelsDict = listDisct
    for post in reelsDict:
        file_path = post['path']
        caption = post['description'] + ' '.join(['#' + "tag "])  # Adjust tags as needed
        # Call clip_upload with the correct parameters
        cl(file_path, caption)

def uploadYoutubePosts(listDict):
    shortsDict = listDict
    for post in shortsDict:
        file_path = post['path']
        caption = post['description']# + ' '.join(['#' + "tag "])  # Adjust tags as needed
        # Call youtube_upload with the correct parameters
        youtube_upload(file_path, caption)

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
    uploadYoutubePosts(listDict)
    time.sleep(120)
    movePosts(listDict, "posted")

uploadPosts(".", 1)
