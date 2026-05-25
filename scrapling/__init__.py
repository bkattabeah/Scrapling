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
"""

__version__ = "0.2.9"
__author__ = "D4Vinci"
__license__ = "MIT"

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
]
