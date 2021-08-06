
`Python` `js` `Django` 

## **Version of Python and Django**
>	Python==3.7.5   
>	django==2.1.5  

## **Step 1** ：Set up enviroment
>	download all files from https://github.com/2593628L/PandaE-books.git
>	$conda create -n panda python=3.7.5
>	$conda activate panda
>   $conda install django=2.1.5  
>   $conda install pillow

## **Step 2** ：Install some tools  
>	$pip install social-auth-app-django  
>	$pip install -U django-registration-redux==2.2  

## **Step 3** ：Migration and load script
>	$python manage.py makemigrations  
>	$python manage.py migrate  
>	$python populate_panda.py  


## **Step 4** ：Create a superuser
>	$python manage.py createsuperuser  

## **Step 5** ：Run server
>	$python manage.py runserver  

## **Step 6** ：Use PandaE-books
>	Open your browser and enter localhost:8000 to use PandaE-books
