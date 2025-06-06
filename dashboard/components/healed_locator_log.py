# dashboard/components/healed_locator_log.py

import streamlit as st

def show_healing_logs():
    st.subheader("🧠 GenAI Locator Healing Log")

    # Sample healing logs - replace with file/JSON integration if needed
    healing_log = [
        {
            "module": "test_login",
            "broken": "//input[@id='username_email_input']",
            "healed": "//input[@id='user_login']",
            "confidence": 84
        },
        {
            "module": "test_dashboard",
            "broken": "//div[@class='user-info']",
            "healed": "//div[contains(@class, 'user')]",
            "confidence": 79
        }
    ]

    for entry in healing_log:
        st.markdown(f"""
        **Module:** `{entry['module']}`  
        🔴 Broken: `{entry['broken']}`  
        🟢 Healed: `{entry['healed']}`  
        🧠 Confidence: **{entry['confidence']}%**  
        ---
        """)
