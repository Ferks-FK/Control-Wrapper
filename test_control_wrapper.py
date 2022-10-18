from control_wrapper import ControlWrapper
import asyncio

api = ControlWrapper("http://192.168.10.112:81", "iqrlA0Om2dzarsh5vj4KnteDEYCyc8gWsnEhfTG3pD6Ljstg")

async def lista_usuarios():
    usuarios = await api.user.update_user(1, name="teste", email="teste@teste.com")

    print(usuarios)
    return usuarios

asyncio.run(lista_usuarios())
