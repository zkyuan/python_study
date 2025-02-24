"""
 * @author: zkyuan
 * @date: 2025/2/24 14:49
 * @description: RAG文本切割
"""
from langchain_text_splitters import RecursiveCharacterTextSplitter

with open('test.txt', encoding='utf8') as f:
    text_data = f.read()


'''
chunk_size：块的最大大小，其中大小由length_function决定
chunk_overlap：数据块之间的目标重叠。重叠数据块有助于在数据块之间划分上下文时减少信息丢失。
length_function：确定块大小的函数。
is_separator_regex：分隔符列表（默认为 ）是否应解释为正则表达式。
'''

# 递归切割器  Recursive递归的
# 默认的分隔符：["\n\n", "\n", " ", ""]
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
    # 分隔符，切分的方式，用下列优先级切分
    separators=[
        "\n\n",
        "\n",
        ".",
        "?",
        "!",
        "。",
        "！",
        "？",
        ",",
        "，",
        " "
    ]
)

# chunks_list = text_splitter.split_documents([text_data])
chunks_list = text_splitter.create_documents([text_data])

print(len(chunks_list))

print(chunks_list[0]) # page_content='Madam Speaker, Madam Vice President, our First Lady and Second Gentleman'
print('--------------------------')
print(chunks_list[1])
