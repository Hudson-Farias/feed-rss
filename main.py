from fastapi import FastAPI
from importlib import import_module
from os import walk
from os.path import join

app = FastAPI()

def load(subapp: FastAPI, directory: str = "routers"):
    import_cache = {}

    for root, _, files in walk(directory):
        for file in files:
            if not file.startswith("__") and file.endswith(".py"):
                path = join(root, file).replace(".py", "").replace("/", ".").replace("\\", ".")

                if path not in import_cache:
                    import_cache[path] = import_module(path)

                module = import_cache[path]
                subapp.include_router(module.router)

    del import_cache

load(app)
