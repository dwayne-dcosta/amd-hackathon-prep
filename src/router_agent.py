# router_agent.py - Core Dynamic Routing Decision Logic

from config import TOKEN_LIMIT_LOCAL
from token_utils import count_tokens, estimate_processing_cost

def evaluate_and_route(task_query):
    """ 
    Analyzes an incoming hackathon task and dynamically selects 
    the most token efficient deployment pathway.
    """
    # 1. Calculate the real-time token footprint of the user query.
    tokens = count_tokens(task_query)

    # 2. Extract lower-case text to run semantic keyboard scans.
    query_lower = task_query.lower()

    # 3. Identify heavy logical triggers (e.g., complex coding or debugging tasks).
    logic_triggers = ["bug", "optimize", "architect", "quantum", "compile", "docker", "script", "leak"]
    requires_heavy_reasoning = any(trigger in query_lower for trigger in logic_triggers)

    # 4. Dynamic Routing Decision Tree Logic.
    if tokens > TOKEN_LIMIT_LOCAL:
        selected_route = "remote_premium"
        decision_reason = f"Token footprint ({tokens}) exceeds safe local context boundary of {TOKEN_LIMIT_LOCAL} tokens."

    elif requires_heavy_reasoning:
        selected_route = "remote_premium"
        decision_reason = "Query contains complex computer science parameters requiring deep reasoning matrices."
    
    else:
        selected_route = "local_cheap"
        decision_reason = "Query parameters are mathematically light and safe for local edge processing."

    # 5. Compute the projected financial cost tracking metric.
    simulated_cost = estimate_processing_cost(tokens, selected_route)

    # 6. Return a comprehensive structured packaging dictionary.
    return {
        "route": selected_route,
        "tokens": tokens,
        "estimated_cost": simulated_cost,
        "reasoning": decision_reason
    }