# API is Application Programming Interface
# Provides information of its rules and protocols that will be used
# Acts as an interface between a client and the server
# Restful API is Representational State Transfer API
# Difference between the two is that Restful API allows for us to perform CRUD operations
# CRUD stands for Create, Read, Update, Delete (Not operationally prioritized)
# Three famous ways of using Restful API in Python:
# 1) Django, 2) Flask, 3) FastAPI
# Django is a heavyweight application, can be more reliable and open-source
# Flask is a lightweight application, can be more reliable and open-source
# Django and Flask have similar concepts
# FastAPI is easy to use, supports asynchronus programming, much faster
# https://www.google.com/search?q=cat&rlz=1C1VDKB_enUS957US957&oq=cat&gs_lcrp=EgZjaHJvbWUqBwgAEAAYjwIyBwgAEAAYjwIyEggBEC4YQxiDARixAxiABBiKBTIGCAIQIxgnMgYIAxBFGD0yBggEEEUYPDIGCAUQRRg9MgYIBhBFGEEyBggHEEUYQdIBBzY4N2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8
# HTTP stands for HyperText Transfer Protocol and doesn't have security
# HTTPS stands for the same thing, but does have security
# Certificates, licensing, and ransomware provide security to an API
# Licensing is something we purchase which adds security
# Ransomware is like an antivirus, and provides some security layers through firewalls
# URL stands for Uniform Resource Locator
# (/search?)
# After the URL is over, there is a slash, and a word comes after the slash, which is called a path or root for an API
# The question mark is a path parameter
# At the end, there is source-id, which is cookies, and UTF-8 is encoding standard
# Cookies holds a lot of information like user information and browser capability information.
# (q=cat)
# Q means Query.
# Uvicorn is a server, which mainly supports FastAPI


from fastapi import FastAPI

app = FastAPI()
var_list = []

@app.get("/return")
def list_retrieve():
    return var_list

@app.post("/append")
def post_func(item: str):
    var_list.append(item)