import dotenv
dotenv.load_dotenv()

from packages.answer_grader.llm import answer_grader

def test_answer_grader():
    question = "Is Potter 3000 a washing machine?"

    print(f"\n\nFor question: {question}")
    generation = "Today is friday"
    print(f"\nGrading answer: {generation}")

    result = answer_grader.invoke({"question": question, "generation": generation})
    print(f"Does answer solve the question? {result.binary_score}")

    generation = "Yes, it is a washing machine"
    print(f"\nGrading answer: {generation}")
    result = answer_grader.invoke({"question": question, "generation": generation})
    print(f"Does answer solve the question? {result.binary_score}")