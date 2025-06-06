# dashboard/components/image_diff_viewer.py

import streamlit as st
from PIL import Image
import os


def show_image_diffs():
    st.subheader("🖼️ Visual Difference Viewer")

    module = st.selectbox("Select module to compare:", options=["test_login", "test_checkout", "test_dashboard"])

    baseline_path = f"visual_validator/baseline_store/{module}.png"
    captured_path = f"visual_validator/captured_screens/{module}.png"

    if os.path.exists(baseline_path) and os.path.exists(captured_path):
        col1, col2 = st.columns(2)

        with col1:
            st.image(Image.open(baseline_path), caption="Baseline Image", use_column_width=True)

        with col2:
            st.image(Image.open(captured_path), caption="Captured Image", use_column_width=True)

        st.success(f"✅ Images loaded successfully for `{module}`")
    else:
        st.warning(f"⚠️ Image not found for module: `{module}`")
