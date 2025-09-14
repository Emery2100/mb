#Important notes for Sjango Projects

open terminal and creat a folder to store the project
Move to the respective folder (Make sure that you are on the right location)
Create a Virtual environment (Win: python -m venv venv or Mac: python3 -m venv venv)
After the creation we have to activate our virtual environment (Win: venv\Scripts\activate or Mac: source venv/bin/activate)
install django (Win: pip install django or Mac: pip3 install django)
Create the project (django-admin startproject config .)
Create the structure for the project
-Create the static,templates, img, css, JS folders
-Create the .gitignore, README.md

#Additional Notes
-All of the subcommands for django are going to be called followed by python manage.py (E.G python manage.py runserver)
if we want to check the full list, we can run (python manage.py)
To create an app we need to run (python manage.py startapp NAME_OF_THE_APP) remember to change the name of the app for the actual name.
After a creation of an app make sure to create the urls.py file inside of the app (IF AND ONLY IF you are going to create views on it.)

Python manage.py startapp NAME_OF_THE_APP
