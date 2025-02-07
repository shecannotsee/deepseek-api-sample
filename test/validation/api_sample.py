# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

with open('key', 'r') as file:
    key = file.read()  # 读取整个文件内容

client = OpenAI(api_key=key, base_url="https://api.deepseek.com")
DeepSeek_V3 = "deepseek-chat"
DeepSeek_R1 = "deepseek-reasoner"
messages = [{"role": "user", "content": "大模型中的B是什么意思"}]

# Round 1
response = client.chat.completions.create(
    model=DeepSeek_V3,
    messages=messages,
    stream=False
)

content = response.choices[0].message.content
print(content)
print("对话结束, 下一段对话...\n")

# Round 2
messages.append({"role": "assistant", "content": content})
messages.append({'role': 'user', 'content': "671B是指的是什么呢"})

response = client.chat.completions.create(
    model=DeepSeek_V3,
    messages=messages,
    stream=True
)
reasoning_content = ""
content = ""
for chunk in response:
    if chunk.choices[0].delta.reasoning_content:
        reasoning_content += chunk.choices[0].delta.reasoning_content
    else:
        content += chunk.choices[0].delta.content
print(reasoning_content)
print(content)
