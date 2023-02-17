import openai
import os

openai.organization = "org-FSa4NxgrGx4qQMRGIFpUh31b"
openai.api_key = os.getenv("OPENAI_API_KEY")

def rephrase(sent: str, print_sent=False):
    openai.organization = "org-FSa4NxgrGx4qQMRGIFpUh31b"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f'Rephrase the following sentence in a unique way: {sent}',
        temperature=0.4,
        max_tokens=32,
        n=1
    )

    sentences = [choice["text"].replace("\n", "") for choice in response["choices"]]
    if print_sent:
        print(sentences)
    return sentences

rephrase("hi")