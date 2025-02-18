<h1 align="center"> 🚀 AI-Powered Honeypot 🌟  </h1>

![Python](https://img.shields.io/badge/Python-3.8%2B-blueviolet) ![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-brightgreen) ![Groq AI](https://img.shields.io/badge/Groq%20AI-Powered-blue)

Welcome to the **AI-Powered Honeypot**, a cutting-edge cybersecurity tool designed to detect and analyze suspicious login attempts using artificial intelligence. This honeypot leverages the power of **Groq AI** to provide real-time insights into potential cyber threats. 🔒💻

---

## 📌 Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Screenshots](#screenshots)
6. [Contributing](#contributing)
7. [License](#license)

---

## 🌟 Overview

The **AI-Powered Honeypot** is a Streamlit-based application that simulates login endpoints to attract attackers. When a suspicious login attempt is detected, the system logs the details and sends them to Groq AI for analysis. The AI provides insights into the nature of the attack, helping you stay one step ahead of malicious actors. 🕵️‍♂️🤖

This tool is perfect for:
- **Cybersecurity researchers** looking to study attack patterns.
- **Developers** building secure applications.
- **System administrators** monitoring network security.

---

## ✨ Features

- **Real-Time AI Analysis**: Leverages Groq AI to analyze login attempts and detect potential threats. 🧠
- **Dual Login Endpoints**: Simulates both user and admin login attempts to attract attackers. 👤🔒
- **Detailed Logging**: Logs all login attempts with timestamps, IP addresses, and AI analysis results. 📝
- **Streamlit Interface**: A clean and interactive UI for easy monitoring and analysis. 🖥️
- **Customizable**: Easily adapt the honeypot to your specific use case. 🛠️

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Groq API key (Sign up at [Groq](https://www.groq.com))

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/AI-Powered-Honeypot.git
   cd AI-Powered-Honeypot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Groq API key:
   - Replace `your_api_key` in the code with your actual Groq API key.
   - Alternatively, set it as an environment variable:
     ```bash
     export GROQ_API_KEY=your_api_key
     ```

4. Run the app:
   ```bash
   streamlit run ai_honeypot.py
   ```

---

## 🚀 Usage

1. Launch the app and navigate to the provided URL (e.g., `http://localhost:8501`).
2. Use the **User Login Attempt** form to simulate normal user login attempts.
3. Use the **Admin Login Attempt (Honeypot)** form to simulate admin-level attacks.
4. View the AI's analysis of each login attempt directly in the app interface.
5. Check the `honeypot.log` file for detailed logs of all activities.

---

## 📸 Screenshots

### User Login Attempt
| **EXAMPLE 1** |
|-----------------------------|
| ![User Login Attempt Example 1](https://github.com/user-attachments/assets/2e8007bc-f170-4029-bb7e-4e3b79a7c289) |

| **EXAMPLE 2** |
|-----------------------------|
| ![User Login Attempt Example 2](https://github.com/user-attachments/assets/058b9fdf-ac8e-4520-9bdd-453e91291ecf) |



### Admin Login Attempt (Honeypot)
| **EXAMPLE 1** |
|-----------------------------|
| ![Admin Login Attempt Example 1](https://github.com/user-attachments/assets/ba4f0ef8-b26a-4e4d-8eac-7bce4a735059) |

| **EXAMPLE 2** |
|-----------------------------|
| ![Admin Login Attempt Exmaple 2](https://github.com/user-attachments/assets/be7a16fb-03e0-454e-843d-9dd9fab2efe7) |


---

## 🤝 Contributing

We welcome contributions from the community! Here’s how you can help:

1. **Fork** the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m "Add YourFeatureName"`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a **Pull Request**.

For major changes, please open an issue first to discuss your ideas. 💡

---

## 🙏 Acknowledgments

- **Groq AI**: For providing the powerful AI model used in this project. 🧠
- **Streamlit**: For making it easy to build beautiful web apps. 🖥️
- **Open Source Community**: For inspiring us to create and share. ❤️

---

## 📞 Contact

Have questions or suggestions? Feel free to reach out:

- Email: gauravghandat12@gmail.com
- GitHub: [@yourusername](https://github.com/GauravGhandat-23)
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/gaurav-ghandat-68a5a22b4/)

---

🌟 **Make cybersecurity smarter with AI!** 🌟

---
