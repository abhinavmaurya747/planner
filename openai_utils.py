import openai
import asyncio


async def get_completion_from_messages(messages,
                                       model="gpt-3.5-turbo",
                                       temperature=1,
                                       max_tokens=3000):
    await asyncio.sleep(1)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return {"context": response.choices[0].message["content"], "usage": response.usage}
