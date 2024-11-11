from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import uvicorn
import string
import random

app = FastAPI()

url_store = {}

SHORT_ID_LENGTH = 6
ALLOWED_CHARS = string.ascii_letters + string.digits


class URLRequest(BaseModel):
    original_url: str


def generate_short_id():
    return ''.join(random.choices(ALLOWED_CHARS, k=SHORT_ID_LENGTH))


def is_valid_url(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")


@app.post("/shorten")
async def shorten_url(request: URLRequest):
    original_url = request.original_url
    if not is_valid_url(original_url):
        raise HTTPException(status_code=400, detail="Некорректный URL. Он должен начинаться с http:// или https://")

    short_id = generate_short_id()
    while short_id in url_store:
        short_id = generate_short_id()

    url_store[short_id] = original_url
    return {"short_url": f"http://localhost:8000/{short_id}"}


@app.get("/{short_id}")
async def redirect_to_url(short_id: str):
    original_url = url_store.get(short_id)
    if not original_url:
        raise HTTPException(status_code=404, detail="Ссылка не найдена")

    return RedirectResponse(url=original_url)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
