import os
import sys
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta, timezone

# 🕒 Explicitly step backward out of telemetry/ to find the src/ root components
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

def render_advanced_dashboard(telemetry_file_path="output/telemetry_analytics.csv"):
    st.markdown("## 📊 System Monitoring & Governance Command Center")
    st.write("Real-time edge-to-cloud performance tracking and automated budget circuit breakers.")
    st.write("----")

    # Ensure the database ledger directory structure exists cleanly
    if not os.path.exists(telemetry_file_path):
        st.info("📡 Ingestion channel clear. Waiting for system traffic logs to populate...")
        return

    # Ingest ledger dataframe matrix
    df = pd.read_csv(telemetry_file_path)

    if df is not None and not df.empty:
        # 🗓️ Ensure proper datetime formatting, forcing invalid entries to NaT null markers
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df = df.dropna(subset=['timestamp'])
        
        # 🧼 Enforce robust numeric type-casting on cost columns to prevent value errors
        df['precision_cost'] = pd.to_numeric(df['precision_cost'], errors='coerce').fillna(0.0)

        # Compute core operational analytics parameters
        total_requests = len(df)
        total_spend = df['precision_cost'].sum()
        
        # Display professional layout metric grids
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Total Processed Requests", value=f"{total_requests} Logs")
        with col2:
            st.metric(label="Cumulative Infrastructure Spend", value=f"${total_spend:.6f}")
            
        st.write("### Raw Telemetry Audit Trail")
        st.dataframe(df.tail(20), use_container_width=True)

if __name__ == "__main__":
    render_advanced_dashboard()
