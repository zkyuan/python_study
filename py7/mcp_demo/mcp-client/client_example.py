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
from mcp import ClientSession  # MCP 客户端会话管理
from contextlib import AsyncExitStack  # 资源管理（确保客户端关闭时释放资源）


class MCPClient:
    def __init__(self):
        """初始化 MCP 客户端"""
        self.session = None
        self.exit_stack = AsyncExitStack()

    async def connect_to_mock_server(self):
        """模拟 MCP 服务器的连接（暂不连接真实服务器）"""
        print("✅ MCP 客户端已初始化，但未连接到服务器")

    async def chat_loop(self):
        """运行交互式聊天循环"""
        print("\n📢 MCP 客户端已启动！输入 'quit' 或 'exit' 退出")

        while True:
            try:
                query = input("\n📝 Query: ").strip()
                if query.lower() == 'quit' or query.lower() == 'exit':
                    print("\n👋 退出聊天...")
                    break
                print(f"\n🤖 [Mock Response] 你说的是：{query}")
            except Exception as e:
                print(f"\n⚠️ 发生错误: {str(e)}")

    async def cleanup(self):
        """清理资源"""
        await self.exit_stack.aclose()


async def main():
    client = MCPClient()
    try:
        await client.connect_to_mock_server()
        await client.chat_loop()
    finally:
        await client.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
