from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: str
    REDIS_PASSWORD: str

    @property
    def redis_url(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"


class GitHubSettings(BaseSettings):
    GITHUB_API_TOKEN: str


class Settings(RedisSettings, GitHubSettings):
    class Config:
        case_sensitive = True
        env_file = "../.env"


settings = Settings()
