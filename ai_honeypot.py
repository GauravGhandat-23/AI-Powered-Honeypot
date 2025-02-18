import streamlit as st
import requests
import logging
import os
from datetime import datetime
from groq import Groq

# Log file setup
LOG_FILE = "honeypot.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

# Groq API client setup (Ensure to replace with your actual API key)
client = Groq(api_key="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")

# Function to analyze attack using Groq AI
def analyze_attack(ip, username, password, user_agent, endpoint):
    try:
        # Send request to Groq API for completion
        completion = client.chat.completions.create(
            model="qwen-2.5-32b",
            messages=[
                {"role": "system", "content": "Analyze the following login attempt for potential cyber threats."},
                {"role": "user", "content": f"IP: {ip}, Username: {username}, Password: {password}, User-Agent: {user_agent}, Endpoint: {endpoint}"}
            ],
            temperature=0.6,
            max_completion_tokens=4096,
            top_p=0.95,
            stream=True,
            stop=None,
        )

        # Handle streamed response
        analysis_result = ""
        for chunk in completion:
            if chunk.choices:
                # Print the structure of the chunk for debugging purposes
                print("Chunk structure:", chunk.choices[0])

                # Check if 'delta' has 'content' and handle None values
                delta = chunk.choices[0].delta
                if hasattr(delta, 'content') and delta.content is not None:
                    content = delta.content
                else:
                    content = "No content returned from Groq API."

                # Append the content to the analysis result
                analysis_result += content

        # Return the analysis result or a default message
        if not analysis_result:
            return "No analysis available."
        return analysis_result

    except Exception as e:
        logging.error(f"Error analyzing attack: {str(e)}")
        return f"Error analyzing attack: {str(e)}"

# Streamlit layout
st.title("AI-Powered Honeypot")
st.markdown("This honeypot uses AI to detect and analyze suspicious login attempts.")

# User login attempt form
with st.form(key='user_login_form'):
    st.subheader("User Login Attempt")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.form_submit_button("Login")
    
if login_button:
    ip = "192.168.1.1"  # Placeholder, replace with actual IP retrieval logic
    user_agent = "Mozilla/5.0"  # Placeholder, replace with actual user-agent
    logging.info(f"[LOGIN] IP: {ip}, Username: {username}, Password: {password}, User-Agent: {user_agent}")
    
    # AI Analysis
    analysis = analyze_attack(ip, username, password, user_agent, "LOGIN")
    
    st.markdown(f"### Login Attempt Results")
    st.write(f"**IP:** {ip}")
    st.write(f"**Username:** {username}")
    st.write(f"**Password:** {password}")
    st.write(f"**User-Agent:** {user_agent}")
    st.write(f"**Analysis:** {analysis}")
    
    # Log the result with AI feedback
    logging.info(f"AI Analysis: {analysis}")
    st.write("**Analysis logged to honeypot.log.**")

# Admin login attempt form
with st.form(key='admin_login_form'):
    st.subheader("Admin Login Attempt (Honeypot)")
    admin_username = st.text_input("Admin Username")
    admin_password = st.text_input("Admin Password", type="password")
    admin_login_button = st.form_submit_button("Admin Login")
    
if admin_login_button:
    ip = "192.168.1.1"  # Placeholder, replace with actual IP retrieval logic
    user_agent = "Mozilla/5.0"  # Placeholder, replace with actual user-agent
    logging.info(f"[ADMIN] IP: {ip}, Username: {admin_username}, Password: {admin_password}, User-Agent: {user_agent}")
    
    # AI Analysis
    analysis = analyze_attack(ip, admin_username, admin_password, user_agent, "ADMIN")
    
    st.markdown(f"### Admin Login Attempt Results")
    st.write(f"**IP:** {ip}")
    st.write(f"**Username:** {admin_username}")
    st.write(f"**Password:** {admin_password}")
    st.write(f"**User-Agent:** {user_agent}")
    st.write(f"**Analysis:** {analysis}")
    
    # Log the result with AI feedback
    logging.info(f"AI Analysis: {analysis}")
    st.write("**Analysis logged to honeypot.log.**")
