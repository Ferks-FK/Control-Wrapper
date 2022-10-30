---
sidebar_position: 4
---

# Notifications

Listed below are all the notification methods, along with their parameters, filters, and includes.<br/>
All parameters that contain (`*`) are required.

## User Notifications

> Returns all notifications from the user, or `None` if user has no messages.<br/>
> If the user ID does not exist, an error is returned.
:::tip Parameters

id: `int` -> The user ID. `*`
:::

## Notification Details

> Returns a dict containing the notification information, or an error if the user ID or notification ID does not exist.
:::tip Parameters

id: `int` -> The user ID. `*`<br/>
notification_id: `str` -> The notification ID. `*`
:::

## Send Notification To All Users

> Returns a dict containing the sent message informations.
:::tip Parameters

title: `str` -> The title of the message. `*`<br/>
content: `str` -> The content of the message. `*`<br/>
via: `str` -> The way in which users will receive the message. Available Methods: `['mail', 'database']`. `*`
:::
:::info

If the shipping method chosen is `mail`, and it is not working correctly on your server, an error will be returned.
:::

## Send Notification To Specific Users

> Returns a dict containing the sent message informations.
:::tip Parameters

title: `str` -> The title of the message. `*`<br/>
content: `str` -> The content of the message. `*`<br/>
users: `list` -> The user ID's that will receive this message. `*`<br/>
via: `str` -> The way in which users will receive the message. Available Methods: `['mail', 'database']`. `*`
:::
:::info

If the shipping method chosen is `mail`, and it is not working correctly on your server, an error will be returned.
:::

## Delete All Notifications

> Returns a dict containing the information of the user deleted messages.
:::tip Parameters

id: `int` -> The user ID. `*`
:::

## Delete Notification

> Returns a dict containing the information of the deleted message.
:::tip Parameters

id: `int` -> The user ID. `*`<br/>
notification_id: `str` -> The notification ID. `*`
:::