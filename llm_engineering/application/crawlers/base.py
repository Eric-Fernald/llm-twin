from abc import ABC, abstractmethod
import time
from tempfile import mkdtemp
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from llm_engineering.domain.documents import NoSQLBaseDocument

chromedriver_autoinstaller.install()

class BaseCrawler(ABC):
    model: type[NoSQLBaseDocument]

    @abstractmethod
    def extract(self, link: str, **kwargs) -> None: ...

class BaseSeleniumCrawler(BaseCrawler, ABC):
    def __init__(self, scroll_limit: int = 5) -> None:
        options = webdriver.ChromeOptions()

        options.add_argument("--no-sandbox")
        options.add_argument("--headless-new")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("--log-level-3")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-background-networking")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument(f"--user-data-dir={mkdtemp()}")
        options.add_argument(f"--data-path={mkdtemp()}")
        options.add_argument(f"--disk-cache-dir={mkdtemp()}")
        options.add_argument("--remote-debugging-port=9226")

        self.set_extra_driver_options(options)
        self.scroll_limit = scroll_limit
        self.driver = webdriver.Chrome(options=options,)

    def set_extra_driver_options(self, options: Options) -> None:
        pass

    def login(self) -> None:
        pass