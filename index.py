#!/usr/bin/env python3
# -*-  coding: utf-8 -*-

from pywebio import *

def main():  # PyWebIO application function
    name = input.input("输入项目名称")
    #output.put_text("hello", name)

start_server(main, port=8090, debug=True)