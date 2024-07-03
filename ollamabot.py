import os
import discord
import requests
import json
from datetime import datetime

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND = os.getenv('COMMAND', 'ollama') # Default to 'ollama' if not set
MODEL = os.getenv('MODEL')
LOG_FILE = "chatlog.txt"

# Initialize bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable message content intent
client = discord.Client(intents=intents)

# Make API request and log interactions
def get_ollama_response(prompt):
    url = "http://localhost:11434/api/chat"

    # Read log file and construct context messages
    context_messages = read_log_file()

    # Append current user prompt to context messages
    context_messages.append({"role": "user", "content": prompt})

    payload = {
        "model": MODEL,
        "messages": context_messages,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        try:
            data = response.json()
            if "message" in data and "content" in data["message"]:
                chat_response = data["message"]["content"]
                log_interaction(prompt, chat_response)
                return chat_response
            else:
                error_msg = "No valid response from the API."
                log_interaction(prompt, error_msg)
                return error_msg
        except json.JSONDecodeError as e:
            error_msg = f"Error decoding JSON response: {e}"
            log_interaction(prompt, error_msg)
            return error_msg

# Read log file and construct context messages
# Currently set to 50 pairs for context but can be changed below
def read_log_file(max_context=50):
    context_messages = []
    with open(LOG_FILE, 'r') as log:
        lines = log.readlines()
        
        # Limit the number of context pairs to max_context
        start_index = max(0, len(lines) - 2 * max_context)
        
        for i in range(start_index, len(lines), 2):
            if i + 1 < len(lines):
                if len(lines[i].strip().split('] ')) > 1 and len(lines[i+1].strip().split('] ')) > 1:
                    user_prompt = lines[i].strip().split('] ')[1].split(': ')[1]
                    assistant_response = lines[i+1].strip().split('] ')[1].split(': ')[1]
                    context_messages.append({"role": "user", "content": user_prompt})
                    context_messages.append({"role": "assistant", "content": assistant_response})
    
    return context_messages[-2 * max_context:]  # Return only the last max_context pairs

# Log interactions to file
def log_interaction(prompt, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{timestamp}] User: {prompt}\n")
        log.write(f"[{timestamp}] Assistant: {response}\n\n")

# Bot ready handler
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Incoming messages handler
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f'!{COMMAND}'):
        prompt = message.content[len(f'!{COMMAND}'):].strip()

        if prompt:
            # Send initial message
            response_message = await message.channel.send("...")

            # Get API response
            response = get_ollama_response(prompt)

            # Send (edit) response to Discord channel
            await response_message.edit(content=response)
        else:
            await message.channel.send("Who, me? (Please provide a prompt)")

# Run the bot
client.run(DISCORD_TOKEN)

# Well hello there :) If you're reading this you'll probably find a few flaws/quirks. Well, it works... For now...

# -fatcat
