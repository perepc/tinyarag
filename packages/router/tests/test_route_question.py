import dotenv
dotenv.load_dotenv()

from packages.router.route_question import route_question

def test_route_question(): 
    state = {'question':"What's the weather like in Barcelona?"}
    print(f"\n\nQuestion: {state['question']}\n")
    assert route_question(state) == "off_topic"

    state = {'question':"What are the washing programs available?"}
    print(f"\nQuestion: {state['question']}\n" )
    assert route_question(state) == "vectorstore"

    state = {'question':"What are the main functionalities of a Potter 3000?"}
    print(f"\nQuestion: {state['question']}\n" )
    assert route_question(state) == "vectorstore"

    state = {'question':"Is it healthy to ate apples?"}
    print(f"\nQuestion: {state['question']}\n" )
    assert route_question(state) == "off_topic"