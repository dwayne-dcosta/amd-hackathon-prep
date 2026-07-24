import time
import streamlit as st

# Define tier-specific transaction limits per 60-second window
TIER_LIMITS = {
    "FREE": {"max_requests": 5, "window_size": 60},
    "DEVELOPER": {"max_requests": 30, "window_size": 60},
    "ENTERPRISE": {"max_requests": 100, "window_size": 60}
}

def is_rate_limited(client_token: str, tier: str = "FREE") -> tuple[bool, int]:
    """
    Evaluates rate-limiting parameters using an in-memory sliding window matrix.
    Returns a tuple: (is_limited, remaining_requests).
    """
    if tier not in TIER_LIMITS:
        tier = "FREE"
        
    config = TIER_LIMITS[tier]
    now = time.time()
    
    # Initialize global in-memory transaction cache if absent
    if "rate_limit_cache" not in st.session_state:
        st.session_state.rate_limit_cache = {}
        
    # Initialize specific tracking slot for incoming client identity
    if client_token not in st.session_state.rate_limit_cache:
        st.session_state.rate_limit_cache[client_token] = []
        
    # Extract timestamps and filter out stale entries outside the rolling window
    timestamps = st.session_state.rate_limit_cache[client_token]
    valid_timestamps = [ts for ts in timestamps if now - ts < config["window_size"]]
    
    # Update cache matrix with cleaned entries
    st.session_state.rate_limit_cache[client_token] = valid_timestamps
    
    # Evaluate capacity bounds
    if len(valid_timestamps) >= config["max_requests"]:
        return True, 0
        
    # Append valid current transaction timestamp and compute clearance room
    st.session_state.rate_limit_cache[client_token].append(now)
    remaining_requests = config["max_requests"] - len(st.session_state.rate_limit_cache[client_token])
    
    return False, remaining_requests
