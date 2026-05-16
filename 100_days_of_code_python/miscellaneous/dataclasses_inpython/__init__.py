from dataclasses import dataclass

@dataclass
class SparkJobConfig:
    job_name: str
    main_class: str
    args: list[str]
    driver_memory: str = "4g"
    executor_memory: str = "4g"
    num_executors: int = 2
    executor_cores: int = 2

def create_spark_submit_command(config: SparkJobConfig):
    command = (
        f"spark-submit --name {config.job_name} "
        f" --class {config.main_class}"
        f" --driver-memory {config.driver_memory}"
        f" --executor-memory {config.executor_memory}"
        f" --num-executors {config.num_executors}"
        f" --executor-cores {config.executor_cores}"
    )
    args_str = ' '.join(config.args)
    return args_str,command

config = SparkJobConfig(
    job_name="ExampleSparkJob",
    main_class="com.example.Main",
    jar_path="jdbc.psotgress.12.3.0.jar",
    args=["arg1", "arg2", "arg3"],
    driver_memory="8g",
    executor_memory="8g",
    num_executors=4,
    executor_cores=4
)
args_str,command = create_spark_submit_command(config)
# print(args_str)
# print(command)

def sumbit_spark_command(command:str):
    print(command)


sumbit_spark_command(create_spark_submit_command(config))