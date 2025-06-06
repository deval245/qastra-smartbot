# dashboard/components/prediction_card.py

import streamlit as st

def show_prediction_stats():
    st.subheader("📊 Flaky Test Prediction Summary")
    st.metric(label="Predicted Flaky Tests", value="3/10", delta="-1 vs last run")
    st.progress(0.3)
    st.markdown("Flakiness confidence based on ML model for module `test_login`, `test_checkout`, and `test_dashboard`.")
