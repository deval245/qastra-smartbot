# dashboard/app.py

import streamlit as st
from components.prediction_card import show_prediction_stats
from components.image_diff_viewer import show_image_diffs
from components.healed_locator_log import show_healing_logs

st.set_page_config(page_title="Qastra Dashboard", layout="wide")

st.title("📊 Qastra SmartBot Dashboard")

tab1, tab2, tab3 = st.tabs([
    "🧠 Flaky Predictions",
    "🖼️ Visual Validator",
    "📂 Healed Locators"
])

with tab1:
    show_prediction_stats()

with tab2:
    show_image_diffs()

with tab3:
    show_healing_logs()
