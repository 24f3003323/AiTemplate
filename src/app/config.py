import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    api_key: str
    model: str
    debug: bool

def load_settings() -> Settings:
    api_key = os.environ.get('LLM_API_KEY')

    if not api_key:
        raise RuntimeError('API key is not set!')
    
    return Settings(
        api_key=api_key,
        model=os.environ.get('LLM_MODEL','default_model'),
        debug=os.environ.get('DEBUG',False)
    )