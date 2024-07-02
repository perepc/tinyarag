from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

from packages.retrieval_grader.GradeDocuments import GradeDocuments

# LLM with function call. Notice that the selected model is a llama2 instead of biggest llama3 as 
# we don't need an advanced LLM model to just classify if something is off-topic
llm = ChatGroq(model_name="llama3-8b-8192", temperature=0)

structured_llm_grader = llm.with_structured_output(GradeDocuments)

# Prompt
system = """You are a grader assessing relevance of a retrieved document to a user question. \n 
    If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
    It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""
grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Retrieved document: \n\n {document} \n\n User question: {question}"),
    ]
)

retrieval_grader = grade_prompt | structured_llm_grader