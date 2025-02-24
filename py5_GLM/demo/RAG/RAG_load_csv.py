"""
 * @author: zkyuan
 * @date: 2025/2/24 13:33
 * @description: 加载csv文件
"""

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='../weather_district_id.csv', encoding='utf-8')

data = loader.load()

for record in data[:2]:
    print(record)