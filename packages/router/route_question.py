from packages.router.llm import question_router
import warnings

warnings.filterwarnings("ignore", message="WARNING! mode is not default parameter.")

def route_question(state):
    """
    Route question to off toppic or RAG.

    Args:
        state (dict): The current graph state

    Returns:
        str: Next node to call
    """

    print("---ROUTE QUESTION---")
    question = state["question"]
    source = question_router.invoke({"question": question})
    if source.datasource == "off_topic":
        print("---ROUTE QUESTION TO OFF TOPIC---")
        return "off_topic"
    elif source.datasource == "vectorstore":
        print("---ROUTE QUESTION TO RAG---")
        return "vectorstore"