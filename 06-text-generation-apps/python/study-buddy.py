from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

question = input("Ask questions related to javascript: ")
prompt = f"""You are a tutor that helps students answering doubts in javascript. The response should be in this format:
    - concept
    - detail explaination to the doubt
    - code related to the doubt
    
    Provide the answer for this question: {question}
"""

messages = [{"role": "user", "content": prompt}]
chat = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages)

print(chat.choices[0].message.content)
