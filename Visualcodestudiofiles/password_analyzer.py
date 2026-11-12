import re
import getpass

COMMON_PASSWORDS = {
"password", "password123", "123456",
"12345678", "qwerty", "admin123",
"letmein", "welcome123"
}

def analyze_password(password):
"""Evaluate a password using basic security checks."""

checks = {
    "At least 15 characters": len(password) >= 15,
    "Contains uppercase letters": bool(re.search(r"[A-Z]", password)),
    "Contains lowercase letters": bool(re.search(r"[a-z]", password)),
    "Contains numbers": bool(re.search(r"\d", password)),
    "Contains special characters": bool(
        re.search(r"[^A-Za-z0-9]", password)
    )
}

score = sum(checks.values())
suggestions = []

if len(password) < 15:
    suggestions.append("Use at least 15 characters.")

if not checks["Contains uppercase letters"]:
    suggestions.append("Consider adding uppercase letters.")

if not checks["Contains lowercase letters"]:
    suggestions.append("Consider adding lowercase letters.")

if not checks["Contains numbers"]:
    suggestions.append("Consider adding numbers.")

if not checks["Contains special characters"]:
    suggestions.append("Consider adding special characters.")

lower_password = password.lower()

if lower_password in COMMON_PASSWORDS:
    score = 0
    suggestions.append("Avoid commonly used passwords.")

if re.search(r"(.)\1{3,}", password):
    score = max(0, score - 1)
    suggestions.append("Avoid repeated characters.")

if re.search(r"1234|abcd|qwerty", lower_password):
    score = max(0, score - 1)
    suggestions.append("Avoid predictable sequences.")

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Moderate"
else:
    strength = "Strong"

return strength, score, checks, suggestions
def main():
print("=== Password Strength Analyzer ===")

password = getpass.getpass("Enter a test password: ")

strength, score, checks, suggestions = analyze_password(password)

print("\n--- Analysis Results ---")
print(f"Password Length: {len(password)}")
print(f"Strength: {strength}")
print(f"Score: {score}/5")

print("\nSecurity Checks:")
for check, passed in checks.items():
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {check}")

print("\nRecommendations:")
if suggestions:
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("No basic weaknesses identified.")

print("\nNote: This is an educational heuristic,")
print("not a guarantee that the password is secure.")
if name == "main":
main()
