import google.generativeai as genai

def get_category(prompt):
    API_KEY = "AIzaSyDX1lheYeca-QP7ZiaGUjvGsHYINcJi7WM"

    genai.configure(api_key=API_KEY)

    model_name = "gemini-1.5-pro-latest"

    # Create a generative model object
    model = genai.GenerativeModel(model_name)


    # Generate text with some customization options (optional)
    generation_config = {
        "temperature": 0.8,  # Controls randomness (0 = deterministic, 1 = more random)
        "max_output_tokens": 2048  # Maximum number of tokens to generate
    }
    response = model.generate_content(prompt, generation_config=generation_config)

    # Print the generated text
    print("response: ",response.text)
    return response.text

get_category("Is machine learning a part of Artificial Intelligence, sports, cooking, or something else? If it's something else, what is it? Just wirte the topic only")
