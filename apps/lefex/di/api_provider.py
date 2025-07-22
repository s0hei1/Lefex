from fastapi import FastAPI


class ApiProvider:

    @classmethod
    def lefex_api(cls):
        return FastAPI()