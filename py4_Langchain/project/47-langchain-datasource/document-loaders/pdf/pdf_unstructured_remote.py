# pip install "unstructured[pdf]"

from langchain_community.document_loaders import OnlinePDFLoader
loader = OnlinePDFLoader("https://arxiv.org/pdf/2302.03803.pdf")
data = loader.load()
print(data)
