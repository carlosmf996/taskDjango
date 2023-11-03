Creo el entorno virtual en la carpeta de mi proyecto

```bash
mkvirtualenv taskDjango
```

Instalo y actualizo PIP

```bash
-m pip install --upgrade pip
```

Creo el archivo "requirements.txt" y lo instalo

    requirements.txt ---> Django~=4.2.7

```bash
pip install -r requirements.txt
```

Creo el proyecto en la carpeta que quiero

```bash
django-admin startproject task .
```

Edito lo básico en "settings.py"

```python

TIME_ZONE = ‘Europe/Madrid’
LANGUAGE_CODE = ‘es-es’

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

ALLOWED_HOSTS = ['127.0.0.1','localhost', '.pythonanywhere.com']

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```

Creo la base de datos y la inicio

```bash
python manage.py migrate
```

Compruebo que mi servidor funciona

```bash
python manage.py runserver
```

En web puedo acceder con cualquiera de las siguientes URLs

    ---> 127.0.0.1
    ---> localhost