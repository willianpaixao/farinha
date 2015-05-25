# Farinha
Now you can store pieces of code or text in general for daily tasks. Very handy,
Farinha will make you more productive.

## Installation
I strongly recommend to use *farinha* under a portable and virtual environment,
like [Virtualenv](https://virtualenv.pypa.io/en/latest/).

After activate your environment, install the dependences:

```
pip install django
pip install fabric
```

Don't forget to initialize your SQLite database, as in any Django project:

```
python manage.py syncdb
```

## Basic usage
By now, you haven't install *farinha* as a Python module, the commands aren't in
your PATH yet. But you can run them like this:

```
python manage.py ls
python manage.py cat 1
python manage.py echo 1
```


## Basic commands
### *add* a new snippet
Creates a new snippet with the given title.

#### Examples
```
python manage.py add script.sh
python manage.py add first second
```

For further information, type:
```
python manage.py help add
```
