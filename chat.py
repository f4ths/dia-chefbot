import streamlit as st
from streamlit_chat import message
from hugchat import hugchat

# Setting the Streamlit page configuration
st.set_page_config(page_title="ChefBot", page_icon=":robot:")
st.markdown("<h1 style='text-align: center; color: white;'>ChefBot</h1>", unsafe_allow_html=True)
st.markdown("Powered by [HuggingFace](https://github.com/huggingface) and [Streamlit](https://streamlit.com).")

# st.write("---")
# st.markdown("<h3 style='text-align: left; color: white;'>Enter your details:</h3>", unsafe_allow_html=True)

# Displaying the options for job title, industry, years of experience, accomplishments, and skills and technologies
# col1, col2 = st.columns(2)
# with col1:
# 	recipe_title = st.text_input('Title of Recipe:', '')
#
# with col2:
# 	dietary_restrictions = st.selectbox(
# 		'Dietary Restrictions:',
# 		('Vegan', 'Vegetarian', 'Pescetarian', 'Keto', 'Halal', 'No Restrictions')
# 	)

st.markdown("---")
st.markdown("<h3 style='text-align: left; color: white;'>Start Chatting</h3>", unsafe_allow_html=True)

# Initialize session state if not already
if 'generated' not in st.session_state:
	st.session_state['generated'] = ["Hi I'm ChefBot, your personal AI-powered recipe generator. Please list the ingredients you have in your kitchen and I'll suggest recipes you can make!"]
if 'past' not in st.session_state:
	st.session_state['past'] = ['Hi!']

# Layout of input/response containers
input_container = st.container()
response_container = st.container()

# Global variable to keep track of the conversation history
conversation_history = []

# Initial prompt
initial_prompt = """As an AI-powered recipe generator, you assist users in finding recipes based on the ingredients they have in their kitchen.
	Your goal is to generate a recipe that the user can make with the ingredients they have in their kitchen.
	List out the ingredients and instructions for the recipe."""

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
	chatbot = hugchat.ChatBot()

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
			message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
			message(st.session_state["generated"][i], key=str(i))

# contextualized_prompt = (f"""As an AI-powered recipe generator, you assist users in finding recipes based on the ingredients they have in their kitchen. Users will interact by providing a list of ingredients they have in their kitchen.
	#
	# The user provides the following context:
	# List of ingredients they have in their kitchen: {prompt}
	# Dietary Restrictions: {dietary_restrictions}
	# Type of dish they would like to make: {recipe_title}
	#
	# Your goal is to generate a recipe that the user can make with the ingredients they have in their kitchen.
	# List out the ingredients and instructions for the recipe.""")

	# Contextualize the prompt with user's information.
	# contextualized_prompt = (f"""As an AI-powered professional development coach, you assist users in their job search and resume enhancement. Users will interact by asking questions regarding their skills, job search, career advice, and more.
	#
	#     The user provides the following context:
	#
	#     Current Job Title: {job_title}
	#     Industry: {industry}
	#     Years of Experience: {years_experience}
	#     Skills and Technologies mastered: {skills_technologies}
	#     Current employment status: {current_job}
	#
	#     Your goal is to provide insightful responses and actionable advice based on the user's input, to guide them in their career development journey.""")
