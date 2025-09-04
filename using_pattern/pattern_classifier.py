import re

regex_patterns = {
    "runtime error: invalid memory address or nil pointer dereference" : "TEST",
    "timed out when waiting for image-controller annotations to be updated on component": "INTERMITTENT",
}

def classify_using_regex(log_msg):
    for pattern, category in regex_patterns.items():
        if re.search(pattern, log_msg, re.IGNORECASE):
            return category
    return "UNKNOWN"

def main():
    print("Running Regex classifier")
    log_msg = "runtime error: invalid memory address or nil pointer dereference"
    category = classify_using_regex(log_msg)
    print(category)

if __name__ == '__main__':
    main()