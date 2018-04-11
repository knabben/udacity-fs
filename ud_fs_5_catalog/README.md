Run on DEV prod like env
---

NOTE: You should have Vagrant, VirtualBox and pip installed on your machine.

For the development environment you must clone the repository from:

```
$ git clone https://github.com/knabben/ud_fs_7_linux
```

After the clone run the virtual machine and provision it with Ansible,
the necessary dependencies are going to be installed.

```
ud_fs_7_linux$ make run ; make install
```

To login you must copy the client_secrets.json on your app/ folder.

Access:

```
http://localhost:8000/
```

Development
---

For development create a virtualenv on the host machine, after activation,
install the requirements:

```
$ virtualenv items
$ source items/bin/activate
items$ pip install -r requirements.txt
```

Run the application
```
python main.py
```

Service is provided on localhost:5000
