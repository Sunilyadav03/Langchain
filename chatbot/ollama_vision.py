import ollama

# image_path = 'my_pan.png'  # Replace with your image path

# Use Ollama to analyze the image with Llama 3.2-Vision
response = ollama.chat(
    model="llama3.2",
    messages=[{
      "role": "user",
      "content": "what is AI?"
    #   "images": [image_path]
    }],
)

# Extract the model's response about the image
cleaned_text = response['message']['content'].strip()
print(f"Model Response: {cleaned_text}")