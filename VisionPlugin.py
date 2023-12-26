from dotenv import load_dotenv
from openai import OpenAI
from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter
from semantic_kernel.orchestration.sk_context import SKContext
import os

class Vision:
    @sk_function(
        description="""Asks the GPT-4 Vision API to perform an operation described by the prompt
        on an image given its url""",
        name="ApplyPromptToImage"
    )
    @sk_function_context_parameter(
        name="prompt",
        description="The prompt you want to send to the Vision API",
    )
    @sk_function_context_parameter(
        name="url",
        description="",
    )
    def ApplyPromptToImage(self, context: SKContext) -> str:
        load_dotenv()
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": f"{context['prompt']}"},
                {"type": "image_url","image_url": {"url": f"{context['url']}",
            },},],}],
        max_tokens=300,
        )

        return response.choices[0].message.content