from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

@app.post('/chatbot/')
async def chatbot(message: str):
    response_text = {'message': 'Você disse: ' + message}
    return {"response_text": response_text}
