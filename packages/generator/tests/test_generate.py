import dotenv
dotenv.load_dotenv()

from packages.retriever.index import retriever
from packages.generator.generate import generate

def test_generate():
    question = "Which are the Potter 3000 washing programs?"
    docs = retriever.get_relevant_documents(question)
    print(f"\n\nRetrieved documents: {len(docs)}")
    print(f"Generating response for question: {question}")
    state = {'question': question, 'documents':docs}

    result = generate(state)
    print(result['generation'])