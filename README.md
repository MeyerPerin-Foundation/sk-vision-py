# Vision plugin for the Microsoft Semantic Kernel

The code in this repository provides a simple Python interface to connect the [OpenAI Vision API](https://platform.openai.com/docs/guides/vision) to the [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel/).

# Requirements

This plugin requires the following packages to be installed:
- `semantic_kernel`
- `openai`
- `python-dotenv`

The plugin also requires an OpenAI API key and organization ID. You can get these by creating an account on [OpenAI](https://openai.com/). Then, create a `.env` file in the root of your project and add the following lines to it:

```
OPENAI_API_KEY=<your api key>
OPENAI_ORG_ID=<your organization id>
```

## How to use the plugin

Copy the `VisionPlugin.py` file to your code. Then, import it and create a new instance of the `VisionPlugin` class. You can then use the plugin by calling the 'ApplyPromptToImage' method.

The code below shows a simple example of how to use the plugin.

```python
import semantic_kernel as sk
from semantic_kernel.orchestration import sk_context
import asyncio
from VisionPlugin import Vision

async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()

    vision = kernel.import_skill(Vision())
    variables = sk.ContextVariables()
    variables['prompt'] = "<the prompt you want to use>"
    variables['url'] = "<url of the image you want to use>"
    result = await kernel.run_async(vision['ApplyPromptToImage'], input_vars=variables)
    print(f"{result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Using the Vision plugin as part of the Semantic Kernel

I wrote a longer article in which I explain how to use the Vision plugin as part of the Semantic Kernel. You can find it [here](https://l.meyerperin.com/skv_py).
