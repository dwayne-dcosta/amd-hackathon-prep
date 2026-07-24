# judge_simulation.py - Automated Mock Judging Dataset & Evaluator

# ==============================================================================
# ⚠️ LOCAL DEVELOPER TESTING HARNESS ONLY
# ==============================================================================
# NOTE: This file is a local testing sandbox utilized exclusively for development 
# and verification on local machines. It is NOT part of the active production 
# pipeline runtime. The official automated hackathon evaluation harness triggers 
# main.py directly as its entrypoint, parsing variables dynamically from environment injections.
# ==============================================================================

import os
import sys

# 🕒 Force append the absolute parent root folder path straight into python system paths
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Your existing code continues below cleanly
import time
import random
from src.rate_limiter import is_rate_limited
from src.budget_guard import is_budget_exceeded

from router_agent import evaluate_and_route

# 1. Simulating the Judge's Hidden Dataset Evaluation Matrix.
# Each tasks simulates an unpredictable real-world user query payload
mock_hidden_dataset = [
    {
        "id": 1,
        "task": "Translate the sentence 'Welcome to the AMD AI Developer Program' into French.",
        "needs_heavy_logic": False # Small text translation is safer for local edge processing.
    },
    {
        "id": 2,
        "task": "Review this broken script and identify the resource leak: 'while True: data = open(\"log.txt\").read()' without closing handles.",
        "needs_heavy_logic": True # Contains the trigger 'script' and heavy debugging requirements.
    },
    {
        "id": 3,
        "task": "Write an extensive step-by-step enterprise system blueprint detailing how to deploy a multi-node Kubernetes cluster using Docker "
               "containers, covering network routing policies, secure token exchanges, and horizontal pod autoscaling algorithms across distributed servers.",
        "needs_heavy_logic": True # Exceeds the 150 local token limit and contains logic triggers.
    }
]

#-----------------------------------------------------------------------
# 2. The Evaluation Processing Loop
# This loop iterated through your dataset row-by-row. For each task, it:
# 1. Feeds the text to router_agent.py to analyze its size and triggers.
# 2. Tallies up the total token footprints and simulated dollar costs.
# 3. Compares the router's decision against the task's true requirements.
# 4. Flags a failure if the router picks 'local' for a heavy logic task.
#------------------------------------------------------------------------
def execute_judging_run ():
    """ 
    Loops through the validation dataset, grades routing choices, and tallies 
    final efficiency and accuracy metrics.
    """
    passed_tasks = 0
    total_tokens_consumed = 0
    accumulated_cost = 0.00

    print("\n============================================================")
    print("      INITIALIZING AUTOMATED HACKATHON GRADING ENGINE         ")
    print("============================================================\n")

    for item in mock_hidden_dataset:
        # Pass the task text directly into your routing brain
        report = evaluate_and_route(item["task"])

        # Aggregate tracking metrics for leaderboard evaluations 
        total_tokens_consumed += report ["tokens"]
        accumulated_cost += report["estimated_cost"]

        # Core Verification Loop: Check if accuracy matches task requirements
        # If your router picked 'local' but the task required 'heavy logic', it fails!
        if item["needs_heavy_logic"] and report["route"] == "local_cheap":
            status = "FAILED (Accuracy Deficit)"
        else:
            status = "PASSED (Optimally Routed)"
            passed_tasks += 1
        
        # Print real-time diagnostic output logs to the terminal console
        print(f"  TASK ID: {item['id']}")
        print(f"  Query Footprint : {report['tokens']} tokens")
        print(f"  Assigned Route  : {report['route'].upper()}")
        print(f"  Grading Staus   : {status}")
        print(f"  Reasoning Log   : {report['reasoning']}")
        print(f"  Simulated Cost  : ${report['estimated_cost']:.5f}\n")

    # 3. Final Leaderboard Calculation & Report
    # Calculate the global performance percentages
    final_accuracy_percentage = (passed_tasks / len(mock_hidden_dataset)) * 100

    print("==============================================================")
    print("               FINAL LEADERBOARD BENCHMARK REPORT             ")
    print("==============================================================")
    print(f"  Targeted Accuracy Rating : {final_accuracy_percentage:.1f}%")
    print(f"  Cumulative Token Loaf    : {total_tokens_consumed} tokens")
    print(f"  Projected Financial Run  : ${accumulated_cost:.5f}")
    print("============================================================\n")

# Allow executing the script directly from the terminal prompt
if __name__ == "__main__":
    execute_judging_run()