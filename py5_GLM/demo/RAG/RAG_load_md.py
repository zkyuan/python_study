"""
 * @author: zkyuan
 * @date: 2025/2/24 13:56
 * @description: 加载md文件
"""

from langchain_community.document_loaders import UnstructuredMarkdownLoader

# 整个md文件内容是一个document
# loader = UnstructuredMarkdownLoader(file_path='test_translated.md')

#
loader = UnstructuredMarkdownLoader(file_path='test_translated.md', mode='elements')

data = loader.load()
print(data)