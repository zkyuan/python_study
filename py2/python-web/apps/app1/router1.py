from fastapi import APIRouter

app1 = APIRouter()


@app1.post("/post1",
           tags=["这是post1接口标题"],
           summary="接口测试语法",
           description="这是接口的详情信息",
           response_description="响应详细信息",
           deprecated=False,  # 是否废弃
           )
async def post():
    return "post1"


@app1.get("/get1")
async def get():
    return "get1"


@app1.put("/put1")
async def put():
    return "put1"


@app1.delete("/delete1")
async def delete():
    return "delete1"
