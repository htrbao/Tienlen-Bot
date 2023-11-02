import os
from functools import lru_cache

import yaml
from pydantic_settings import BaseSettings

yaml_settings = dict()

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "config.yaml")) as f:
    yaml_settings.update(yaml.load(f, Loader=yaml.FullLoader))
    print(yaml_settings)


class Settings(BaseSettings):
    accounts: list[dict] = yaml_settings.get("accounts")


@lru_cache()
def get_settings():
    return Settings()
