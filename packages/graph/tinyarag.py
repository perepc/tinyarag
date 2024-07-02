import os
from typing_extensions import TypedDict
from typing import List
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph,END

from ..off_topic.off_topic import off_topic
from ..retriever.retrieve import retrieve
from ..retrieval_grader.grade_documents import grade_documents
from ..retrieval_grader.decide_to_generate import decide_to_generate
from ..generator.generate import generate
from ..question_rewriter.transform_query import transform_query
from ..router.route_question import route_question
from ..answer_grader.grade_generation_v_documents_and_question import grade_generation_v_documents_and_question


# Load environment from .env file
load_dotenv()

llm_big = ChatGroq(model_name="llama3-8b-8192",api_key=os.environ.get('GROQ_API_KEY'))
llm_small = ChatGroq(mode="llama2", api_key=os.environ.get('GROQ_API_KEY'))

# State graph
class State(TypedDict):
    question: str
    generation: str
    documents: List[str]

# Langgraph workflow
workflow = StateGraph(State)

# LangGraph nodes
workflow.add_node("off_topic", off_topic)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("transform_query", transform_query)


# Build graph
workflow.set_conditional_entry_point(
    route_question,
    {
        "off_topic": "off_topic",
        "vectorstore": "retrieve",
    },
)
workflow.add_edge("off_topic", END)
workflow.add_edge("retrieve", "grade_documents")
workflow.add_conditional_edges(
    "grade_documents",
    decide_to_generate,
    {
        "transform_query": "transform_query",
        "generate": "generate",
    },
)
workflow.add_edge("transform_query", "retrieve")
workflow.add_conditional_edges(
    "generate",
    grade_generation_v_documents_and_question,
    {
        "not supported": "generate",
        "useful": END,
        "not useful": "transform_query",
    },
)

# Compile
app = workflow.compile()