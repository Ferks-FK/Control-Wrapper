---
sidebar_position: 1
---

# Users

Listed below are all the user methods, along with their parameters, filters, and includes.<br/>
All parameters that contain (`*`) are required.

## Create User

> Returns a dict of the new registered user.<br/>
> If any of the supplied parameters are in the wrong format or are missing, (with the exception of the password), an error will be returned.
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
role: `str` -> The user role. Available Roles: `['admin', 'moderator', 'client', 'member']`.<br/>
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

## Update User

> Returns a dict with the user updated data.<br/>
> If the `email` is in the incorrect format, or the user ID does not exist, one will be returned.
:::tip Parameters

id: `int` -> The user ID. `*`<br/>
name: `str` -> The new user name. `*`<br/>
email: `str` -> The new email of the user. `*`<br/>
credits: Optional[`int`] -> The new user credits.<br/>
server_limit: Optional[`int`] -> The amount of servers user can manage.<br/>
role: Optional[`str`] -> The new user role. Valid Roles: `['admin', 'moderator', 'client', 'member']`.
:::
:::info
For some reason the API forces you to pass the user `name` and `email` address in order to update it.
:::

## Suspend User

> Returns a dict of the user who was suspended.<br/>
> If the user is already suspended, or, the user ID passed in does not exist, an error will be returned.
:::tip Parameters

id: `int` -> The user ID. `*`
:::

## Unsuspend User

> Returns a dict of the user who had his suspension revoked.<br/>
> If the user is not already suspended, or, the user ID passed in does not exist, an error will be returned.
:::tip Parameters

id: `int` -> The user ID. `*`
:::

## Increment User

> Returns a dict of the user who had an increment added.<br/>
> If the user ID passed in does not exist, or if any parameter has an incorrect value, an error will be returned.
:::tip Parameters

id: `int` -> The user ID. `*`<br/>
credits: `int` -> The amount of credits that will be added to the user.<br/>
server_limit: `int` -> The amount of server limit that will be added to the user.
:::
:::info

This method will not overwrite the user's existing server credits or limits, instead the new value will be added to the old one.<br/>
The `credits` and `server_limit` parameters are not required simultaneously, but one of them must be supplied.
:::

## Decrement User

> Returns a dict of the user who had an decrement added.<br/>
> If the user ID passed in does not exist, or if any parameter has an incorrect value, an error will be returned.
:::tip Parameters

id: `int` -> The user ID. `*`<br/>
credits: `int` -> The amount of credits that will be added to the user.<br/>
server_limit: `int` -> The amount of server limit that will be added to the user.
:::
:::info

This method will not overwrite the user's existing server credits or limits, instead the new value will be deducted from the old one.<br/>
The `credits` and `server_limit` parameters are not required simultaneously, but one of them must be supplied.
:::

## Delete User

> Returns a dict of the user that was deleted.<br/>
> If the user ID does not exist, an error is returned.
:::tip Parameters

id: `int` -> The user ID. `*`
:::
:::danger

Currently this endpoint will delete the user, even if they have servers associated with them, so use this with caution.
:::



