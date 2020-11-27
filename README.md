# Django_Pizza
Pizza Django
download the complete folder, 

All instruction based on windows operating system


first thing that we need is activate virtual environment for that: 
have to run env\script\activate

now go to pizza directory


run this commands:

- "python manage.py makemigrations"
- "python manage.py migrate"
- "python manage.py runserver"

than go to browser 

http://127.0.0.1:8000/posts -for list all data in rest framework

http://127.0.0.1:8000/input -for add data in database rest framework

http://127.0.0.1:8000/remove/1 -for update or delete data from database (remove/1 where "1" is entery id for delete or update data of it)

Here is the tables :

1. shape_piza

  1 -> regular
  2 -> square

2. size_piza

  1 -> small
  2 -> medium
  3 -> large

3. Choice

  1 -> corn
  2 -> capsicum
  3 -> onion
  4 -> cheese
  5 -> tomato
