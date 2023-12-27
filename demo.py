import semantic_kernel as sk
from semantic_kernel.orchestration import sk_context
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from dotenv import load_dotenv
import asyncio
from VisionPlugin import Vision


async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()
    gpt3 = OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id)
    kernel.add_chat_service("gpt3", gpt3)

    vision = kernel.import_skill(Vision())
    plugins = kernel.import_semantic_skill_from_directory(".", "plugins")

    # read each line of the animal url List text
    with open('animal_url_list.txt') as f:
        lines = f.readlines()
    
    # remove whitespace characters like `\n` at the end of each line
    animal_url_list = [x.strip() for x in lines]  

    # Interpreting memes
    meme_base_url = "https://raw.githubusercontent.com/lucas-a-meyer/lucas-a-meyer.github.io/main/images/"
    meme_url_list = ["meme1.jpg", "meme2.png", "meme3.jpg"] 

    for url in meme_url_list:
        variables = sk.ContextVariables()
        variables['prompt'] = "Why is this meme funny?"
        variables['url'] = meme_base_url + url
        print(f"Processing meme {meme_base_url + url}")
        meme = await kernel.run_async(vision['ApplyPromptToImage'], input_vars=variables)
        print(f"{meme}\n\n")     

    # Generating facts about animals
    count = 0
    # List of animal positions to process so you can easily skip
    # some and save money on OpenAI credits
    animal_positions_to_process = [2, 9, 10]
    for url in animal_url_list:
        count += 1
        if count in animal_positions_to_process:
            variables = sk.ContextVariables()
            variables['prompt'] = "What animal is this? Please respond in one word."
            variables['url'] = url
            animal = await kernel.run_async(vision['ApplyPromptToImage'], input_vars=variables)
            facts = await kernel.run_async(plugins['AnimalFacts'], input_str=str(animal))
            print(f"The animal from the picture is a {animal}")  
            print(f"{facts}\n\n")

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
