import ollama

# Initialize the variable i
i = 0

# Define the system message to set the model's persona
system_message = {
    "role": "system",
    "content": "You are Sunil, a witty and knowledgeable AI assistant. Respond to queries with clarity and a touch of humor."
}

while i < 2:
    # Take user input for the question
    user_question = input(f"Write your {i + 1}th question: ")

    # Send the question to the Ollama model
    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                system_message,  # Set the persona
                {
                    "role": "user",
                    "content": user_question
                }
            ],
        )

        # Extract the model's response
        cleaned_text = response['message']['content'].strip()
        print(f"Sunil: {cleaned_text}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Increment the counter
    i += 1
