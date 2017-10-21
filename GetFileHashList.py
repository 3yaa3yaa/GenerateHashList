'''
Created on Oct 1, 2017
@author: nobuy
'''

import os
import sys
import datetime
import hashlib
import socket


def getFileTimeStamp(path):
    dt = datetime.datetime.fromtimestamp(os.stat(path).st_mtime)
    return dt.strftime("%Y-%m-%d %H:%M:%S")
    
def getFileHash(path):
    return hashlib.md5(path).hexdigest()

def getFileSize(path):
    size=os.path.getsize(path)
    return str(size)
    
def generateFileName():
    hostname=socket.gethostname()
    now=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    cwd=os.getcwd()
    return (os.path.join(cwd,"FileList_" + hostname + now + ".csv"))
    
def writeLsrResult(directory):
    filename=generateFileName();
    f=open(filename,'w')
    for file in lsr(directory):
        dir,name=os.path.split(file);
        line= dir  + "," + name + ","+ getFileTimeStamp(file)+","+ getFileSize(file)+","+ getFileHash(file)+ "\r\n"
        f.write(line)
    f.close()

def writeLsrResultOfCurrentDir():
    cwd=os.getcwd()
    writeLsrResult(cwd)
    
        
def lsr(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


if __name__ == '__main__':
    print("Start collecting file list...");
    args = sys.argv
    path=""
    try:
        path=args[1]
    except:
        None
        
    if os.path.exists(path): 
        writeLsrResult(path)
    else:
        writeLsrResultOfCurrentDir()
    print("End collecting file list!");
    

