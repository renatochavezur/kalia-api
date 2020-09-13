# Kalia API
This is a Django REST project to manage backend of kalia

## Commands
### Make Migrations
```
python manage.py makemigrations
```

### Create Superuser
```
python manage.py createsuperuser
```

### Run Migrations
```
python manage.py migrate
```

### Run Migrations on deployed stage
```
zappa manage dev migrate
```

### Run in local
```
python manage.py runserver
```

### Invoke zappa function
```
zappa invoke production 'my_app.my_function'
```

### Invoke raw zappa function
```
zappa invoke production "print(1 + 2 + 3)" --raw
```