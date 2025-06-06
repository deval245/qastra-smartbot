import os
import pandas as pd
from datetime import datetime

def save_report(data: pd.DataFrame, report_type: str):
    date_str = datetime.now().strftime('%Y-%m-%d')
    folder_map = {
        "flaky": "reports/flaky",
        "visual": "reports/visual",
        "summary": "reports/summary"
    }

    if report_type not in folder_map:
        raise ValueError("Unsupported report type")

    folder = folder_map[report_type]
    os.makedirs(folder, exist_ok=True)
    filename = f"{report_type}_report_{date_str}.csv"
    filepath = os.path.join(folder, filename)
    data.to_csv(filepath, index=False)
    print(f"[✅] {report_type.capitalize()} report saved: {filepath}")
    return filepath
