## command to create virtual environment 
```
python -m venv venv
```

## command to activate virtual environment in windows
```
venv\Scripts\activate
```

## command to activate virtual environment in bash
```bash
source venv/scripts/activate
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

## To run project using uvicorn
```
uvicorn main:app --reload
```

## To run project using uvicorn in particular port
```
uvicorn main:app --port 3000 --reload
```

## To run project using uvicorn in production mode
```
uvicorn main:app --host 0.0.0.0 --port 8000
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
