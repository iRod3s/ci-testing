import prefect
from prefect import task, Flow

PROJECT_NAME = "test"

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("¡Hola Nube!")

with Flow("hello-flow") as flow:
    say_hello()
