import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPEN_AI_KEY")
openai.api_key = api_key

def main(message):
  
  api_key = os.getenv("OPEN_AI_KEY")
  openai.api_key = api_key
  messages = [{"role": "system", "content": "You are a kind and helpful assistant."}]
  messages.append({"role": "user", "content": message})
  chat_response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
  reply = chat_response['choices'][0]['message']['content']
  print(reply)
  
  
  
main()
