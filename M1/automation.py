#!usr/bin/env python3
import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost != '127.0.0.1':
        return False

    return True

def check_connectivity():
    request = requests.get("http://www.google.com")
    responses = request.status_code
    if responses != 200:
        return False

    return True