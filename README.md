# Local Library

Local Library is a simple Django web application to manage small local library. Where users can issue a book, check availability and search the books. Admin can manage Books, Authors and Book Issue details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
1. [Python](http://docs.python-guide.org/en/latest/starting/install3/linux/)
2. [Django](https://docs.djangoproject.com/en/2.0/topics/install/)
3. [PostgreSQL](http://www.postgresqltutorial.com/install-postgresql/)


## Deployment

1. Consider this Local Library as a project which contains two different applications (1). Accounts and (2). Catalog.  Local Library directory contains settings file leave it as it is. Just you need to change E-mail configuration , Timezone and allowed IP addresses. 

	ALLOWED_HOSTS = [Address of your Host machine]\
  
2. Setup postgresql
	> setup credentials like this in application’s settings.py file
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'user_name',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

127.0.0.1:5432 is default host and port for postgresql. If you have changed Host and Port of your hosting database, you have to change here in settings.py file accordingly.	
3. Run `python manage.py make migrations` to create table schema in the database.
4. Run `python manage.py migrate` to apply changes in models.py.

## Built With

* [Python](https://www.python.org/download/releases/3.0/) - Base Language
* [Django](https://docs.djangoproject.com/en/2.0/) - The web framework used
* [PostgreSQL](https://www.postgresql.org/docs/) - Used as a Database

## Authors

* **Ishit Gandhi** - *Initial work* - [IshitGandhi](https://github.com/itgandhi)


## License

This project is Not licensed.

## Acknowledgments

* Mozilla Tutorials
