---
sidebar_position: 1
---

# Users

Listed below are all the user methods, along with their parameters, filters, and includes.<br/>
All parameters that contain (`*`) are required.

## Create User

> Returns a dict of the new registered user.
> 
:::tip Parameters

name: `str` -> The user name. `*`<br/>
email: `str` -> The user email. `*`<br/>
password: Optional[`str`] -> The user password. If a password is not supplied, a random one will be generated.
:::
:::info

If a random password is generated, this method or the API will NOT return the password.
In this case, the user will need to reset their password on the website.
:::

## List Users

> Returns all users registered in the system, or `None` if a specific user is not found.<br/>
> Optionally you can provide Filters and Includes for user query.
:::tip Filters & Includes
name: `str` -> The user name.<br/>
email: `str` -> The user email.<br/>
server_limit: `int` -> Limit of user servers.<br/>
pterodactyl_id: `int` -> The Pterodactyl ID of the user.<br/>
role: `str` -> The user role. Available Roles: `['admin', 'mod', 'client', 'member']`.<br/>
suspended: `bool` -> Whether the user is suspended or not.<br/>
includes: `list` -> List of includes. Available Includes: `['servers', 'serversCount', 'notifications', 'notificationsCount', 'payments', 'paymentsCount', 'vouchers', 'vouchersCount', 'discordUser', 'discordUserCount']`.
:::


## User Details

> Returns data for a specific user, or `None` if the user is not found.<br/>
> This is useful for checking whether a user has verified his discord account.
:::tip Parameters & Includes

id: `int` -> The user ID. `*`<br/>
includes: `list` -> List of includes. Available Includes: `['servers', 'serversCount', 'notifications', 'notificationsCount', 'payments', 'paymentsCount', 'vouchers', 'vouchersCount', 'discordUser', 'discordUserCount']`.
:::


