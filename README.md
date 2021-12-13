##Setup

Please refer to `requirements.txt` for installing the necessary dependencies for running web app

Git clone this project

In terminal, go into the repo folder:

```
cd OMDB_APP
```

Create a venv:

```
python -m venv venv
```

Activate venv:

```
. venv/bin/activate
```

Install depencencies using `requirements.txt`

```
pip install -r `requirements.txt`
```

Run the web app in terminal

```
python3 app.py
```

#This is a back-end web app which allows users to search for movies and obtain the list of movies as a set of links. The data is fetched from the Open Movie Database API - OMDB API. Users search history will be stored in /history.

### diagram of client server architecture

```
            request                makes a request to get 'omdbapi.com/?t=jaws'
[browser]------------>[movies app]-------------------------------------------------->[omdb api]


            response                    JSON response from omdbapi.com
[browser]<------------[movies app]<--------------------------------------------------[omdb api]
```

### Resource and documentation

-    Open movie database API](http://www.omdbapi.com/)

### Tech used:

-    Python Flask
-    OMDB api
-    html
-    CSS
