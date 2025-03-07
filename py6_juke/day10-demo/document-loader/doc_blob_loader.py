from typing import Iterator

from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoader
from langchain_core.document_loaders import BaseBlobParser, Blob
from langchain_core.documents import Document
blob_loader = FileSystemBlobLoader(path="./../resource", glob="*.mdx", show_progress=True)


class MyParser(BaseBlobParser):
    """一个简单的解析器，每行创建一个文档。"""

    def lazy_parse(self, blob: Blob) -> Iterator[Document]:
        """逐行将 blob 解析为文档。"""
        line_number = 0
        with blob.as_bytes_io() as f:
            for line in f:
                line_number += 1
                yield Document(
                    page_content=line,
                    metadata={"line_number": line_number, "source": blob.source},
                )



parser = MyParser()
for blob in blob_loader.yield_blobs():
    for doc in parser.lazy_parse(blob):
        print(doc)
        break
