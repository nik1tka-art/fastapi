from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get('/')
def root():
    return 'Hello мир'

"""
можно запускать проект как fastapi dev main.py
так же можно как uvicorn main:app --reload
reload это автоматическая перезагрузка сервера при изменение файла
uvicorn это веб-сервер, который принимает запросы от браузера и передаёт их fastapi"""

@app.get("/items/{item_id}")
def read_item(item_id:int) -> dict[str, int]:
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
