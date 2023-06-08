# README

This is the [Flask](http://flask.pocoo.org/) [quick start](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application) example for [Render](https://render.com).

The app in this repo is deployed at [https://flask.onrender.com](https://flask.onrender.com).

## Deployment

Follow the guide at https://render.com/docs/deploy-flask.


## Build Enviroment
```
python -m venv env
```
### Save Requirements with CMD
```
pip install -r requirements.txt
```

### Save Requirements with PowerShell
``` 
powershell -Command "pip freeze  | %{$_.split('==')[0]} | %{$_} > requirements.txt"
```

### Restore Requirements
```
pip install -r requirements.txt
```