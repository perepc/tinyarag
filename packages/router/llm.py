from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

from packages.router.RouteQuery import RouteQuery

# LLM with function call. Notice that the selected model is a llama3 8b instead of biggest llama3 70b as 
# we don't need an advanced LLM model to just classify if something is off-topic
llm = ChatGroq(model_name="llama3-8b-8192", temperature=0)

structured_llm_router = llm.with_structured_output(RouteQuery)

# Prompt
system = """You are an expert at routing a user question to a vectorstore or off topic.
The vectorstore contains documents related to Potter 3000 washing machine user manual.
Use the vectorstore for questions related to Potter 3000. Otherwise, use off topic."""
route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router