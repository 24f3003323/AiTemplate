from app.config import load_settings


def mask(secret:str) -> str:
    return secret[:3] + "***" if len(secret) > 3 else '***'

def main() -> None:
    print('Hello Dev!')
    settings = load_settings()
    print(f'Api key: {settings.api_key} Model Name: {settings.model} Debug: {settings.debug}')


if __name__ == '__main__' :
    main()