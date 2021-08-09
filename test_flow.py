import prefect
from prefect import task, Flow

PROJECT_NAME = "test"

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, Cloud!")

with Flow("hello-flow") as flow:
    say_hello()
