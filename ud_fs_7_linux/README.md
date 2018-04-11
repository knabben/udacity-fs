Installed Softwares
---

* Vagrant
* Ansible

* PostgreSQL
* Apache2
* mod_wsgi

Ansible is a configuration management software, it is capable of keep states of your tasks without
redoing the work via SSH. All the work here was made with this, so the machine is kept immutable.


Deploy
===

Development
---

Start the vagrant box:

```
$ make run
```

To run the vagrant box for development you must run the following command:

```
$ make install
```

To destroy the machine:

```
$ make drop
```

To update the code on Vagrant machine run

```
$ make deploy
```


Production
---

To configure the production machine (IP is already configurated), you must have the private key:

```
$ ssh-add ~/.ssh/id_machine
```

Configure the software stack in the remote host.

```
$ make install_production
```

BEFORE: You must copy your client_secrets.json (Google Console provides you this) to /var/www/

To deploy code in production you must run:

```
$ make deploy_production
```


Configurations
===


SSH Configuration
---

SSH is hosted on a non-default port for production.

```
+Port {{ SSH_PORT }}
-#Port 22
```

Key Based SSH authentication.

```
-PasswordAuthentication yes
+PasswordAuthentication no
```

You cannot log in as a root remotely.

```
+PermitRootLogin no
-PermitRootLogin yes
```


Apache 2
---

000-default.conf Apache configuration file was substituted by this one:

```
<VirtualHost *:80>
    WSGIDaemonProcess main user=www-data group=www-data threads=5
    WSGIScriptAlias / /var/www/flask/wsgi.py

    <Directory /var/www/flask>
        WSGIProcessGroup main
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
```

Setting the WSGIScriptAlias parameter from root to the main wsgi.py application.


PostgreSQL
---

The pg_hba.conf file was modified to trust on localhost connections:

```
local   all             all                                     trust
local   all             postgres                                peer
host    all             all             127.0.0.1/32            trust
```
