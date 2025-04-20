from fastapi import FastAPI
import uvicorn

from routers import router

app=FastAPI()
app.include_router(router=router)

"""
можно запускать проект как fastapi dev main.py
так же можно как uvicorn main:app --reload
reload это автоматическая перезагрузка сервера при изменение файла
uvicorn это веб-сервер, который принимает запросы от браузера и передаёт их fastapi"""

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
