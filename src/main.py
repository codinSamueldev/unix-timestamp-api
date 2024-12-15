from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


import os
from datetime import datetime


DATE_FORMAT = "%Y-%m-%d %H:%M:%S GMT"


app = FastAPI()
templates = Jinja2Templates(directory=os.path.abspath("templates"))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})


@app.post("/", response_class=HTMLResponse)
def calculate_how_much_seconds_someone_has_lived(request: Request, birthday: str = Form(...)):
    """
    Feature for users to get out of curiosity, how many seconds they have lived.
    Params:
        birthday -> param that receives the data entered by the user in the date form.

    expected:
        200_response -> The feature should be able to calculate since EPOCH, how many seconds
        an user has lived and return either the seconds or age, or both.

    To keep in mind:
        a not leap year has 31536000 seconds.

    """

    birthday_date = datetime.strptime(birthday, "%Y-%m-%d") # get user birth date, turn it into a datetime obj.
    
    current_seconds = int(datetime.now().timestamp()) # get how many seconds have transcurred since EPOCH when POST request made.
    user_birthday_unix_seconds = int(birthday_date.timestamp()) # calculate seconds since EPOCH until user birth date.

    user_age_in_seconds = current_seconds - user_birthday_unix_seconds # substract and get user lived seconds.
    
    user_is = user_age_in_seconds // 31536000 # how old user is?


    return templates.TemplateResponse(request=request, name="results.html", context={ 
        "seconds": user_age_in_seconds,
        "year": user_is
        })


@app.get("/api")
def current_unix_code_and_utc_date():
    now = datetime.now()

    current_unix = int(now.timestamp())
    current_utc = now.strftime(DATE_FORMAT)

    return {"unix": current_unix, "utc": current_utc}


@app.get("/api/{dt}")
def turn_timestamp_to_unix_date_code(dt: datetime):
    return {"unix": dt.timestamp(), "utc": dt.strftime(DATE_FORMAT)}


@app.get("/api/{unix_code}")
def turn_unix_date_code_to_utc(unix_code: int):
    readable_unix_code = datetime.utcfromtimestamp(unix_code).strftime(DATE_FORMAT)

    return {"unix": unix_code, "utc": readable_unix_code}

