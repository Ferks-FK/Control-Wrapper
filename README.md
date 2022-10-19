<h1 align="center"> 
    Control-Wrapper
</h1>
</br>

![Discord](https://img.shields.io/discord/876934115302178876?label=DISCORD&style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/Ferks-FK/Pterodactyl-AutoAddons?style=for-the-badge)

<h1 align="center">What is this?</h1>

Control-Wrapper is an **Async API Wrapper** written in Python for the [ControlPanel](https://controlpanel.gg) API.
This is intended to make CPGG API calls easier to use for any endpoint.

<h1 align="center">Project Status</h1>

Currently this project is being maintained by [Ferks-FK](https://github.com/Ferks-FK), and is in its initial stage (Alpha), so any bugs or problems you find, please open an issue on github.
So far, this package is not on [PyPi](https://pypi.org) because it is still in its early stages.

<h1 align="center">How to install?</h1>

At the moment you can test this package by installing the development version.
You will need [GIT](https://git-scm.com) installed to use the command below.

```
pip install git+https://github.com/Ferks-FK/Control-Wrapper@development
```

<h1 align="center">Usage Examples</h1>

```py
from control_wrapper import ControlWrapper as CPGG
import asyncio

api = CPGG("https://mydomain.com", "my token")

async def get_users():
    users = await api.user.list_users()
    print(users)
    
    return users
 
asyncio.run(get_users())
```

<h1 align="center">Available Endpoints</h1>

Currently only a few user endpoints are available, the rest will be implemented as the project develops.

```py
api = CPGG("https://mydomain.com", "my token")

api.user.list_users()
api.user.user_details()
api.user.update_user()
api.user.suspend_user()
api.user.unsuspend_user()
```
