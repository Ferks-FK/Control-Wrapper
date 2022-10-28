---
sidebar_position: 3
---

# Vouchers

Listed below are all the voucher methods, along with their parameters, filters, and includes.
All parameters that contain (*) are required.

## Create Voucher

> Returns a dict with the information of the voucher created.<br/>
> If any of the supplied parameters are in the wrong format or are missing, an error will be returned.
:::tip Parameters

uses: `int` -> The number of times this voucher can be used. `*`<br/>
credits: `int` -> The amount of credits the user will receive when using this voucher. `*`<br/>
code: Optional[`str`] -> The voucher code. If none is provided, a random code will be generated.<br/>
memo: Optional[`str`] -> The voucher memo.<br/>
expires_at: Optional[`str` | `datetime`] -> A `str` or `datetime` object containing the voucher expiration date.
:::

## List Vouchers

> Returns all registered vouchers, or `None` if a specific voucher is not found.<br/>
> Optionally you can provide Filters and Includes for user query.
:::tip Filters & Includes

code: `str` -> The voucher code.<br/>
memo: `str` -> The voucher memo.<br/>
credits: `int` -> The voucher credits.<br/>
uses: `int` -> The uses for voucher.<br/>
includes: `list` -> List of includes. Available Includes: `['users', 'usersCount']`.
:::

## Voucher Details

> Returns a dict with the specific voucher data, or `None` if none is found.
:::tip Includes

includes: `list` -> List of includes. Available Includes: `['users', 'usersCount']`.
:::

## Update Voucher

> Returns a dict containing the updated voucher information, or an error if the voucher ID does not exist.
:::tip Parameters

id: `int` -> The voucher ID. `*`<br/>
code: `str` -> The voucher code. `*`<br/>
uses: `int` -> The uses for voucher. `*`<br/>
credits: `int` -> The voucher credits. `*`<br/>
memo: Optional[`str`] -> The voucher memo.<br/>
expires_at: Optional[`str` | `datetime`] -> A `str` or `datetime` object containing the voucher expiration date.
:::

## Delete Voucher

> Returns a dict with the deleted voucher information, or an error if the passed ID does not exist.
:::tip Parameters

id: `int` -> The voucher ID. `*`<br/>
:::