from genai_healer.locator_healer import heal_locator

# Simulate a broken locator
broken_locator = "//input[@id='username_email_input']"
healed = heal_locator(broken_locator, module="test_login")

print(f"\nFinal result: {healed if healed else 'No match found'}")
