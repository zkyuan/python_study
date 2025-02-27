# Langchain CLI脚手架

安装客户端和服务端命令：
pip install --upgrade "langchain[all]"

### 1、使用langchain cli命令创建新应用
langchain app new langserve

### 2、在add_routes中定义可运行对象，转到server.py并编辑
add_routes(app.NotImplemented)
### 3、使用poetry添加第三方包
pip install pipx
pipx ensurepath
pipx install poetry

poetry add langchain
poetry add langchain-openai
### 4、设置环境变量，编写代码
### 5、切换到项目目录，启动应用
poetry run langchain serve --port=8000
### 6、接口文档地址
localhost:8000/docs
