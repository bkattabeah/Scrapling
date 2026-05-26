"""Scrapling - A powerful, flexible web scraping library.

Scrapling provides a high-level interface for web scraping with support
for both static and dynamic content, smart element matching, and
automatic adaptation to website changes.

Basic Usage:
    >>> from scrapling import Fetcher, AsyncFetcher
    >>> page = Fetcher().get('https://example.com')
    >>> title = page.find('h1').text

For dynamic content (JavaScript-rendered pages):
    >>> from scrapling import PlaywrightFetcher
    >>> page = PlaywrightFetcher().fetch('https://example.com')

For async usage:
    >>> import asyncio
    >>> from scrapling import AsyncFetcher
    >>> page = asyncio.run(AsyncFetcher().get('https://example.com'))
"""

__version__ = "0.2.9"
__author__ = "D4Vinci"
__license__ = "MIT"

# Personal fork: added AsyncFetcher async usage example to docstring
# and exposed the __author__ and __license__ in __all__ for convenience
from scrapling.core.page import Adaptor
from scrapling.fetchers import (
    Fetcher,
    AsyncFetcher,
    PlaywrightFetcher,
    StealthyFetcher,
)

__all__ = [
    "Adaptor",
    "Fetcher",
    "AsyncFetcher",
    "PlaywrightFetcher",
    "StealthyFetcher",
    "__version__",
    "__author__",
    "__license__",
]
