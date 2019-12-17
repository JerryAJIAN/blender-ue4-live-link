import socket
import threading
import bpy
from bpy.props import (BoolProperty, IntProperty, PointerProperty)
from bpy.types import (PropertyGroup)


class MySettings(PropertyGroup):

    is_running: BoolProperty(
        name="is_running",
        description="Is the server currently running",
        default=False)

    port: IntProperty(
        name="port",
        description="Port to listen for livelink connections on",
        default=8888,
        min=8080)


def register():
    bpy.utils.register_class(MySettings)


def unregister():
    bpy.utils.unregister_class(MySettings)
    bpy.types.Scene.my_tool = PointerProperty(type=MySettings)


def startserver():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(),8888))
    s.listen(1)

    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        clientsocket.send(bytes("welcome to the server", "utf-8"))

    thread = threading.Thread(target=startserver)
    thread.start()


register()
print("Registered")
