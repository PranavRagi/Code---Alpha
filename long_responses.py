import random

# Long responses
R_ADVICE = "If I were you, I would search the internet and input exactly what you just said!"

R_EATING = "I don't consume any food as I am a bot, obviously!"

# Function to handle unknown messages
def unknown():
    responses = [
        "Could you please rephrase that?",
        "Hmm...",
        "That sounds about right.",
        "What does that mean?"
    ]
    response = random.choice(responses)
    return response
