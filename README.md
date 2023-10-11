# DPTH stack
DPTH, pronounced *"depth"* - an extended PyHAT stack. It contains these technologies:
- Django
- ASGI
- Django components
- PostgreSQL
- HTMX
- Hyperview
- TailwindCSS
- hyperscript

## Get started
Pull the repo:

```sh
git clone https://github.com/Tasty-Kiwi/dpth-stack.git
```

Install dependencies:

```sh
pip install -r requirements.txt
```

Fill in the .env file:

```properties
DB_NAME=<NAME>
DB_USER=<USERNAME>
DB_PASSWORD=<PASSWORD>
DB_HOST=<HOSTNAME>
DB_PORT=<PORT>
```

Make migrations:

```sh
python manage.py migrate
```

And finally, run the server:

```sh
python manage.py runserver
```

## Resources
[awesome-python-htmx](https://github.com/PyHAT-stack/awesome-python-htmx)

## License
Apache 2.0

btw, the name `onlykiwis` is just a joke