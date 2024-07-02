import dotenv
dotenv.load_dotenv()

from packages.retriever.index import retriever
from packages.retrieval_grader.grade_documents import retrieval_grader
from packages.retrieval_grader.grade_documents import grade_documents

def test_grade_documents(): 
    question = "Barcelona weather"
    print(f"\n\nGrading relevant documents for question: {question}. Assert 'no'")
    docs = retriever.get_relevant_documents(question)
    print(f"Retrieved documents: {len(docs)}")
    state = {'question': question, 'documents':docs}
    grade_documents(state)
    doc_txt = docs[1].page_content

    response = retrieval_grader.invoke({"question": question, "document": doc_txt})
    assert response.binary_score == "no"

    question = "Potter 3000"
    print(f"\nGrading relevant documents for question: {question}. Assert 'yes'")
    print(f"Retrieved documents: {len(docs)}")
    state = {'question': question, 'documents':docs}
    grade_documents(state)
    docs = retriever.get_relevant_documents(question)
    doc_txt = docs[1].page_content

    response = retrieval_grader.invoke({"question": question, "document": doc_txt})
    assert response.binary_score == "yes"