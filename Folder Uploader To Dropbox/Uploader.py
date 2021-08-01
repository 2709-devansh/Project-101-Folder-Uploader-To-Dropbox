import os
import dropbox
from dropbox.files import WriteMode

class transferFolder:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFolder(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode = WriteMode("overwrite"))

def main():
    access_token = "J-NSQ0t_clYAAAAAAAAAAQHuM6D8yymMDg4_c3Scte0lbmFm1Kqv06jwMwA9zGVo"
    transferData = transferFolder(access_token)

    file_from = input("Enter the path of the file to be moved: ")
    file_to = input("Enter Where the file should be moved: ")

    transferData.uploadFolder(file_from, file_to)   
    print("Folder Transferred Succesully!")

main()
