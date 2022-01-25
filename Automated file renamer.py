from pathlib import Path
from datetime import datetime
import os

# Create a path object
test_files = Path("/home/diegoploche/Documents/test")

#Is the path a file?
#print(test_files.is_file())	#Should be false


#Is the path a directory?
#print(test_files.is_dir())	#Should be true


#Parent of the file
#print(test_files.parent)	#Should return everything before test

#What is the base of the filename?
#print(test_files.stem)		#Should return test

#What are the extensions of the file?
#print(test_files.suffix)	#Should return nothing
for file in test_files.iterdir():

    # 1) Check if the file is a file
    if file.is_file() and file.stem != ".DS_Store":
        # 2) Create helpful variables
        directory = file.parent
        extension = file.suffix

        old_name = file.stem
        department, report_type, old_date = old_name.split('-')

        # 3) Change date format and label the new file
        old_date = datetime.strptime(old_date, "%Y%b%d")
        date = datetime.strftime(old_date, '%Y-%m-%d')
        new_file = f'{date} - {department} - {report_type}{extension}'

        # 4) Calculate the month and create a new path with it
        month = datetime.strftime(old_date, "%B")
        new_path = test_files.joinpath(month)

        # 5) Check if the folder exists. If not, create it
        if not new_path.exists():
            new_path.mkdir()

        # 6) Create a new path in the new directory
        new_file_path = new_path.joinpath(new_file)

        # 7) Move the files
        file.replace(new_file_path)
