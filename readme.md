
To run this app you will need: Flask and PyMYsql

```
python3 -m pip install PyMySQL
```

### Hosted on Azure

https://ritasapp.azurewebsites.net/

I followed this tutorial

https://github.com/smartninja/example-azure-flask


https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

For this project I used: Flask, PyMySQL, Jquery, REST API, AJAX call and linking to a third party API.

The project consists of a login screen which check the database to see if the user exists and that the password and email address are correct before bringing the user to the main page. 
![Login screen](images/loginscreen.png)

The table fetches a few films from the database using PyMySQL, REST API and AJAX calls.

![Film Table](images/table.png)

A create feature using Jquery, PyMySQL, REST API and AJAX calls.
![Update](images/createfilm.png)

An update feature using Jquery, PyMySQL, REST API and AJAX calls.
![Update](images/updatefilm.png)

An delete function that removes the film from the database:

The Search is hooked in to a third party api www.omdbapi.com and returns search results from the api. The OMDb API is a RESTful web service to obtain movie information, all content and images on the site are contributed and maintained by our users.

![Update](images/searchfilm.png)
