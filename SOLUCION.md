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