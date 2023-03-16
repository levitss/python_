from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the pre-trained model and tokenizer
model_name = "distilbert-base-cased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Define a function to generate an answer to a question
def generate_answer(question, context):
    # Tokenize the input text
    inputs = tokenizer.encode_plus(question, context, return_tensors="pt")

    # Generate an answer using the fine-tuned model
    answer_start_scores, answer_end_scores = model(**inputs).values()
    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))

    return answer

# Define a route for the web API
@app.route("/qa", methods=["POST"])
def qa():
    # Get the question and context from the request body
    data = request.get_json()
    question = data["question"]
    context = data["context"]

    # Generate an answer to the question
    answer = generate_answer(question, context)

    # Return the answer as a JSON response
    return jsonify(answer=answer)

if __name__ == "__main__":
    app.run()
