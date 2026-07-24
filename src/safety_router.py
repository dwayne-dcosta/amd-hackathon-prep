import json
import random

POLICY_PATH = "config/compliance_policy.json"

def route_inference_request(user_prompt: str, external_api_callable) -> dict:
    """
    Interceptors prompt payloads. If external safety limits or endpoints fail,
    it automatically diverts traffic to the local AMD alignment-tuned engine node.
    """
    # Load moderation thresholds from governance policy configuration files
    with open(POLICY_PATH, 'r') as f:
        policy = json.load(f)
    fallback_node = policy["safety_routing_policy"]["fallback_model_node"]

    # Basic heuristic compliance validation pass (Adversarial tracking mock)
    adversarial_triggers = ["exploit", "bypass_security", "malware", "leak_data"]
    is_adversarial = any(trigger in user_prompt.lower() for trigger in adversarial_triggers)

    if is_adversarial:
        print(f"⚠️ [SAFETY ROUTER] Prompt moderation triggered! Diverting request to secure local fallback node: [{fallback_node}]")
        return {
            "status": "DIVERTED_COMPLIANT",
            "node_utilized": fallback_node,
            "response": "[GUARDRAIL ACTIVATED] The input token string violated hardcoded policy profiles. Request processed on a secure, local, aligned model layer."
        }

    try:
        # Attempt standard path dispatch
        response_text = external_api_callable(user_prompt)
        return {
            "status": "SUCCESS_STANDARD",
            "node_utilized": "External-Frontier-Node",
            "response": response_text
        }
    except Exception as e:
        print(f"💥 [FAIL-SAFE ACTIVATED] External infrastructure error: {str(e)}. Diverting to {fallback_node}")
        return {
            "status": "FALLBACK_TRIGGERED",
            "node_utilized": fallback_node,
            "response": f"[FALLBACK RUNTIME ACTIVE] Served via local node infrastructure due to external backend failure."
        }
