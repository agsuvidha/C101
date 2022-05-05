import dropbox
class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.accessToken)

        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    accessToken='sl.BG73WFEFpu7Q-VXJ-7b1Bk2A8IYkACPGVr5RwWysUQbPl0ftBGJReO9JwycSu7yCajPWdG7EBb3Suqttkn_q1L-S2fpOJFwbVsYsfOFkzjaA-tn8jEpR-JHQTPUaj93L4CxtVqVjkBDT'
    transferData=TransferData(accessToken)

    file_from=input("Enter the file path to transfer ")
    file_to=input("Enter the full path to upload ")

    transferData.upload_file(file_from,file_to)
    print("File has been moved")


main()
