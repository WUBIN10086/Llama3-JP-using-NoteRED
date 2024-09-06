from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib
from llama_cpp import Llama

class LlamaAPI(BaseHTTPRequestHandler):
    # 初始化LLaMA模型
    llm = Llama(model_path="./Llama-3-ELYZA-JP-8B-q4_k_m.gguf", n_ctx=4098)

    # 处理GET请求，返回简单的说明页面
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {
            "message": "Welcome to LLaMA API. Use POST /ask with {'prompt': 'your question'}"
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))

    # 处理POST请求，生成LLaMA模型的回答
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # 获取请求体的长度
        post_data = self.rfile.read(content_length)  # 读取请求体
        request_data = json.loads(post_data.decode('utf-8'))  # 将请求体解析为JSON

        prompt = request_data.get('prompt', '')  # 提取用户输入的提示
        if not prompt:
            self.send_response(400)
            self.end_headers()
            response = {"error": "No prompt provided"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return

        # 使用LLaMA模型生成回答
        response = self.llm(prompt, max_tokens=100)
        generated_text = response['choices'][0]['text']

        # 返回生成的文本
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response_data = {
            "prompt": prompt,
            "response": generated_text
        }
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

# 启动HTTP服务器
def run(server_class=HTTPServer, handler_class=LlamaAPI, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting LLaMA API Server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=8080)
