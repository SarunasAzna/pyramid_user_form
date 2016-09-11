# pyramid_user_form
Šarūnas first test with Pyramid framework.

# How to run the app
1. Create Virtual Env(VENV) fro project (*python-virtualenv* must be installed).
```
cd pyramid_user_form
virtualenv --no-site-packages -p /usr/bin/python3.5 venv
```
2. Activate VENV.
```
source venv/bin/activate
```
3. Install required packages
```
pip install -r requirements.txt
```
Note: ensure that you are using local *pip* - not global.
```
which pip
```
Expected output:
```
..../pyramid_user_form/venv/bin/pip
```
4. Install the App.
```
pip install -e app

```
5. Run dev server.
```
cd app
../venv/bin/pserve development.ini
```
