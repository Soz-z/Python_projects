# Author: Daniel Clark
# Program to be called through commandline and point to a file
# Creates SHA256 and MD5 hashes of files
import hashlib
import sys

BufferSize = 65536 #read in 64kb chunks

md5 = hashlib.md5()
sha256 = hashlib.sha256()
with open(sys.argv[1], "rb") as f:
    while True:
        data = f.read(BufferSize)
        if not data:
            break
        md5.update(data)
        sha256.update(data)
print("MD5: {0}".format(md5.hexdigest()))
print("SHA256: {0}".format(sha256.hexdigest()))
