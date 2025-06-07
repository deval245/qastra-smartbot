
from components.healer_runner import auto_heal_run

def test_autoheal_58():
    html = """<input name='username'>"""
    broken_locator = "//input[@nam='usernam']"
    result = auto_heal_run(broken_locator, html, module="test_case_58")
    assert result is not None
