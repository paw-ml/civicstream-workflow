from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "CivicStream"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # CORS - using hardcoded values in main.py for development
    # BACKEND_CORS_ORIGINS: List[str] = []
    
    # MongoDB
    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "civicstream"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Azure
    AZURE_STORAGE_CONNECTION_STRING: Optional[str] = None
    AZURE_STORAGE_CONTAINER_NAME: str = "civicstream-files"
    
    # Blockchain
    BLOCKCHAIN_API_URL: Optional[str] = None
    BLOCKCHAIN_API_KEY: Optional[str] = None
    
    # Document Storage
    DOCUMENT_STORAGE_PATH: str = "./storage/documents"
    MAX_DOCUMENT_SIZE_MB: int = 50
    DOCUMENT_BASE_URL: Optional[str] = None  # For serving files
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()