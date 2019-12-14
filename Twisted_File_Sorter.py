import os
import argparse
import time
from File_Type import f_Type

parser = argparse.ArgumentParser()
parser.add_argument("-s","--source", action='store', dest='source', type=str,required=True, help='[Source dir] like: Downloads path')
parser.add_argument("-v","--verbose", action="store_true", dest="verbose",help="Verbose Mode")

args = parser.parse_args()

t0=time.time()

dl_dir = args.source
verbose=args.verbose


def rName(the_file_dir, the_filename,file_obj):
    new_path = os.path.join(os.path.join(dl_dir, the_file_dir), the_filename)
    i = 1
    if os.path.exists(new_path):

        while os.path.exists(new_path):
            fn = file_obj.name
            fn_tup=os.path.splitext(fn)
            new_flName="{0}-{1}{2}".format(fn_tup[0],str(i),fn_tup[-1])
            #print(new_flName)
            new_path=os.path.join(os.path.join(dl_dir, the_file_dir), new_flName)

            i+=1
    if verbose is True:
        print(file_obj.path, "==>", new_path)
    os.renames(file_obj.path,new_path)



def main():
    scanned = os.scandir(dl_dir)
    for file_obj in scanned:

        if os.path.isdir(file_obj) == True: # mute dirs
            continue

        file_name_tup = os.path.splitext(file_obj)
        file_ext = file_name_tup[-1]
        the_file_dir = f_Type(file_ext) # turning the file type into the folder
        the_filename = file_obj.name
        rName(the_file_dir,the_filename,file_obj)

main()

t1=time.time()
if verbose is True:
    print("Time -",t1-t0)