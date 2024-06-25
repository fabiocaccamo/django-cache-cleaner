[![](https://img.shields.io/pypi/pyversions/django-cache-cleaner.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/pypi/djversions/django-cache-cleaner?color=0C4B33&logo=django&logoColor=white&label=django)](https://www.djangoproject.com/)

[![](https://img.shields.io/pypi/v/django-cache-cleaner.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/django-cache-cleaner/)
[![](https://static.pepy.tech/badge/django-cache-cleaner/month)](https://pepy.tech/project/django-cache-cleaner)
[![](https://img.shields.io/github/stars/fabiocaccamo/django-cache-cleaner?logo=github&style=flat)](https://github.com/fabiocaccamo/django-cache-cleaner/stargazers)
[![](https://img.shields.io/pypi/l/django-cache-cleaner.svg?color=blue)](https://github.com/fabiocaccamo/django-cache-cleaner/blob/main/LICENSE.txt)

[![](https://results.pre-commit.ci/badge/github/fabiocaccamo/django-cache-cleaner/main.svg)](https://results.pre-commit.ci/latest/github/fabiocaccamo/django-cache-cleaner/main)
[![](https://img.shields.io/github/actions/workflow/status/fabiocaccamo/django-cache-cleaner/test-package.yml?branch=main&label=build&logo=github)](https://github.com/fabiocaccamo/django-cache-cleaner)
[![](https://img.shields.io/codecov/c/gh/fabiocaccamo/django-cache-cleaner?logo=codecov)](https://codecov.io/gh/fabiocaccamo/django-cache-cleaner)
<!-- [![](https://img.shields.io/codacy/grade/{id}?logo=codacy)](https://www.codacy.com/app/fabiocaccamo/django-cache-cleaner) -->
[![](https://img.shields.io/codeclimate/maintainability/fabiocaccamo/django-cache-cleaner?logo=code-climate)](https://codeclimate.com/github/fabiocaccamo/django-cache-cleaner/)
[![](https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&logoColor=black)](https://github.com/psf/black)
[![](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# django-cache-cleaner
clear the entire cache or individual caches easily using the admin panel or management command.

## Installation
-   Run `pip install django-cache-cleaner`
-   Add `cache_cleaner` to `settings.INSTALLED_APPS`
-   Run `python manage.py migrate`
-   Restart your application server

## Usage

### Admin
To clear caches using the admin panel:
-   ➡️ Navigate to the `Cache Cleaner / Caches`
-   ✔️ Check the caches you want to clear
-   🧹 Select "Clear selected caches" from the actions menu
-   ✨ Done :)

### Command
This package doesn't need any setting.

#### Clear default cache
```python
python manage.py clear_cache
```

#### Clear individual caches
```python
python manage.py clear_cache news products
```

#### Clear all caches
```python
python manage.py clear_cache --all
```

## Testing
```bash
# clone repository
git clone https://github.com/fabiocaccamo/django-cache-cleaner.git && cd django-cache-cleaner

# create virtualenv and activate it
python -m venv venv && . venv/bin/activate

# upgrade pip
python -m pip install --upgrade pip

# install requirements
pip install -r requirements.txt -r requirements-test.txt

# install pre-commit to run formatters and linters
pre-commit install --install-hooks

# run tests
tox
# or
python runtests.py
# or
python -m django test --settings "tests.settings"
```


## License
Released under [MIT License](LICENSE.txt).

---

## Supporting

- :star: Star this project on [GitHub](https://github.com/fabiocaccamo/django-cache-cleaner)
- :octocat: Follow me on [GitHub](https://github.com/fabiocaccamo)
- :blue_heart: Follow me on [Twitter](https://twitter.com/fabiocaccamo)
- :moneybag: Sponsor me on [Github](https://github.com/sponsors/fabiocaccamo)

## See also

- [`django-admin-interface`](https://github.com/fabiocaccamo/django-admin-interface) - the default admin interface made customizable by the admin itself. popup windows replaced by modals. 🧙 ⚡

- [`django-colorfield`](https://github.com/fabiocaccamo/django-colorfield) - simple color field for models with a nice color-picker in the admin. 🎨

- [`django-extra-settings`](https://github.com/fabiocaccamo/django-extra-settings) - config and manage typed extra settings using just the django admin. ⚙️

- [`django-maintenance-mode`](https://github.com/fabiocaccamo/django-maintenance-mode) - shows a 503 error page when maintenance-mode is on. 🚧 🛠️

- [`django-redirects`](https://github.com/fabiocaccamo/django-redirects) - redirects with full control. ↪️

- [`django-treenode`](https://github.com/fabiocaccamo/django-treenode) - probably the best abstract model / admin for your tree based stuff. 🌳

- [`python-benedict`](https://github.com/fabiocaccamo/python-benedict) - dict subclass with keylist/keypath support, I/O shortcuts (base64, csv, json, pickle, plist, query-string, toml, xml, yaml) and many utilities. 📘

- [`python-codicefiscale`](https://github.com/fabiocaccamo/python-codicefiscale) - encode/decode Italian fiscal codes - codifica/decodifica del Codice Fiscale. 🇮🇹 💳

- [`python-fontbro`](https://github.com/fabiocaccamo/python-fontbro) - friendly font operations. 🧢

- [`python-fsutil`](https://github.com/fabiocaccamo/python-fsutil) - file-system utilities for lazy devs. 🧟‍♂️
