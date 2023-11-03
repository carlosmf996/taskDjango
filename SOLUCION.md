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

Creo la aplicación (No puede tener el mismo nombre que el proyecto)

```bash
python manage.py startapp taskapp
```
En "settings.py" tenemos que registrar la apliación

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taskapp',]
```

Creamos un modelo en "models.py". Debería de quedar así:

```python
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

Aplicamos los cambios en los modelos para la Base de Datos

```bash
python manage.py makemigrations taskapp
```

```bash
python manage.py migrate taskapp
```

Modificamos el "admin.py" para crear un nuevo superusuario. Deberíamos tener algo así:

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Creamos el administrador. Necesitamos tener el servidor arrancado y ejecutar la siguiente orden en otra terminal

```bash
python manage.py createsuperuser
```
    Usuario ---> taskapp

Para acceder a la página del login:
    --->http://127.0.0.1:8000/admin/