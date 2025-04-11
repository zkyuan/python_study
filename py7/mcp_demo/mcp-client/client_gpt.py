"""
 * @author: zkyuan
 * @date: 2025/4/10 21:39
 * @description:

以下是client.py 代码详解，代码核心功能：

初始化 MCP 客户端

提供一个命令行交互界面

模拟 MCP 服务器连接

支持用户输入查询并返回「模拟回复」

支持安全退出
"""
import asyncio  # 让代码支持异步操作
import os

from dotenv import load_dotenv
from mcp import ClientSession  # MCP 客户端会话管理
from contextlib import AsyncExitStack  # 资源管理（确保客户端关闭时释放资源）

from openai import OpenAI

# 加载 .env 文件，确保 API Key 受到保护
load_dotenv()


class MCPClient:
    def __init__(self):
        """初始化 MCP 客户端"""
        self.exit_stack = AsyncExitStack()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")  # 读取 OpenAI API Key
        self.base_url = os.getenv("BASE_URL_GPT")  # 读取 BASE YRL
        self.model = os.getenv("MODEL_GPT")  # 读取 model

        if not self.openai_api_key:
            raise ValueError("❌ 未找到 OpenAI API Key，请在 .env 文件中设置 OPENAI_API_KEY")

        self.client = OpenAI(api_key=self.openai_api_key, base_url=self.base_url)

    async def process_query(self, query: str) -> str:
        """调用 OpenAI API 处理用户查询"""
        messages = [{"role": "system", "content": "你是一个智能助手，帮助用户回答问题。"},
                    {"role": "user", "content": query}]

        try:
            # 将 OpenAI API 变成异步任务，防止程序卡顿
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=1000,
                    temperature=0.3,
                )
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ 调用 OpenAI API 时出错: {str(e)}"


    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\n📢 MCP 客户端已启动！输入 'quit' 或 'exit' 退出")
        while True:
            try:
                query = input("\n📝 Query: ").strip()
                if query.lower() == 'quit' or query.lower() == 'exit':
                    print("\n👋 退出聊天...")
                    break
                response = await self.process_query(query)  # 发送用户输入到 OpenAI API
                print(f"\n🤖 OpenAI: {response}")
            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")

    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()


async def main():
    client = MCPClient()
    try:
        await client.chat_loop()
    finally:
        await client.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
