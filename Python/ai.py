"""ai.py
A simple OpenAI client example with a placeholder for the API key.
"""

from openai import OpenAI

OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

client = OpenAI(api_key=OPENAI_API_KEY)


def main():
    user_prompt = input("Prompt: ")
    system_prompt = "Limit your answer to one sentence. Pretend you're a cat."

    response = client.responses.create(
        input=user_prompt,
        instructions=system_prompt,
        model="gpt-5"
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
