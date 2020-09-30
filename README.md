# Get Locations

### Introduction:
Get Locations is a Python Django application that retrieves the list of locations in the following format:
```angular2
{
'data':[
{
'state': 'Karnataka'
'districts': [
{
'id':1,
'name':'Bagalkot',
'pincode':'587101'
},
{
'id':2,
'name':'Bengaluru Rural',
'pincode':'560066'
}
...
]
},
.....
]
}
```

The _admin user_ has the privilege to add new locations to the database.

### Follow the steps to _run the application_:

1. Install all the required packages(python modules):

    ```pip install -r requirements.txt``` (Assuming that you have created a virtual environment)

2. Migrate all the models to the database(database is included in the code- **db.sqlite3**)
 
    ```python manage.py migrate```
    
3. When the migrations are successfully completed, we can run the server:

    ```python manage.py runserver```
    
    If the steps are followed correctly, the server will be up and running.
 
 4. To gather all static files:
   
    ```python manage.py collectstatic```

 4. To login to admin panel, we have to create a superuser:
 
    ```python manage.py createsuperuser``` (default- username: **root**, password: **root**)
    
    User can log into the **Admin Panel** using the following url(assuming that you are on local server):
    
        127.0.0.1:8000/admin/ (local instance)

### API Endpoints:

1. ```<base_url>/locations/``` list of all locations in the format mentioned above. (127.0.0.1:8000/locations/ on local instance)
