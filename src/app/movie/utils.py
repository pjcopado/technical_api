import re


def clean_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.split(r"Response:", text)[-1]
    text = re.sub(r"[\s\W_]+", " ", text)
    return text.strip()
