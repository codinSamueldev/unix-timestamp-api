from fastapi import FastAPI, Request
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

