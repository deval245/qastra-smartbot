import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def suggest_locator_fix(failed_locator, html_snippet=None):
    prompt = f"""
You are a QA automation assistant.

A Selenium test failed due to a broken XPath locator: {failed_locator}.

Analyze and suggest the best possible corrected XPath or CSS locator.

HTML context (if any): {html_snippet if html_snippet else "N/A"}

Return only the corrected locator string.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"[❌] Ollama API error: {e}")
        return None
