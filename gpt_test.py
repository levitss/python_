import openai
openai.api_key="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"

dataset=open("C:\gpt3_test\qa_dataset.txt","r").readline()
model="text-davinci-002"
prompt="Q:What is the capital of France?\nA:"
response=openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
test_question=["What is the tallest mountain in the world?","Who invented the telephone?"]
for question in test_question:
    prompt=f"Q:{question}\nA"
    response=openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer=response.choices[0].text.strip()
    print(f"Q:{question}\nA:{answer}\n")