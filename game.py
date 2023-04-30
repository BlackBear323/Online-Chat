from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio.platform.flask import start_server

def chat():
    put_text("Welcome to the chat!")
    name = input("What's your name?", type=TEXT)
    while True:
        message = input("Enter your message:", type=TEXT)
        put_text(name + ": " + message)

if __name__ == '__main__':
    start_server(chat, port=8080)