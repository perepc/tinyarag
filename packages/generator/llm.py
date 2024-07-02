from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Prompt
prompt = hub.pull("rlm/rag-prompt")

# LLM
llm = ChatGroq(model_name="llama3-70b-8192", temperature=0)

# Post-processing
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# Chain
rag_chain = prompt | llm | StrOutputParser()