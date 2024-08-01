from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get_data")
async def get_data(token: str, netid: str):
    url = f"https://app.alphax.cloud/getPathData?token={token}&netid={netid}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text
