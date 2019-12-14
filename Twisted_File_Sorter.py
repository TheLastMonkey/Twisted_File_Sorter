import os
from os import path
import argparse
import time
from File_Type import f_Type

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", action='store', dest='source', type=str, required=True,
                    help='[Source dir] like: Downloads path')
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="Verbose Mode")

args = parser.parse_args()

t0 = time.time()

source_dir = args.source
verbose = args.verbose


def sort_it(the_file_dir, the_filename, file_ext, source_f_path):
    # path assembly
    new_path = path.join(path.join(source_dir, the_file_dir), the_filename + file_ext)

    i = 1
    # check to see if the path already exists
    while os.path.exists(new_path):
        # Filename with ext assembly
        new_file_name = "{0}-{1}{2}".format(the_filename, str(i), file_ext)  # test-1.txt
        # path assembly
        new_path = path.join(path.join(source_dir, the_file_dir), new_file_name)
        i += 1

    if verbose:
        print(source_f_path, "==>", new_path)
    os.renames(source_f_path, new_path)


def main():
    scanned = os.scandir(source_dir)
    for file_obj in scanned:

        if path.isdir(file_obj):  # mute dirs
            continue
        source_f_path = file_obj.path
        the_filename, file_ext = path.splitext(file_obj.name)
        the_file_dir = f_Type(file_ext)  # turning the file type into the folder
        sort_it(the_file_dir, the_filename, file_ext, source_f_path)


main()

t1 = time.time()
if verbose:
    print("Time -", t1 - t0)
