from pprint import pprint

import dotenv
dotenv.load_dotenv()

from packages.graph.tinyarag import app



# Run
inputs = {
    "question": "Which washing programs does Potter 3000 have?"
}
app.stream(inputs)
for output in app.stream(inputs):
    for key, value in output.items():
        # Node
        print(f"Node '{key}':")
        # Optional: print full state at each node
        # pprint(value, indent=2, width=80, depth=None)
    # print("\n---\n")

# Final generation
print(value["generation"])
