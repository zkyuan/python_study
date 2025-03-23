"""
 * @author: zkyuan
 * @date: 2025/3/23 22:53
 * @description: ORM操作对象关系映射器
"""


if __name__ == '__main__':
    import uvicorn

    # uvicorn.run(app, host="127.0.0.1", port=8080)
    # 加上一下参数，app要写成 文件:app 的形式
    uvicorn.run("7、orm:app", host="127.0.0.1", port=8080, reload=True)
