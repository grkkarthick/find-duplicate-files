import os
import hashlib
import sys

folderPath = raw_input('Enter the directory name: ')
csvFile = raw_input('Enter the result csv file name: ')

if not os.path.isdir(folderPath):
    print 'Folder path: "{0}" is incorrect'.format(folderPath)
    sys.exit(1)

def IterateFiles(folderPath, recursive = False):
    if recursive:
        for folder in IterateFolders(folderPath):
            for file in IterateFiles(folderPath = folder):
                yield file
    else:
        for file in os.listdir(folderPath):
            if os.path.isfile(os.path.join(folderPath, file)):
                yield os.path.join(folderPath, file)

def IterateFolders(folderPath):
    for folders in os.walk(folderPath):
        yield folders[0]

def ChecksumMd5(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(100 * 1024 * 1024), b''):
            md5.update(chunk)
    return md5.hexdigest()

with open(csvFile, 'w') as csvFile:
    with open('error.log', 'w') as logFile:
        print "Running....."
        hashTable = {}
        duplicateTable = {}
        csvFile.write('{0},{1},{2}\n'.format('hash', 'file', 'size\n'))
        for file in IterateFiles(folderPath, True):
            with open(file, 'rb') as ipFile:
                checksum = ChecksumMd5(file)
                if checksum not in hashTable:
                    hashTable[checksum] = [file]
                else:
                    if checksum not in duplicateTable:
                        duplicateTable[checksum] = hashTable[checksum]
                    duplicateTable[checksum].append(file)

        for key, value in duplicateTable.items():
            try:
                csvFile.write('"{0}","{1}","{2}"\n'.format(key, '\n'.join(value), os.path.getsize(value[0])))
            except:
                logFile.write('Error while processing file hash: {0} ----- names:'.format(key))
                for index, fileName in enumerate(value):
                    if isinstance(value[index], str):
                        value[index] = fileName.encode('string-escape')
                    elif isinstance(value[index], unicode):
                        value[index] = fileName.encode('unicode-escape')
                logFile.write('|\t|'.join(value))
                logFile.write('\n')

        print "Completed....."
