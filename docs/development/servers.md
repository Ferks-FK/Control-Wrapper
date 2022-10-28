---
sidebar_position: 2
---

# Servers

Listed below are all the server methods, along with their parameters, filters, and includes.<br/>
All parameters that contain (`*`) are required.

## List Servers

> Returns a dict containing all registered servers, or `None` if a specific server is not found.<br/>
> Optionally you can provide Filters and Includes for server query.
:::tip Filters & Includes

name: `str` -> The server name.<br/>
identifier: `str` -> The server identifier.<br/>
user_id: `int` -> The user ID that owns the server.<br/>
pterodactyl_id: `int` -> The Pterodactyl ID of the user who owns the server.<br/>
product_id: `str` -> The ID of the product from which the server originates.<br/>
suspended: `str` | `datetime` -> A `str` or `datetime` object containing the date on which the server was suspended.<br/>
includes: `list` -> List of includes. Available Includes: `['product', 'productCount', 'user', 'userCount'].`
:::

## Server Details

> Returns a dict containing the server information, or `None` if not found.
:::tip Parameters

id: `int` -> The server ID. `*`
:::

## Suspend Server

> Returns a dict with the suspended server information, or an error if the ID does not exist.
:::tip Parameters

id: `int` -> The server ID. `*`
:::

## Unsuspend Server

> Returns a dict with the information of the server that had its suspension revoked, or an error if the ID does not exist.
:::tip Parameters

id: `int` -> The server ID. `*`
:::

## Delete Server

> Returns a dict containing the deleted server information, or an error if the ID does not exist.
:::tip Parameters

id: `int` -> The server ID. `*`
:::
