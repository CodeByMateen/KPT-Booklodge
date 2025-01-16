## command to create virtual environment
```
python -m venv venv
```

## command to activate virtual environment
```
venv\Scripts\activate
```

## For Linux
```bash
source venv/Scripts/activate
```

## To check python in virtual environment
```
python --version
```

## command to deactivate virtual environment
```
deactivate
```

## To install fastapi with standard
```
pip install "fastapi[standard]"
```

## To run fastapi in development mode
```
fastapi dev main.py
```

## To see the API documentation in swagger
```
http://127.0.0.1:8000/docs
```

## To see the API documentation in redoc
```
http://127.0.0.1:8000/redoc
```

## To create the requirements.txt file
```
pip freeze > requirements.txt
```

## To install the packages from the requirements.txt file
```
pip install -r requirements.txt
```