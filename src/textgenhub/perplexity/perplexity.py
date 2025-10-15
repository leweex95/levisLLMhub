"""
Perplexity provider - Simple and clean implementation
"""
from ..core.provider import SimpleProvider


def ask(prompt: str, headless: bool = True, remove_cache: bool = True) -> str:
    """
    Send a prompt to Perplexity and get a response.
    
    Args:
        prompt (str): The prompt to send to Perplexity
        headless (bool): Whether to run browser in headless mode
        remove_cache (bool): Whether to remove browser cache
        
    Returns:
        str: The response from Perplexity
    """
    provider = SimpleProvider("perplexity", "perplexity_cli.js")
    return provider.ask(prompt, headless, remove_cache)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Perplexity AI CLI via Node.js wrapper")
    parser.add_argument("--prompt", type=str, required=True, help="Prompt to send to Perplexity AI")
    parser.add_argument("--headless", type=lambda x: x.lower() == "true", default=True, help="Run Node in headless mode")
    parser.add_argument("--remove-cache", type=lambda x: x.lower() == "false", default=False, help="Remove cache on cleanup")

    args = parser.parse_args()

    resp = ask(args.prompt, headless=args.headless, remove_cache=args.remove_cache)
    print("Response returned from ask method: ", resp)