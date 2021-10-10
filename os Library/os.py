import os
from datetime import datetime

print("--------------------------------------------------------------------------------------------")

# print(dir(os)) Prints everything the os module can do

print(os.getcwd()) # Prints current working directory

os.chdir('C:/Users/suyog/Desktop/') # Change current working directory
print(os.getcwd())

print("--------------------------------------------------------------------------------------------")

print(os.listdir()) # Creates a list of all of the files in the current working directory 
os.chdir('C:/Users/suyog/Desktop/Coding Projects/Projects/Python Projects/os Library')

print("--------------------------------------------------------------------------------------------")

os.mkdir("OS-Folder") # Creates a folder in cwd

# If you need to make a directory a few levels deep, makedirs will make all of the intermediate directories
os.makedirs('OS-Folder-Make/SubDir')

# Delete folders, first will only delete specific folder, second will delete all intermediates
os.rmdir("OS-Folder")
os.removedirs('OS-Folder-Make/SubDir')

# Creating and deleting folders will not change the cwd

# Renaming files and folders in cwd
os.rename('text.txt', 'renamed.txt') # Original Name, New Name

# Find information about a specific file

print(os.stat('renamed.txt')) # Returns list of information about a file

print("--------------------------------------------------------------------------------------------")

print(os.stat('renamed.txt').st_size) # You can call the name of a piece of info on this for a specific one
# This returns the size of the file in bytes

modtime = (os.stat('renamed.txt').st_mtime) # Returns date modified
print(datetime.fromtimestamp(modtime))

os.rename('renamed.txt', 'text.txt')
print("--------------------------------------------------------------------------------------------")

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
     print('Current Path:', dirpath)
     print('Directories:', dirnames)
     print('Files:', filenames)


# Access home directory location by grabbing home environment variable
    # os.environ.get(‘HOME’). # Returns a path

# To properly join two files together use os.path.join()
    # file_path = os.path.join(os.environ.get(‘HOME’), ‘test.txt’)

# the benefit of os.path.join, is it takes the guess work out of inserting a slash


# os.path has other useful methods

os.path.basename
# This will grab filename of any path we are working on

    # os.path.dirname(‘/tmp/test.txt’)
# returns the directory /tmp

    # os.path.split(‘/tmp/test.txt’)
# returns both the directory and the file as a tuple

    # os.path.exists(‘/tmp/test.txt’)
# returns a boolean

    # os.path.isdir(‘/tmp/test.txt’)
# returns False

    # os.path.isfile(‘/tmp/test.txt’)
# returns True

    # os.path.splitext(‘/tmp/test.txt’)
# Splits file route of the path and the extension
# returns (‘/tmp/test’, ‘.txt’)
# This is alot easier than parsing out the extension. Splitting off and taking the first value is much better.
# Very useful for file manipulation
