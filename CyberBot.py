import nltk
from nltk.tokenize import word_tokenize
import random

nltk.download('punkt')  # Download NLTK data (if not already downloaded)

# Add a variable to store the previous user question
previous_question = ""

# Responses dictionary with 50 responses
responses = {
    "hello": "Hello! How can I assist you with cybersecurity and online safety today?",
    # Responses dictionary with 50 responses
    "phishing": "Phishing is a type of cyber fraud where attackers use fake emails or websites to trick people into revealing sensitive information like passwords or credit card details.",
    "malware": "Malware is malicious software that can harm your computer. It includes viruses, Trojans, and spyware.",
    "protect online accounts": "To protect your online accounts, use strong and unique passwords for each account, enable two-factor authentication, and be cautious of suspicious emails or links.",
    "suspicious email": "If you receive a suspicious email, don't click on any links or download attachments. Report it as spam or phishing to your email provider.",
    "voice assistant security": "Voice assistants can pose security risks. Review and adjust privacy settings, and be cautious of voice commands that can lead to unintended actions.",
    "public charging stations": "Avoid using public charging stations for your devices, as they can pose security risks. Use your charger or a portable power bank.",
    "cybersecurity jobs": "Cybersecurity is a growing field. Consider a career in cybersecurity to help organizations protect against cyber threats.",
    "online dating safety": "Stay safe while online dating by not sharing personal information too soon and arranging to meet in public places.",
    "safe online forums": "Choose online forums with active moderation to ensure a safer and more secure online community.",
    "password manager": "Consider using a password manager to generate and store strong, unique passwords for all your online accounts.",
    "internet of things (IoT) security": "Secure your IoT devices by changing default passwords, updating firmware, and isolating them on a separate network if possible.",
    "phishing awareness training": "Phishing awareness training can help employees recognize and respond to phishing attempts effectively.",
    "security updates": "Regularly update your operating system and software to patch security vulnerabilities and protect your devices.",
    "browser security": "Use browsers with built-in security features and regularly clear your browser cache and cookies for enhanced security.",
    "mobile app security": "Before downloading mobile apps, review their permissions, read reviews, and download from trusted app stores.",
    "wireless network security": "Secure your wireless network by using WPA3 encryption, changing the default router login credentials, and enabling a strong passphrase.",
    "data encryption": "Encrypt sensitive data to protect it from unauthorized access. Use encryption tools and secure storage solutions.",
    "dark web monitoring": "Consider using dark web monitoring services to check if your personal information is being traded on the dark web.",
    "incident response plan": "Develop an incident response plan to quickly and effectively respond to cybersecurity incidents within your organization.",
    "secure email communication": "Secure email communication by using end-to-end encryption tools and verifying the authenticity of email senders.",
    "online shopping safety": "When shopping online, use reputable websites, check for secure payment options, and be cautious of offers that seem too good to be true.",
    "social engineering attacks": "Social engineering attacks manipulate individuals into divulging confidential information. Be cautious of unsolicited requests for personal or financial information.",
    "firewall protection": "Firewalls help block unauthorized access to your devices or network. Enable firewalls and keep them updated for added security.",
    "data backup best practices": "Regularly back up your important data to an external drive or cloud storage to prevent data loss in case of cyber incidents.",
    "internet safety for children": "Monitor your child's online activities, set parental controls, and educate them about the potential risks of sharing personal information online.",
    "avoiding clickbait": "Be skeptical of sensational headlines and clickbait. Verify information from trusted sources before clicking on links or sharing content.",
    "online privacy tips": "Protect your online privacy by using VPNs, adjusting privacy settings on social media, and limiting the sharing of personal information online.",
    "secure remote work": "When working remotely, use secure VPNs, enable multi-factor authentication, and follow your organization's security guidelines.",
    "safe online payments": "Use secure payment methods and verify the legitimacy of online sellers before making payments for goods or services.",
    "smartphone security": "Secure your smartphone with PINs or biometrics, keep software updated, and be cautious of app permissions.",
    "computer antivirus software": "Install reputable antivirus software to protect your computer from malware and other threats. Keep it updated for optimal security.",
    "internet router security": "Change default router passwords, use WPA3 encryption, and regularly update router firmware to secure your home network.",
    "identity theft prevention": "Protect against identity theft by monitoring your credit report, shredding sensitive documents, and being cautious of sharing personal information.",
    "safe social media usage": "Use privacy settings on social media platforms to control who can see your posts and limit the sharing of personal information.",
    "secure online gaming": "When gaming online, use strong and unique passwords, avoid sharing personal information, and be cautious of in-game scams.",
    "cybersecurity for small businesses": "Small businesses should invest in cybersecurity measures, including employee training and regular security assessments.",
    "ransomware protection": "Protect against ransomware by regularly backing up data, avoiding suspicious email attachments, and keeping security software up to date.",
    "safe video conferencing": "Use secure video conferencing platforms with password protection and waiting room features to prevent unauthorized access.",
    "cloud security best practices": "When using cloud services, enable two-factor authentication, encrypt sensitive data, and monitor account activity for signs of compromise.",
    "online dating safety tips": "Stay safe while online dating by arranging to meet in public places, sharing information cautiously, and trusting your instincts.",
    "social media privacy": "Review and adjust privacy settings on social media platforms to control who can see your posts and limit data sharing.",
    "cybersecurity certifications": "Consider obtaining cybersecurity certifications like CompTIA Security+ or CISSP to advance your career in cybersecurity.",
    "safe online chat rooms": "Use reputable online chat rooms with moderation and reporting features to ensure a safer and more secure chatting experience.",
    "email phishing protection": "To protect against email phishing, verify sender information, avoid clicking on suspicious links, and report phishing attempts.",
    "mobile device updates": "Regularly update your mobile device's operating system and apps to patch security vulnerabilities and protect your data.",
    "internet scams awareness": "Be aware of common internet scams like lottery scams, advance fee fraud, and phishing attempts. Be cautious of unsolicited offers.",
    "strong password creation": "Create strong passwords by using a combination of uppercase and lowercase letters, numbers, and symbols. Avoid using easily guessable information.",
    "online privacy tools": "Use online privacy tools like ad blockers, tracker blockers, and VPNs to enhance your online privacy and security.",
    "safe online forums": "Participate in online forums with active moderation to ensure a safer and more secure community for discussions.",
    "cybersecurity for seniors": "Seniors should be cautious of online scams, protect personal information, and seek cybersecurity education to stay safe online."
}

# Create an empty list to store the conversation
conversation_history = []

def save_conversation(filename):
    # Save the conversation history to a text file
    with open(filename, 'w') as file:
        for turn in conversation_history:
            file.write(f"{turn['user']}\n")
            file.write(f"{turn['bot']}\n")

def load_conversation(filename):
    # Load a conversation from a text file and add it to the conversation history
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            user_input = lines[i].strip()
            bot_response = lines[i + 1].strip()
            conversation_history.append({"user": user_input, "bot": bot_response})

# cyberbot.py
def cyberbot(user_input):
    global previous_question

def cyberbot_response(user_input):
    # Tokenize user input
    words = user_input.lower().split()  # Convert input to lowercase and split into words

    if "hello" in words:
        return responses["hello"]

    if "phishing" in words:
        return responses["phishing"]

    elif "malware" in words:
        return responses["malware"]

    # Add more conditions for other keywords and responses...

    elif "protect online accounts" in user_input.lower():
        return responses["protect online accounts"]

    elif "suspicious email" in user_input.lower():
        return responses["suspicious email"]

    elif "voice assistant security" in user_input.lower():
        return responses["voice assistant security"]

    elif "public charging stations" in user_input.lower():
        return responses["public charging stations"]

    elif "cybersecurity jobs" in user_input.lower():
        return responses["cybersecurity jobs"]

    elif "online dating safety" in user_input.lower():
        return responses["online dating safety"]

    elif "safe online forums" in user_input.lower():
        return responses["safe online forums"]

    elif "password manager" in user_input.lower():
        return responses["password manager"]

    elif "internet of things (IoT) security" in user_input.lower():
        return responses["internet of things (IoT) security"]

    elif "phishing awareness training" in user_input.lower():
        return responses["phishing awareness training"]

    elif "security updates" in user_input.lower():
        return responses["security updates"]

    elif "browser security" in user_input.lower():
        return responses["browser security"]

    elif "mobile app security" in user_input.lower():
        return responses["mobile app security"]

    elif "wireless network security" in user_input.lower():
        return responses["wireless network security"]

    elif "data encryption" in user_input.lower():
        return responses["data encryption"]

    elif "dark web monitoring" in user_input.lower():
        return responses["dark web monitoring"]

    elif "incident response plan" in user_input.lower():
        return responses["incident response plan"]

    elif "secure email communication" in user_input.lower():
        return responses["secure email communication"]

    elif "online shopping safety" in user_input.lower():
        return responses["online shopping safety"]

    elif "social engineering attacks" in user_input.lower():
        return responses["social engineering attacks"]

    elif "firewall protection" in user_input.lower():
        return responses["firewall protection"]

    elif "data backup best practices" in user_input.lower():
        return responses["data backup best practices"]

    elif "internet safety for children" in user_input.lower():
        return responses["internet safety for children"]

    elif "avoiding clickbait" in user_input.lower():
        return responses["avoiding clickbait"]

    elif "online privacy tips" in user_input.lower():
        return responses["online privacy tips"]

    elif "secure remote work" in user_input.lower():
        return responses["secure remote work"]

    elif "safe online payments" in user_input.lower():
        return responses["safe online payments"]

    elif "smartphone security" in user_input.lower():
        return responses["smartphone security"]

    elif "computer antivirus software" in user_input.lower():
        return responses["computer antivirus software"]

    elif "internet router security" in user_input.lower():
        return responses["internet router security"]

    elif "identity theft prevention" in user_input.lower():
        return responses["identity theft prevention"]

    elif "safe social media usage" in user_input.lower():
        return responses["safe social media usage"]

    elif "secure online gaming" in user_input.lower():
        return responses["secure online gaming"]

    elif "cybersecurity for small businesses" in user_input.lower():
        return responses["cybersecurity for small businesses"]

    elif "ransomware protection" in user_input.lower():
        return responses["ransomware protection"]

    elif "safe video conferencing" in user_input.lower():
        return responses["safe video conferencing"]

    elif "cloud security best practices" in user_input.lower():
        return responses["cloud security best practices"]

    elif "online dating safety tips" in user_input.lower():
        return responses["online dating safety tips"]

    elif "social media privacy" in user_input.lower():
        return responses["social media privacy"]

    elif "cybersecurity certifications" in user_input.lower():
        return responses["cybersecurity certifications"]

    elif "safe online chat rooms" in user_input.lower():
        return responses["safe online chat rooms"]

    elif "email phishing protection" in user_input.lower():
        return responses["email phishing protection"]

    elif "mobile device updates" in user_input.lower():
        return responses["mobile device updates"]

    elif "internet scams awareness" in user_input.lower():
        return responses["internet scams awareness"]

    elif "strong password creation" in user_input.lower():
        return responses["strong password creation"]

    elif "online privacy tools" in user_input.lower():
        return responses["online privacy tools"]

    elif "safe online forums" in user_input.lower():
        return responses["safe online forums"]

    elif "cybersecurity for seniors" in user_input.lower():
        return responses["cybersecurity for seniors"]

    else:
        return "I'm not quite sure what you mean. Could you please provide more details or rephrase your question?"
# Define a function to get a response
def get_response(user_input):
    user_input = user_input.lower()

    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    return "I'm not quite sure what you mean. Could you please provide more details or rephrase your question?"
# Main loop for user interaction
print("Welcome to CyberBot! I can provide information on cyber frauds and online security.")
conversation_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "goodbye":
        break

    response = get_response(user_input)
    print("CyberBot:", response)

    conversation_history.append({"user": user_input, "bot": response})

    if "save" in word_tokenize(user_input.lower()):
        filename = input("Enter a filename to save the conversation: ")
        save_conversation(filename)
        print(f"Conversation saved to '{filename}'")

    if "load" in word_tokenize(user_input.lower()):
        filename = input("Enter the filename of the conversation to load: ")
        try:
            load_conversation(filename)
            print(f"Conversation loaded from '{filename}'")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please make sure the file exists.")

    if "goodbye" in word_tokenize(user_input.lower()):
        conversation_ended = True

# Request feedback at the end of the conversation
rating = input("Rate this conversation: 1-5: ")
try:
    rating = int(rating)
    if 1 <= rating <= 5:
        print("Thank you for your feedback!")
    else:
        print("Invalid rating. Please provide a rating between 1 and 5.")
except ValueError:
    print("Invalid rating. Please provide a numeric rating between 1 and 5.")
