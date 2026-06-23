# token_utils.py - Token Counting & Cost Estimation Engine
import tiktoken

def count_tokens(text_input):
    """
    Takes a string of text and returns the exact token count using 
    the industry-standard cl100k_base tokenizer layout.
    """

    # Load the core token decoder architecture
    tokenizer = tiktoken.get_encoding("cl100k_base")

    # Convert the plain text string into a list of numeric token IDs
    encoded_tokens = tokenizer.encode(text_input)

    # Calculate the numerical length of the token list
    token_count = len(encoded_tokens)

    return token_count

def estimate_processing_cost(token_count, routing_target):
    """
    Calculates a mock operational dollar cost based on the number of 
    tokens and where the query is headed.
    """

    if routing_target == "remote_premium":
        # Remote premium models charge money per million tokens (e.g., $0.15 / 1M tokens).
        cost_per_token = 0.15 / 1_000_000 
        total_cost = token_count * cost_per_token
    else:
        # Local open-weight models running on a CPU/GPU are completely free!
        total_cost = 0.00

    return total_cost