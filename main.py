import streamlit as st
from streamlit_chat import message
from hugchat import hugchat
from hugchat.login import Login
import os

email = os.environ.get('HUGGINGFACE_EMAIL')
passwd = os.environ.get('HUGGINGFACE_PASSWORD')

if not email or not passwd:
	raise ValueError("Missing environment variables for email or password.")

# Log in to huggingface and grant authorization to huggingchat
sign = Login(email, passwd)
cookies = sign.login()

# Save cookies to local directory
cookie_path_dir = ".cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

# Setting the Streamlit page configuration
st.set_page_config(page_title="Word2Rec", page_icon="👨‍🍳🤖")
st.title("👨‍🍳🤖 Word2Rec")
st.markdown('''
    ## About
    This is an LLM-powered recipe chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [HugChat](https://github.com/Soulter/hugging-chat-api)API
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor)LLM model
    ''')

st.markdown("---")
st.markdown("<h3 style='text-align: left;'>Start Chatting</h3>", unsafe_allow_html=True)

# Initialize session states
if 'generated' not in st.session_state:
	st.session_state['generated'] = [
		"Hi I'm Word2Rec, your personal AI-powered recipe generator. Please list the ingredients you have in your kitchen and I'll suggest recipes you can make!"]
if 'past' not in st.session_state:
	st.session_state['past'] = ["Hi!"]

# Layout of input/response containers
input_container = st.container()
response_container = st.container()

# Global variable to keep track of the conversation history
conversation_history = []

# Initial hidden prompt passed to the model
initial_prompt = """As an AI-powered recipe generator, you assist users in finding recipes based on the ingredients they have in their kitchen.
	Your goal is to generate a recipe that the user can make with the ingredients they have in their kitchen.
	Give a title to the recipe, then list out the ingredients with the required quantity and instructions for the recipe."""

# Add the initial prompt to the conversation history
conversation_history.append(initial_prompt)


# Function for taking user provided prompt as input
def get_text():
	input_text = st.text_input("Enter your message: ", "", key="input")
	return input_text


# Applying the user input box
with input_container:
	user_input = get_text()
	if user_input:
		conversation_history.append(user_input)  # Add the user input to the conversation history


# Function for taking user prompt as input followed by producing AI generated responses
def generate_response():
	# Initialize the chatbot, cookie_path used for authentication to HuggingFace
	chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

	# Include the entire conversation history in the context
	context = ' '.join(conversation_history)
	response = chatbot.chat(context, temperature=0.5)

	# Add the AI response to the conversation history
	conversation_history.append(response)

	return response


# Conditional display of AI generated responses as a function of user provided prompts
with response_container:
	if user_input:
		response = generate_response()
		st.session_state.past.append(user_input)
		st.session_state.generated.append(response)

	if st.session_state['generated']:
		for i in range(len(st.session_state['generated'])):
			message(st.session_state['past'][i], is_user=True, avatar_style="lorelei", key=str(i) + '_user')
			message(st.session_state["generated"][i], avatar_style="bottts", key=str(i))
