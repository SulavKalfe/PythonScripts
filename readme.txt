these are some of the scripts that i like to use instead of doing things manually.

i suggest that you add the folder that stores all your scripts in filepath of environment variable
as it allows you to run by providing it's name instead of full path.
eg: filename.py instead of path_to_your_file\filename.py
the path should look something like this: C:\Users\your_name\Documents\Scripts
where scripts is the name of the folder that contains all the scripts

if you are lazy like me and don't want to type the file name too i suggest the second option
create a .bat file and add all the alias to that file (which i have done you can just change the alias).
open registery editor and then find HKEY_CURRENT_USER\Software\Microsoft\Command Processor
if there is no Command Processor you can create it under HKEY_CURRENT_USER\Software\Microsoft
right click in Microsoft and click on new then key and name it Command Processor
create a new string value and name it AutoRun and provide the path as value
path looks something like this C:\Users\your_name\Documents\Scripts\alias.bat
where alias is .bat file name

now if you're extra lazy and don't want to type windows key and then cmd to open command prompt
you can add shortcut key to command prompt
go to command prompt's file location by press windows key and then type cmd you'll see go to file location
press it
then right-click command prompt
go to properties you'll see shortcut key option press it and then provide the key that you want
eg: I have my command prompt as ctrl+shift+c (it takes about 3 secs to load atleast for me but i'm lazy so i can wait)
now apply it, and now you can press the shortcut key, and it'll take you to command prompt

to create an alias you use
doskey variablename=filename.py       (if you aren't going to provide a param)
doskey variablename=filename.py $*    (if you are going to provide a param)
(param means parameter which is a value that you will provide to that file or function)

remember $* will accept all the param no matter the amount

now just open command prompt and provide the filename eg: filename.py and it will execute the script
or if you create alias provide the alias eg: variablename or variablename param (if you need to provide a param)

check out the file itself to get more details about that scripts

NOTE: since you're going to run these scripts from cmd don't use venv for this project install everything in machine itself
      don't forget to run pip install requirements.txt in terminal or copy the full path of it and run on cmd