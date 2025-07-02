import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

try:
    load_dotenv()
except Exception as e:
    print(f"An error occured: {e}")


model = init_chat_model("gpt-4o", model_provider="openai")

system_template = "Translate the following text to {language} from English."

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}"),
    ]
)
prompt = prompt_template.invoke({"language": "German", "text": "Hello, how are you?"})

response = model.invoke(prompt)
print(response.content)
    