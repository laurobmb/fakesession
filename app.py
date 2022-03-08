from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from subprocess import Popen
import subprocess

app = FastAPI(title="Fake cookie", docs_url = None, redoc_url = None)

def hostname():
    f = open("/etc/hostname")
    return f.read()

@app.get("/")
async def root():
    return 'up'

@app.get("/cookie/")
async def create_cookie():
    content = {"message": "we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="podhostnamesession", value=hostname())
    return response

