import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import asyncio
from EdgeGPT import Chatbot, ConversationStyle

import streamlit as st
import asyncio
from EdgeGPT import Chatbot, ConversationStyle

async def main():
    bot = await Chatbot.create() # Passing cookies is optional
    conversation_style = ConversationStyle.creative
    st.title("EdgeGPT Chatbot")

    # Define a function to handle user input and display chatbot responses
    async def ask_chatbot(prompt):
        response = await bot.ask(prompt=prompt, conversation_style=conversation_style.precise)
        final_msg = response["item"]["result"]["message"]
        return final_msg

    # Create an input field for the user to enter prompts
    user_prompt = st.text_input("User Input", value="Hello world")
    if st.button("Send"):
        # Call the chatbot and display the response
        bot_response = await ask_chatbot(user_prompt)
        message(user_prompt,is_user=True)
        message(bot_response)

    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
