import subprocess
import json

def execute_curl():
    """根据 stream 参数的值选择不同的执行方式"""
    url = "https://api.deepseek.com/chat/completions"
    with open('key', 'r') as file:
        key = file.read()  # 读取整个文件内容
    headers = [
        "Content-Type: application/json",
        "Authorization: Bearer " + key
    ]
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "模型参数671B中的B是什么意思"}
        ],
        "stream": True
    }

    # 将数据转换为 JSON 字符串
    data_str = json.dumps(data)

    # 构建 curl 命令
    curl_command = [
        "curl",
        url,
        "-H", headers[0],
        "-H", headers[1],
        "-d", data_str
    ]

    # 执行 curl 命令并获取输出
    result = subprocess.run(curl_command, capture_output=True, text=True)

    if result.returncode == 0:
        print("Command executed successfully!")
        print("Response:\n", result.stdout)
    else:
        print("Error occurred:", result.stderr)

# 执行 curl 命令
execute_curl()
