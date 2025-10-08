import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://musicuser:musicpass@db:5432/musicdb")

