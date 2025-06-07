from genai_healer.auto_suggestor.suggester import capture_dom, extract_locators_from_dom, generate_script_from_suggestions

def test_suggestion_workflow():
    url = url = "https://rahulshettyacademy.com/loginpagePractise/"
  # Replace with actual URL for testing
    html = capture_dom(url)
    suggestions = extract_locators_from_dom(html)

    assert suggestions, "No locators were extracted."

    script = generate_script_from_suggestions(suggestions, url)
    assert "driver.get" in script
    assert "find_element" in script

