# dia-chefbot
Simple streamlit chatbot utilising the unofficial huggingchat API and streamlit. The chatbot returns a recipe based on ingredients provided by the user.

## Installation and Setup 
Python 3.9.13 https://www.python.org/downloads/

Create virtual environment
```
py -m venv venv
```

Activate venv
```
.\venv\Scripts\Activate
```

Install required packages:
```
pip install -r requirements.txt
```

## Authentication
The huggingchat API requires you to have a [HuggingFace](https://huggingface.co/) account to authenticate the API call. Make an account if you don't have one, then save your email and password as environment variables:

### On Linux or macOS:
```
export HUGGINGFACE_EMAIL=myemail@example.com
export HUGGINGFACE_PASSWORD=mypassword
```

To make them persistent, you can add the above lines to your ~/.bashrc or ~/.bash_profile or ~/.zshrc, depending on which shell you use.

### On Windows:

Using the Command Prompt:
```
setx HUGGINGFACE_EMAIL "myemail@example.com"
setx HUGGINGFACE_PASSWORD "mypassword"
```

Using PowerShell:
```
$env:HUGGINGFACE_EMAIL="myemail@example.com"
$env:HUGGINGFACE_PASSWORD="mypassword"
```

For persistent environment variables on Windows, you can also set them through the System Properties window.

## Running the chefbot
Run this command to have an instance of the chefbot open on your browser:
```
streamlit run main.py
```
![github1](https://github.com/f4ths/dia-chefbot/assets/91867823/f7baec20-03ae-43f2-a9d9-ad5f2473c454)
