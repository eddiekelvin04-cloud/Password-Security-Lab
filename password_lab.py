import re
import hashlib

def check_password_strength(password):
    """
    Evaluates password strength based on length, casing, and special characters.
    """
    strength = 0
    feedback = []

    # Criteria 1: Length
    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("Increase length to at least 12 characters.")

    # Criteria 2: Uppercase & Lowercase
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Use a mix of uppercase and lowercase letters.")

    # Criteria 3: Numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    # Criteria 4: Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    return strength, feedback

def hash_password(password):
    """
    Demonstrates SHA-256 hashing (a core concept in Cryptography).
    """
    return hashlib.sha256(password.encode()).hexdigest()

# --- Main Lab Execution ---
print("--- Kelvin's Cybersecurity Lab: Password Security ---")
user_pwd = input("Enter a test password to evaluate: ")

score, suggestions = check_password_strength(user_pwd)
hashed_pwd = hash_password(user_pwd)

print(f"\n[+] Password Strength Score: {score}/4")

if score < 4:
    print("Suggestions for improvement:")
    for note in suggestions:
        print(f" - {note}")
else:
    print("[!] Strong password detected.")

print(f"\n[+] SHA-256 Hash of your password:\n{hashed_pwd}")
print("\nNote: In a real system, the original password is never stored; only this hash is saved.")
