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
def begin_chat(sid):
    sio.enter_room(sid, 'chat_user')
    print('user: ', sid, ' enter room chat_user')

@sio.event
def exit_chat(sid):
    sio.leave_room(sid, 'chat_user')
    print('user: ', sid, ' leave room chat_user')


@sio.event
async def echo(sid, data):
    await sio.emit('echo', data)
    print('echo')

@sio.event
def disconnect(sid):
    print('disconnected on', datetime.now().time())


if __name__ == '__main__':
    web.run_app(app)

