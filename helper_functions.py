from openai import OpenAI

client = OpenAI()

def print_llm_response(prompt):
    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    print("LLM Response:")
    print(response.output_text)