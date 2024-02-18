import os

# Check whether the specified path exists or not
def check_create_dir(path):

    isExist = os.path.exists(path)
    
    if not isExist:

        # Create a new directory because it does not exist
        os.makedirs(path)
        print("The new directory is created!")

    else:
         print("The directory already exists")