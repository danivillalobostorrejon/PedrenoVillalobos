from .proxies import get_proxies

###########################
# Main configuration
###########################

BOT_NAME = 'eci'

SPIDER_MODULES = ['eci.spiders']
NEWSPIDER_MODULE = 'eci.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620    
}

DEFAULT_REQUEST_HEADERS = {
    'authority': 'www.elcorteingles.com',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest':' document'
}

FEED_EXPORT_ENCODING='latin-1'

DOWNLOAD_TIMEOUT = 10


###########################
# User agent configurarion
###########################

USER_AGENTS = [
    
    # Add more user agents which actually work nowadays
]

#########################
# Proxies configuration
#########################

RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]

ROTATING_PROXY_PAGE_RETRY_TIMES = 99999999999 # TODO: is it possible to setup this parameter with no limit?
ROTATING_PROXY_LIST = get_proxies()