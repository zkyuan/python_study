from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

examples = [
    {
        "question": "谁的寿命更长，穆罕默德·阿里还是艾伦·图灵？",
        "answer":
            """
            这里需要跟进问题吗：是的。
            跟进：穆罕默德·阿里去世时多大？
            中间答案：穆罕默德·阿里去世时74岁。
            跟进：艾伦·图灵去世时多大？
            中间答案：艾伦·图灵去世时41岁。
            所以最终答案是：穆罕默德·阿里
            """
    },
    {
        "question": "craigslist的创始人是什么时候出生的？",
        "answer":
            """
            这里需要跟进问题吗：是的。
            跟进：craigslist的创始人是谁？
            中间答案：craigslist由Craig Newmark创立。
            跟进：Craig Newmark是什么时候出生的？
            中间答案：Craig Newmark于1952年12月6日出生。
            所以最终答案是：1952年12月6日
            """
    },
    {
        "question": "乔治·华盛顿的祖父母中的母亲是谁？",
        "answer":
            """
            这里需要跟进问题吗：是的。
            跟进：乔治·华盛顿的母亲是谁？
            中间答案：乔治·华盛顿的母亲是Mary Ball Washington。
            跟进：Mary Ball Washington的父亲是谁？
            中间答案：Mary Ball Washington的父亲是Joseph Ball。
            所以最终答案是：Joseph Ball
            """
    },
    {
        "question": "《大白鲨》和《皇家赌场》的导演都来自同一个国家吗？",
        "answer":
            """
            这里需要跟进问题吗：是的。
            跟进：《大白鲨》的导演是谁？
            中间答案：《大白鲨》的导演是Steven Spielberg。
            跟进：Steven Spielberg来自哪里？
            中间答案：美国。
            跟进：《皇家赌场》的导演是谁？
            中间答案：《皇家赌场》的导演是Martin Campbell。
            跟进：Martin Campbell来自哪里？
            中间答案：新西兰。
            所以最终答案是：不是
            """
    }
]

from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
#使用语义相似性示例选择器
example_selector = SemanticSimilarityExampleSelector.from_examples(
    # 这是可供选择的示例列表。
    examples,
    # 这是用于生成嵌入的嵌入类，该嵌入用于衡量语义相似性。
    OpenAIEmbeddings(),
    # 这是用于存储嵌入和执行相似性搜索的VectorStore类。
    Chroma,
    # 这是要生成的示例数。
    k=1
)

# 选择与输入最相似的示例。
question = "大白鲨的导演是哪个国家的?"
selected_examples = example_selector.select_examples({"question": question})
print(f"最相似的示例：{question}")
for example in selected_examples:
    print("\\n")
    for k, v in example.items():
        print(f"{k}：{v}")
