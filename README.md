# Task manager
The website task manager for professionally

Web base on Python Django and Sqlite3


# Seting up evironment
### Install python
- In windows OS and Mac OS, you visit [python home page](https://www.python.org/)
    - Note: You must check `Add Python 3.x to PATH`
    -> [image](https://docs.blender.org/manual/vi/latest/_images/about_contribute_install_windows_installer.png)

- In Linux. Python already installed. You can use `python3` and `pip3` instead.

=> In here, I use python on Windows and I use `python` and `pip`.


### Create virtualenv for python (can be ignored)
- In Windows OS:
    - Note: In windows 8.1/10/11 you must open `powershell` in `admin permissions` and run before create virtualenv
        ```bash
        Set-ExecutionPolicy Unrestricted -Force
        ```

    ```bash
    # Create virtualenv
    python -m venv venv

    # Activate virtualenv
    venv/Script/activate
    ```

- Linux/ MacOS
    ```bash
    # Create virtualenv
    python3 -m venv venv

    # Activate virtualenv
    source venv/bin/activate
    ```


### Install python library
```bash
pip install -r requirements.txt
```


### Init and update database structor
```bash
python manage.py migrate
```


### Create superuser account (Can be ignored)
```bash
python manager.py createsuperuser
```


### Run server
```bash
python manage.py runserver <ip address>

# <ip address>
#   if is empty -> 127.0.0.1:8000 (localhost:8000)
#   0.0.0.0:port -> public server to outside
```


### Open browser and type address to enjoy website
```bash
    localhost -> home page
    localhost/admin -> admin manager
```

## Note:
- If you public website to outside. You can access website in LAN. Get server address. You can run this command:
```bash
# Windows
ip config

# Mac/Linux
ifconfig
```


# Thank you so much
