import sys

import requests
import openai
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# KEY
OPENAI_API_KEY = "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"

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}



def chat_with_gpt():
    # user_input = input()
    import sys

    # 获取命令行参数中的消息
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        # print(user_input)
    if user_input:
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "system", "content": "你是一名开源软件源代码后门木马漏洞代码检测专家，我将发送许多可能存在漏洞的代码，我需要你明确指出这些代码是否的确存在漏洞或木马。这些代码可能涉及到java/python/go/php等多种语言。"},
                         {"role": "user", "content": user_input}],
            "temperature": 0.3  # 设置较低的温度值以获得更具体的答案
        }
    try:
        # print("here")
        response = requests.post(url, headers=headers, json=data)
        # print(response)
        response_json = response.json()
        print("response" , response_json)
        reply = response_json['choices'][0]['message']['content'].strip()
        print(reply)
    #     # 将用户输入和ChatGPT的回复显示在文本框中
    #     chat_box.insert(tk.END, f"You: {user_input}\n")
    #     chat_box.insert(tk.END, f"ChatGPT: {reply}\n")
    #     chat_box.see(tk.END)
    #
    #     # 清空用户输入框
    #     user_input_box.delete("1.0", tk.END)
    except Exception as e:
        print(e)


chat_with_gpt()



