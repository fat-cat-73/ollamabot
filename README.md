# Ollama Discord Bot

## Overview

This is my very first GitHub Project! The Ollama Discord Bot uses the API of your local Ollama LLM
install to be used as a Discord bot on your server. This bot also keeps a record of the conversations
between users and Ollama to use the 50 most recent interactions as 'context' for the conversation which
allows it to carry on a conversation as opposed to it being a "new" chat every time it is prompted.

## Prerequisites

- ### Ollama
    You will need to download and install the Ollama application. The downloads can be found 
    both here:
    ### https://github.com/ollama/ollama
    and here:
    ### https://ollama.com/download

- ### Discord Bot
    A Discord bot needs to be set up prior to running the script. If you aren't familiar with the process, please read the official documentation on setting up the bot account. You will need the 'token' to execute the script.
    ### https://discord.com/developers/docs/quick-start/getting-started

 - ### Python
    A local install of Python is necessary to run this. I have not included a download of Python in this package
    so you must install it seperate. I am not sure which version are compatatble (probably most of them). **This was tested using Python 3.10.11** for reference.

## Setup
- ## If you want to use a specific version/path of Python
    Edit both the **setup.bat** and **run.bat** to include the correct path to your Python version. If they are left as <code>set python=python</code> it will use the Python version in your system/local path. It will create a virtualenv (venv) within the folder after running setup.bat.

- ## Edit the **run.bat** file to include:

    ### Discord Token
    <pre><code>::Set your user token
  set DISCORD_TOKEN=<b><u>your-discord-token-here</b></u></code></pre>

    ### Desired Discord Command
    <pre><code>:: Set your bot command
  set COMMAND=<b><u>your-bot-command-here</b></u></code></pre>

    ### Ollama Model
    <pre><code>::Set your Ollama model
  set MODEL=<b><u>ollama-model-here</b></u></code></pre>

## Usage

- ### Run the **setup.bat** file
- ### Execute the **run.bat** file
>[!TIP]
>You do not need to start your Ollama application as the **start.bat** file will open it automatically
- ### Have fun chatting with your new Ollama bot!

## Notes

- ### Logging file
    The chatlog.txt file will populate with both the **'user'** (prompt) and **'assistant'** (Ollama response) as pairs. This means every prompt sent by a user will also send the last 50 messages to Ollama as "context" to allow you to carry on conversations with the bot, as opposed to it treating every prompt as a new conversation (no memory/history retention).
> [!TIP] 
> You will probably want to clear the contents of this file periodically as it does not do it automatically!

- ### Ollama Models
    It is not necessary to download the model you want to use prior to starting the bot, you just need to set it in the **run.bat** file. When the line
    <code>**start ollama run %model%**</code> 
    is ran, it will automatically download the model, same as if you executed <code>ollama run (mistral/llama3/etc...)</code> normally via command prompt. If using a new model you will have to wait for it to download before prompting it in your discord server.

- ### Hope you enjoy! - fatcat (fat-cat-73)
