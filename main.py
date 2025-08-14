from openai import OpenAI
from dotenv import load_dotenv
from characters.character import Character
from pprint import pprint

load_dotenv()

# Using a model snapshot to imrpove consistency
MODEL = "gpt-4o-mini-2024-07-18"
# MODEL = "gpt-5-mini"

client = OpenAI()

SYSTEM_PROMPT = """
You are a helpful assistant that extracts character information from \
https://starwars.fandom.com/wiki/
"""


def extract_character_info(character_name: str) -> Character:

    user_prompt = f"""
    Please extract the character information for {character_name}.
    """

    response = client.responses.parse(
        model=MODEL,
        # reasoning={'effort': 'low'},
        input=[
            {
                "role": "developer",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        text_format=Character,
    )

    return response.output_text


character = extract_character_info("Asajj Ventress")
pprint(character, indent=4)
