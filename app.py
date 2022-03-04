from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from subprocess import Popen
import subprocess

app = FastAPI()

def hostname():
    process = subprocess.run(['hostname'], 
        check=True, 
        stdout=subprocess.PIPE, 
        universal_newlines=True
    )
    output = process.stdout
    return output

@app.get("/")
async def root():
    return 'up'

@app.get("/cookie/")
async def create_cookie():
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="podhostnamesession", value=hostname())
    return response

