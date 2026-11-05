from lmstudio import Chat
from .client import get_model

def ask(prompt: str, *,  system: str | None = None, model_key: str | None = None) -> str:
    """Ask a question to the LLM and get the response."""
    model = get_model(model_key)
    if system:
        chat = Chat(system)
        chat.add_user_message(prompt)
        result = model.respond(chat)
    else:
        result = model.respond(prompt)
    return result.content
