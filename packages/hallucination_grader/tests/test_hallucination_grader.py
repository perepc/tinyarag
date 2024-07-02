import dotenv
dotenv.load_dotenv()

from packages.retriever.index import retriever
from packages.hallucination_grader.llm import hallucination_grader

def test_hallucination_grader():
    question = "What is Potter 3000?"

    print(f"\n\nFor question: {question}")
    generation = "A car"
    print(f"\nGrading generation: {generation}")
    result = hallucination_grader.invoke({"documents": retriever.get_relevant_documents(question), "generation": generation})
    print(f"Generation is supported by the documents? (no hallucionations): {result.binary_score}")

    generation = "A washing machine"
    print(f"\nGrading generation: {generation}")
    result = hallucination_grader.invoke({"documents": retriever.get_relevant_documents(question), "generation": generation})
    print(f"Generation is supported by the documents? (no hallucionations): {result.binary_score}")