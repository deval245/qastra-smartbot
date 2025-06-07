from genai_healer.locator_healer import heal_locator
from genai_healer.genai_adapter import suggest_locator_fix

def auto_heal_run(failed_locator, html, module):
    print(f"[🛠️] Attempting to heal locator: {failed_locator}")
    
    fallback = heal_locator(failed_locator, module)
    if fallback:
        return fallback

    # Use GenAI if fuzzy fails
    suggestion = suggest_locator_fix(failed_locator, html)
    if suggestion:
        print(f"[🤖] GenAI Suggestion: {suggestion}")
        return suggestion

    return None

