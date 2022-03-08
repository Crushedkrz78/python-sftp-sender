"""
This Script is intended to generate a class which will read a file and send it to a remote server
through SFTP, using a customizable Server address, user and password.

Note: Sending files from a Windows host to a Unix/linux host using recursively methods, may cause
that the destination file name is mixed with path string and file stored not exactly where intended.
"""
import pysftp

class sftpManager:
    def __init__(self):
        self.hostName = ""
        self.userName = ""
        self.password = ""
        self.destinationPath = ""
        self.sourcePath = ""
        self.rsa_key = ""
    
    def sendFile(self):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        #with pysftp.Connection(host=self.hostName, username=self.userName, private_key=self.rsa_key, cnopts=cnopts) as sftp:
        with pysftp.Connection(host=self.hostName, username=self.userName, password=self.password, cnopts=cnopts) as sftp:
            print("Connection succesfully stablished ...")
            
            #Send all files and dirs recursively from a local path to a remote path 
            sftp.put_r(self.sourcePath, self.destinationPath)
            
            
    
if __name__ == "__main__":
    sendFileSFTP = sftpManager()
    sendFileSFTP.sendFile()