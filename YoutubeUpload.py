from youtube_upload.client import YoutubeUploader

uploader = YoutubeUploader(secrets_file_path="client_secrets.json")

uploader.authenticate()