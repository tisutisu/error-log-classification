from dotenv import load_dotenv
from groq import Groq

def classify_using_llm(log_msg):
    load_dotenv()
    client = Groq()
    model = "llama-3.3-70b-versatile"
    prompt = f'''
    Classify the log message into one of these categories:
    (1) Test Failure, (2) Intermittent Failure, (3) Infra Failure, (4) Product Failure.
    If you can't figure out a category, return "Unknown".
    Only return the category name. No preamble.
    Log message: {log_msg}
    '''
    completion = client.chat.completions.create(
    model=model,
    messages=[
      {
        "role": "user",
        "content": prompt,
      }
    ],
    )
    return completion.choices[0].message.content

def main():
    print("Running LLM classifier")
    log_msg = "runtime error: invalid memory address or nil pointer dereference"
    category = classify_using_llm(log_msg)
    print("GOT CATEGORY: ", category)

if __name__ == '__main__':
    main()