'''
filename = input('Enter filename: ')

print('the file name is: %s' %(filename))
'''

while True:
    
    filesizeStr = input('Enter the max file size (MB): ')

    if filesizeStr.isdecimal():
        filesizeInt = int(filesizeStr)
        break
    
print('The max size is %d' %(filesizeInt))
print('Size is KB is %d' % (filesizeInt * 1024))
