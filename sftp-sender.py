"""
This Script is intended to generate a class which will read a file and send it to a remote server
through SFTP, using a customizable Server address, user and password.
"""
import pysftp

class sftpManager:
    def __init__(self):
        self.hostName = ""
        self.userName = ""
        self.password = ""
        self.destinationPath = ""
        self.sourcePath = ""
    
    def sendFile(self):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        with pysftp.Connection(host=self.hostName, username=self.userName, password=self.password, cnopts=cnopts) as sftp:
            print("Connection succesfully stablished ...")
            
            sftp.put_r(self.sourcePath, self.destinationPath)
            
    
if __name__ == "__main__":
    sendFileSFTP = sftpManager()
    sendFileSFTP.sendFile()