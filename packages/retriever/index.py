from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.markdown import UnstructuredMarkdownLoader
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

### from langchain_cohere import CohereEmbeddings

# Set embeddings
embd = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Let's load the markdown document
md_loader = UnstructuredMarkdownLoader(file_path='./data/Potter 3000 Washing Machine User Manual.md')
document = md_loader.load()

# Let's make some chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
doc_splits = splitter.split_documents(document)

# Add to vectorstore
vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chroma",
    embedding=embd,
)
retriever = vectorstore.as_retriever()