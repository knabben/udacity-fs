Install and run
---

You should install the dependencies with npm:

```
npm install
```

To run the app use the webpack dev tool:

```
npm run start
```

Server is located at http://localhost:8080


Building
---

You can build the assets to be used in production:

```
npm run build
```

Copy the output of build/ folder.

Backend
---

Yelp 3rd Party API does not allow CORS, so I created a backend service in Flask
to use with the project. It connects YELP API and renders initial locations:

To run locally you can do this, and access it on: http://localhost:5000

```
git clone https://github.com/knabben/ud_fs_5_map_backend
$ pip install -r requirements.txt
$ python main.py
```

By default an existent backend is running in: http://52.206.145.58
