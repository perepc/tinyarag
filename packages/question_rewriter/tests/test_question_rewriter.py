import dotenv
dotenv.load_dotenv()

from packages.question_rewriter.llm import question_rewriter

def test_question_rewriter():
    question = "Which programs Potter 3000 has?"
    print(f"\n\nTesting rewrite question: {question}")
    result = question_rewriter.invoke({"question": question})
    print (f"Edited question: {result}")