from fastapi import FastAPI
from pydantic import BaseModel
import httpx

# FastAPI app
app = FastAPI()

# 定义请求数据的模型
class PromptRequest(BaseModel):
    prompt: str

# 添加一个根路径的GET路由
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI testing service for LLaMA API"}


# 定义与LLaMA API进行交互的POST请求
@app.post("/test_ask")
async def test_ask(prompt_request: PromptRequest):
    async with httpx.AsyncClient() as client:
        # 将请求发送到LLaMA API
        llama_api_url = "http://localhost:8080/ask"
        headers = {"Content-Type": "application/json"}
        response = await client.post(llama_api_url, json=prompt_request.dict(), headers=headers)

    # 返回LLaMA API的响应
    return response.json()
