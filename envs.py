from environs import Env

env: Env = Env()
env.read_env(recurse=False)

WEBHOOK_URL = env("WEBHOOK_URL")
