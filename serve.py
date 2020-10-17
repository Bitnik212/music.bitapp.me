from aiohttp import web
import socketio
from datetime import datetime

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins="*")
app = web.Application()
sio.attach(app)


@sio.event
def connect(sid, environ):
    print("connected on", datetime.now().time())


@sio.event
def disconnect(sid):
    print('disconnected on', datetime.now().time())


if __name__ == '__main__':
    web.run_app(app)

