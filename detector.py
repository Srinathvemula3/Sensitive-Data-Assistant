import re

patterns = {
    "Email Addresses": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "Phone Numbers": r"\b[6-9]\d{9}\b",
    "Aadhaar Numbers": r"\b\d{4}\s?\d{4}\s?\d{4}\b",
    "PAN Numbers": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
    "Credit Card Numbers": r"\b(?:\d[ -]*?){13,16}\b",
    "Passwords": r"(?i)(password\s*[:=]\s*\S+|pwd\s*[:=]\s*\S+)",
    "API Keys": r"(sk-[A-Za-z0-9_\-]{20,}|AIza[0-9A-Za-z\-_]{35}|ghp_[A-Za-z0-9]{36})",
    "Employee IDs": r"\bEMP\d{3,6}\b"
}


def detect_sensitive_data(text):
    results = {}

    for name, pattern in patterns.items():
        matches = re.findall(pattern, text)

        if matches:
            results[name] = matches

    return results


def classify_risk(results):

    score = 0

    weights = {
        "Email Addresses": 1,
        "Phone Numbers": 1,
        "Employee IDs": 2,
        "PAN Numbers": 3,
        "Aadhaar Numbers": 3,
        "Credit Card Numbers": 5,
        "Passwords": 5,
        "API Keys": 5,
    }

    for item, values in results.items():
        score += len(values) * weights.get(item, 1)

    if score >= 10:
        return "🔴 HIGH"

    elif score >= 5:
        return "🟡 MEDIUM"

    return "🟢 LOW"