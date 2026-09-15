###### standard library imports ######
import os
import shutil

###### 3rd party imports ######
#import from thing i downloaded 

###### local imports ######
# from module import something



def copy_file_recursive(soruce_dir_path, dest_dir_path):
    for name in os.listdir(soruce_dir_path):
        from_path = os.path.join(soruce_dir_path, name)
        to_path = os.path.join(dest_dir_path, name)

        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)

        else:
            if not os.path.exists(to_path):
                os.mkdir(to_path)
            copy_file_recursive(from_path, to_path)


def delete_and_recreate(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)

    os.mkdir(dir_path)