## Project is a work in progress (inactive as of now)

## Instructions before starting up project
- Before starting this, make sure you create a new MySQL database for this project.
- Npm modules may be out of date when you clone this repo, take out terminal and type out:
  - `npm install`
  - make to be in root directory of the project before executing the command

In settings.py you need the following

- **django secret key**:
  
  - you can generate one by creating an empty django project and copy pasting that secret key to this project or just type in something if you just want to test it out.
    
  Settings.py line 22  
    
   `
   SECRET_KEY = "SECRET KEY HERE"` 

- **MySQL Database**:
  - Name of database
  - Host  (_example : 130.0.0.5_)
  - Port  (_example: 4405_)
  - User  (_default is root_)
  - Password for MySQL
 
  ### Fill in the following details that are in caps 
  Settings.py line 80-89
  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': "DATABASE NAME",
          'HOST': "HOST",
          'PORT': "PORT",
          'USER': "USER, DEFAULT IS ROOT",
          'PASSWORD': "PASSWORD",
      }
  }

  ```
## How to start-up project:

1) Make sure to install django in an environment, its safer. If you already have a python environment, then install it there.

1) Make sure to have django installed, if not use `python -m pip install Django` in your environment.

2) Git clone the project and navigate with cmd to the folder containing `manage.py`.

3) Type the command: `python manage.py runserver`.


Sorry for not making this process user-friendly :/
Thanks for checking out the repo :)
