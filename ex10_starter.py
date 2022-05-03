import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

for name in glob.glob(pattern):
    file_size = os.path.getsize(name)
    print(name, file_size)

# TODO: Use the glob.glob() function to obtain the list of filenames
# for name in glob.glob('/Users/getintotech/*'):
#     file_size = os.path.getsize(name)
#     print(name, file_size)
#
# # TODO: use os.path.getsize to find each file's size
#
# # TODO: Add a test to only display files that are not zero length
# for name in glob.glob('/Users/getintotech/*'):
#     file_size = os.path.getsize(name)
#     if file_size > 0:
#         print(name, file_size)
#
#
#
# # TODO: Remove the leading directory name(s) from each filename before you print it -
# # using os.path.basename()
# for name in glob.glob('/Users/getintotech/*'):
#     file_size = os.path.getsize(name)
#     print(os.path.basename(name), file_size)
