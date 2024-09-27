from openai import OpenAI
from together import Together
import anthropic


OPENAI_API_KEY = 'INSERT OPENAI API HERE'
CLAUDE_API_KEY = 'INSERT CLAUDE API HERE'
LLAMA_API_KEY = 'INSERT TOGETHER API HERE'

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def get_text(
        self,
        text,
        model,
        max_tokens=500,
        temperature=0.0,
        top_p=1.00,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    ):
        # Try making the API call
        try:
            response = self.client.chat.completions.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                messages=[{"role": "user", "content": text}],
            )
        except Exception as e:
            raise Exception(f"Failed to create completion with OpenAI API: {str(e)}")

        # Check if the response has valid data
        if response.choices and len(response.choices) > 0:
            first_choice = response.choices[0]

            if first_choice.message and first_choice.message.content:
                return str(first_choice.message.content)
            else:
                raise Exception(
                    "Response from OpenAI API does not "
                    "contain 'message' or 'content'."
                )
        else:
            raise Exception(
                "Response from OpenAI API does not contain "
                "'choices' or choices list is empty."
            )

class ClaudeClient:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

    def get_text(
        self,
        text,
        model,
        max_tokens=500,
        temperature=0.0,
        top_p=1.00,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    ):
        # Try making the API call 
        try:
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                messages=[{"role": "user", "content": text}],
            )
        except Exception as e:
            raise Exception(f"Failed to create completion with Claude API: {str(e)}")

        # Check if the response has valid data response.content[0].text
        if response.content and len(response.content) > 0:
            first_choice = response.content[0]

            if first_choice.text:
                return str(first_choice.text)
            else:
                raise Exception(
                    "Response from Claude API does not "
                    "contain 'text'."
                )
        else:
            raise Exception(
                "Response from Claude API does not contain "
                "'choices' or choices list is empty."
            )

class LLaMAClient:
    def __init__(self):
        self.client = Together(api_key=LLAMA_API_KEY)

    def get_text(
        self,
        text,
        model,
        max_tokens=500,
        temperature=0.0,
        top_p=1.00,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    ):
        # Try making the API call
        try:
            response = self.client.chat.completions.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                messages=[{"role": "user", "content": text}],
            )
        except Exception as e:
            raise Exception(f"Failed to create completion with LLaMA API: {str(e)}")

        # Check if the response has valid data 
        if response.choices and len(response.choices) > 0:
            first_choice = response.choices[0]

            if first_choice.message and first_choice.message.content:
                return str(first_choice.message.content)
            else:
                raise Exception(
                    "Response from LLaMA API does not "
                    "contain 'message' or 'content'."
                )
        else:
            raise Exception(
                "Response from LLaMA API does not contain "
                "'choices' or choices list is empty."
            )
