@echo off

:: Set your user token
set DISCORD_TOKEN=your_discord_token_here

:: Set your bot command
set COMMAND=your_bot_command_here

::Set your Ollama model
set MODEL=ollama_model_here

set python=python

echo Starting Ollama with %MODEL%

start ollama run %MODEL%

echo Starting the Discord bot...

%python% ollamabot.py

pause
