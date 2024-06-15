from cachetools import TTLCache

# Cache com expiração após 10 minutos
cache = TTLCache(maxsize=100, ttl=600)
