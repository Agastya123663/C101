import dropbox

class Transferdata:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'RCw8DI9UbxYAAAAAAAAAARrUV0-pjn3xuZicw-A2XPjsM5bfFCddUvJkaEjX9tMt'
    transferdata = Transferdata(access_token)
    
    file_from = input('Enter the file path to transfer : ')
    file_to = input('Enter the full path to upload the file to the dropbox : ')

    transferdata.upload_file(file_from,file_to)
    print('File has been moved !')

main()
