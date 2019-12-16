# Twisted_File_Sorter
Are you perhaps looking to sort files into folders by type?   
Then Twisted Files Sorter might be right for you!  
  
TFS accepts command-line arguments and can be run as a Cron job or scheduled task.  
TFS uses standard python libraries and is operating system agnostic.  
**Windows and Unix based systems**  

#### Use Case  
Perhaps you're a data hoarder with a messy Download Folder or perhaps you've recently considered automating your file organization OCD.
Well with TFS it's as easy as setting up a scheduled task to run in the background.
You can also just run it once by using the command line and some simple command-line arguments.  

#### Arguments  
-s or --source  
Specify a path to the directory that contains the files to be stored.  
This is a required argument.  
`python3 Twisted_Files_Sorter.py -s ~/USER/Downloads/`  
  
-v or --verbose  
as it implies this will verbosely print out what's happening. 
You could pipe this to a log if you prefer. It also outputs the time it took.  
`python3 Twisted_Files_Sorter.py -v -s ~/USER/Downloads/`  

#### Info  
A couple things you need to know. the source that you specify is also the
 destination for the subdirectories that are named by the file types that 
 they contain. TFS does not mess with directories.  So if you have 
 subdirectories within your downloads folder those subdirectories will 
 not be touched.  This is to ensure that pre associated files are not 
 scattered in two different subdirectories. This is part of a do not 
 disorganized philosophy.  
   
TFS comes with its own custom modules that you can edit to your liking.
 They define and return the file types based on the file extension. 
 There are three files you may consider editing.   
  
File_EXT.py  
This file is responsible for storing file extensions such as ".jpg", 
".txt" and so on.  
So in here you can add or remove different file extensions according to 
your preference.  
  
File_DIR.py  
This file is responsible for storing the directory names / file types. 
This file can be edited to your preference.  
  
File_Type.py  
This file is responsible for extension checking. 
It contains simple elif logic to identify a file type from its extension.  
##### **Important**  
If you would like to add a file type you will need to edit all three of 
the previously mentioned files in this section.  
The following is an example of how the three files are related.  
  
File_EXT.py  
`font_file_tup = (".fnt", ".fon", ".otf", ".ttf")`  
  
File_DIR.py  
`font_dir = "Fonts"`  
  
File_Type.py  
`elif f_ext in FILE_EXT.font_file_tup:
    return(FILE_DIR.font_dir)`
  
Understanding this allows you to modify to your heart's content.  
