import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

# connect static files
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.route('/')
async def home(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse(request, 'index.html')


if __name__ == '__main__':
    try:
        uvicorn.run(app, port=8000, host='0.0.0.0')
    except KeyboardInterrupt:
        pass