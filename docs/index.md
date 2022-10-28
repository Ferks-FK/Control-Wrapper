---
sidebar_position: 1
---

# Introduction

In this introduction you will learn the basics about how to authenticate to the API of your CPGG panel, and about using this Wrapper.

## Installation

At the moment you can test this package by installing the development version.
You will need [GIT](https://git-scm.com) installed to use the commands below.

#### To install

```
pip install git+https://github.com/Ferks-FK/Control-Wrapper@development
```

#### To upgrade

```
pip install --force-reinstall --no-deps git+https://github.com/Ferks-FK/Control-Wrapper@development
```

## First Authentication

The first step will be to create an API key in your CPGG panel for use with Control-Wrapper.
Go to `https://your-panel/admin/api/` and create a new one.

![Token Example](../static/img/Token%20Example.PNG)

With this API key, you can authenticate yourself through Control-Wrapper, and make your requests.
You are now ready to use the Wrapper.
