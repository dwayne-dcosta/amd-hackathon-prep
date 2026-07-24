import os
import json
import time
from datetime import datetime, timedelta

POLICY_PATH = "config/compliance_policy.json"

def enforce_data_lifecycle_purge(telemetry_file_path="output/telemetry_analytics.csv"):
    print("🧹 [COMPLIANCE ENGINE] Initializing data lifecycle lifecycle audit check...")
    
    # Read the hardcoded corporate governance guidelines
    try:
        with open(POLICY_PATH, 'r') as f:
            policy = json.load(f)
        retention_days = policy["data_lifecycle_policy"]["cache_retention_days"]
    except Exception:
        retention_days = 60 # Fail-safe strict default configuration
        
    if not os.path.exists(telemetry_file_path):
        print(" -> No log buffers found. Ingestion pristine.")
        return True

    now = datetime.utcnow()
    purge_boundary = now - timedelta(days=retention_days)
    retained_rows = []
    purged_count = 0

    # Parse and filter rows based on the policy boundary
    with open(telemetry_file_path, 'r') as f:
        lines = f.readlines()
        if not lines:
            return True
        header = lines[0]
        retained_rows.append(header)
        
        for line in lines[1:]:
            parts = line.split(',')
            if not parts:
                continue
            try:
                # Ingest isolation timestamp string row
                log_time = datetime.strptime(parts[0].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                if log_time > purge_boundary:
                    retained_rows.append(line)
                else:
                    purged_count += 1
            except Exception:
                retained_rows.append(line) # Protect anomalies from unverified drops

    # Write cleaned rows back to disk
    with open(telemetry_file_path, 'w') as f:
        f.writelines(retained_rows)

    print(f"✅ [COMPLIANCE ENGINE] Audit complete. Purged {purged_count} expired records tracking past the {retention_days}-day limit.")
    return True

if __name__ == "__main__":
    enforce_data_lifecycle_purge()
