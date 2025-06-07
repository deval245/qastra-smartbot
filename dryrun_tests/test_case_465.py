
from components.healer_runner import auto_heal_run

def test_autoheal_465():
    html = """<input id='user_login' placeholder='Enter email'>"""
    broken_locator = "//*[@idd='user_login']"
    result = auto_heal_run(broken_locator, html, module="test_case_465")
    assert result is not None
