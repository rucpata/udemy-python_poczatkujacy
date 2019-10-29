import os
import time

dir = input('Enter directory name: ')

if not os.path.isdir(dir):
    print('%s must be a directory' % dir)
else:
    file = input('enter filename saved in directory %s: ' % dir)

    path = os.path.join(dir, file)

    if not os.path.isfile(path):
        print('File %s does not exist!' % path)

    else:
        print('dispalying properties of file %s' % path)
        print('Last modyfied date' , time.localtime(os.path.getmtime(path)))
        print('Size in bytes ', os.path.getsize(path))
        print('Current directory is:' + os.getcwd())
        print('Relative path to the file is' + os.path.relpath(path))
        
