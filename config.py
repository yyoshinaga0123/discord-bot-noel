import os

# Retrieve the bot token from the environment variable
TOKEN = os.environ.get('DISCORD_TOKEN')

# Retrieve the text channel ID for notifications
enter_id = int(os.environ.get('DISCORD_ENTER_CHANNEL_ID'))

# Retrieve the voice channel IDs
v_ippan = int(os.environ.get('DISCORD_VOICE_CHANNEL_IPPAN_ID'))
v_test = int(os.environ.get('DISCORD_VOICE_CHANNEL_TEST_ID'))

# Add any other configurations as needed
