from fastapi import APIRouter

app2 = APIRouter()


@app2.post("/post2",
           tags=["这是post2接口标题"],
           summary="接口测试语法",
           description="这是接口的详情信息",
           response_description="响应详细信息",
           deprecated=False,  # 是否废弃
           )
async def post():
    return "post2"


@app2.get("/get2")
async def get():
    return "get2"


@app2.put("/put2")
async def put():
    return "put2"


@app2.delete("/delete2")
async def delete():
    return "delete2"
