from fastapi import FastAPI


class ApiProvider:

    @classmethod
    def lefex_api(cls) -> FastAPI:

        from apps.lefex.api.experience_api import experience_router

        app = FastAPI()

        app.include_router(experience_router)

        return app
