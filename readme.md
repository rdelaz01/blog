#How to create a Django project

## Step 1 is to  create a folder for the project 


## step 2 
    Open folder in Vscode 

## step 3 
    Create a virtual environment for the project 

    py -m venv venv 


## step 4 
Activate the venv 

    .\venv\Scripts\activate

## step 5 
Install Django dependency 
     pip install django 


## step 6 
Run the project command to create the project settings 

    Django-admin startproject (name of project) .
    Name of project can be any followed by a (.)

    will create 2 folders and a **Manage.py** 

## Step 7 run server 
    python manage.py runserver 

## Step #8 
python manage.py startapp NAME_OF_THE_APP


# TO LINK PAGES 

## STEP 1
     Create File.html


## STEP 2 
    Create Class Views.py make sure path is correct to file/folder

## STEP 3
    create path in urls and import View

## STEP 4 



## Models in Django 
when we finish a models structure we need to run these commands in order:
    1. python manage.py makemigrations
    2. python manage.py migrate 