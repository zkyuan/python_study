"""
 * @author: zkyuan
 * @date: 2025/2/23 23:16
 * @description: 自定义工具Tools实例，查询天气
"""
import csv
import os
from typing import Type, Optional

import requests
from langchain.tools.base import BaseTool
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import chat_agent_executor
from pydantic import BaseModel, Field


def find_code(csv_file_path, district_name) -> str:
    """
    根据区域或者城市的名字，返回该区域的编码
    :param csv_file_path:
    :param district_name:
    :return: 城市编码
    """
    district_map = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as f:
        # 读取csv文件内容
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            # districtcode、district表格列字段名
            district_code = row['districtcode'].strip()
            district = row['district'].strip()
            # 城市名做键、城市编码做值
            if district not in district_map:
                district_map[district] = district_code
    # 根据城市名拿到编码并返回
    return district_map.get(district_name, None)


class WeatherInputArgs(BaseModel):
    """Input的Schema类"""
    location: str = Field(..., description='用于查询天气的位置信息')
    # location: str = Field(..., description='用于查询天气的位置信息')


# 参考别的工具(TavilySearchResults)实现，重写父类BaseTool的_run方法
class WeatherTool(BaseTool):
    """查询实时天气的工具"""
    name: str = 'weather_tool'
    description: str = '可以查询任意位置的当前天气情况'
    args_schema: Type[WeatherInputArgs] = WeatherInputArgs

    def _run(
            self,
            location: str,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """就是调用工具的时候，自动执行的函数"""
        district_code = find_code('weather_district_id.csv', location)
        print(f'需要查询的{location}, 的地区编码是: {district_code}')
        # 百度的天气查询接口，ak=百度网址申请的:https://lbs.baidu.com/apiconsole/key
        # url = f'https://api.map.baidu.com/weather/v1/?district_id={district_code}&data_type=now&ak=qdkcGt9AtcYfIsArwnzGz4PS09feivdH'
        url = f'https://api.map.baidu.com/weather/v1/?district_id={district_code}&data_type=now&ak=gY1JIffsDTozewoC8Xeds77nPKcSlvPX'

        # 发送请求
        response = requests.get(url)
        data = response.json()

        # 解析数据
        text = data["result"]["now"]['text']
        temp = data["result"]["now"]['temp']
        feels_like = data["result"]["now"]['feels_like']
        rh = data["result"]["now"]['rh']
        wind_dir = data["result"]["now"]['wind_dir']
        wind_class = data["result"]["now"]['wind_class']

        return f"位置: {location} 当前天气: {text}，温度: {temp} °C，体感温度: {feels_like} °C，相对湿度：{rh} %，{wind_dir}:{wind_class}"


if __name__ == '__main__':
    # print(find_code('weather_district_id.csv', '天门'))

    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_PROJECT"] = "zhipu"
    os.environ["LANGCHAIN_API_KEY"] = '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'

    # 创建模型
    model = ChatOpenAI(
        model='glm-4-plus',
        temperature='0.6',
        api_key=os.getenv("ZHIPU_API_KEY"),
        base_url='https://open.bigmodel.cn/api/paas/v4/'
    )

    tools = [WeatherTool()]

    agent_executor = chat_agent_executor.create_tool_calling_executor(model, tools)

    resp = agent_executor.invoke({'messages': [HumanMessage(content='中国的首都是哪个城市？')]})
    print(resp['messages'])

    resp2 = agent_executor.invoke({'messages': [HumanMessage(content='北京天气怎么样？')]})
    print(resp2['messages'])

    print(resp2['messages'][2].content)
