import os
import zipfile

file=open('twitterData.sh', 'r')
lines = file.readlines()
file.close()

print(len(lines))
