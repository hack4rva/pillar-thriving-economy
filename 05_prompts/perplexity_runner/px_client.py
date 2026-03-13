"""
Placeholder Perplexity client. Paste your boilerplate here.

Expected interface (example):

class PerplexityClient:
    def __init__(self, api_key: str | None = None):
        ...

    def create_response(self, *, preset: str, input_text: str, instructions: str | None = None,
                         model: str | None = None, **params) -> dict:
        """Return raw API response as dict, including generated text and search_results."""
        ...

The runner scripts will call `create_response(...)` and expect a dict containing:
- output_text (str)
- search_results (list[dict]) — each with title, url, date if available
- model (str)
- meta (dict) — optional
"""

import os


class PerplexityClient:  # pragma: no cover - stub
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("PERPLEXITY_API_KEY")
        if not self.api_key:
            raise RuntimeError("PERPLEXITY_API_KEY not set. Add it to .env or environment.")

    def create_response(self, *, preset: str, input_text: str, instructions: str | None = None,
                         model: str | None = None, **params) -> dict:
        raise NotImplementedError(
            "Replace px_client.PerplexityClient with your Perplexity boilerplate implementation."
        )

