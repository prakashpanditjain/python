from dataclasses import dataclass , field, asdict

from sqlalchemy import True_


@dataclass
# Define a dataclass for ETL job configuration
class ETLConfig:
    source_path: str
    destination_path: str
    file_format: str = "parquet"
    partition_by: list[str] = field(default_factory=list)
    compression: str = "snappy"
    mode: str = "overwrite"

# Example usage
config = ETLConfig(
    source_path="/data/source",
    destination_path="/data/destination",
    file_format="csv",
    partition_by=["date"],
    compression="gzip",
    mode="append"
)

#print the config as dictionary
print(asdict(config))



###data class schema representation
@dataclass
class UserRecords:
    username: str
    user_id: int
    email: str
    is_active: bool = True

# Example usage
user = UserRecords(username="johndoe", user_id=123, email="as@gamil.com")
print(user.username)  # Output: johndoe





##validation with __post_init__
@dataclass
class JobConfig:
    job_name:str
    retries: int = 3
    partition: int = 2

    def __post_init__(self):
        if self.retries < 0 :
            raise ValueError("Retries must be non-negative")
        if self.partition <= 0:
            raise ValueError("Partition must be positive")

job = JobConfig("example_job", retries=2, partition=3)
print(job)






##create database connection string

@dataclass(frozen=True)
class DatabaseConfig:
    username: str
    password: str
    host: str
    port: int
    database: str

def connection_config(db_config:DatabaseConfig):
    return f"postgresql://{db_config.username}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.database}"


db_config = DatabaseConfig(
    username="admin",
    password="password",
    host="localhost",
    port=5432,
    database="mydb"
)

print(connection_config(db_config))