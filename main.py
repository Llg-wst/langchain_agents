from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

# Load environment variables
try:
    load_dotenv()
except  Exception as e:
    print(f"An error occured: {e}")

# Initialize the OpenAI chat model
llm = ChatOpenAI(model_name="gpt-4.1", temperature=0.2)


# Define the main function to interact with the user
def main():
    print("Hello! how can I help you today? (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = llm.invoke([HumanMessage(content=user_input)])
        print(f"AI: {response.content}")


if __name__ == "__main__":
    main()
