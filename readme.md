
To run this app you will need: Flask and PyMYsql

```
python3 -m pip install PyMySQL
```

### Hosted on Azure

https://ritasapp.azurewebsites.net/

I followed this tutorial

https://github.com/smartninja/example-azure-flask


https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

For this project I used: Flask, PyMySQL, Jquery
The project consists of a login screen which check the database to see if the user exists and that the password and email address are correct
![Login screen](images/loginscreen.png)

A table which fetches a few films from the database using PyMySQL
![Film Table](images/table.png)

A create feature using Jquery, 
![Update](images/createfilm.png)

An update feature using Jquery, 
![Update](images/updatefilm.png)

An delete function that removes the film from the database:

A search which is hooked in to www.omdbapi.com and returns from the api.
![Update](images/searchfilm.png)
