from fastapi import FastAPI

from apps.lefex.api.experience_api import experience_router


class ApiProvider:

    @classmethod
    def lefex_api(cls):
        app = FastAPI()

        app.include_router(experience_router)

        return app