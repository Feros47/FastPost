from tiktok_uploader.upload import upload_videos
from tiktok_uploader.auth import AuthBackend
from FindPosts import createPostDict


def uploadPosts(directory, listLenght):
    auth = AuthBackend(cookies="cookies.txt") 
    upload_videos(auth, createPostDict(directory, listLenght))   

    failed_videos = upload_videos(videos=createPostDict(directory, listLenght), auth=auth)
    for video in failed_videos: 
        print(f'{video["video"]} with description "{video["description"]}" failed')

uploadPosts(".", 2)
