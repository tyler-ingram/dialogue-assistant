from .client import get_model
from .service import ask
from .system_prompts import GENERATE_DIALOGUE_PROMPT
__all__ = ["ask", "get_model", "GENERATE_DIALOGUE_PROMPT"]