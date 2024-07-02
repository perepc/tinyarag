from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from packages.answer_grader.GradeAnswer import GradeAnswer

# LLM with function call. Notice that the selected model is a llama2 instead of biggest llama3 as 
# we don't need an advanced LLM model to just classify if something is off-topic
llm = ChatGroq(model_name="llama3-8b-8192", temperature=0)

structured_llm_grader = llm.with_structured_output(GradeAnswer)

# Prompt
system = """You are a grader assessing whether an answer addresses / resolves a question \n 
     Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""
answer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "User question: \n\n {question} \n\n LLM generation: {generation}"),
    ]
)

answer_grader = answer_prompt | structured_llm_grader