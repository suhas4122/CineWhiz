OPENAI_API_KEY = "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"
VERBOSE = True
REDIS_URL = "redis://@localhost:6380"
INDEX_NAME = "database-index"
BASE_PATH = "./movie-recommender"

REDIS_EMBEDDING_PATH = f"{BASE_PATH}/data/embeddings/"
LANGCHAIN_CACHE_SQLITE_PATH = f"{BASE_PATH}/data/cache/.langchain.db"
SQL_DB_PATH = f"{BASE_PATH}/data/sqlite/movie.db"
TRENDS_STORE_PATH = f"{BASE_PATH}/scraper/data/vogue/summary.txt"
PURCHASE_HISTORY_PATH = f"{BASE_PATH}/user-data/purchase_history.txt"
MAX_DOCUMENTS = 10
SIMILARITY_THRESH = 0.6
LANGCHAIN_EMBEDDING_CACHE_PATH = f"{BASE_PATH}/data/cache/embeddings/"
JSON_PATH = f"{BASE_PATH}/scraper/movies.json"