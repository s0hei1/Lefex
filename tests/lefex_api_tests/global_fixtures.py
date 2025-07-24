import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from apps.lefex.di import ApiProvider
from fastapi import FastAPI

@pytest.fixture
def app() -> FastAPI:
    return ApiProvider.lefex_api()

@pytest_asyncio.fixture
async def async_client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test/"
    ) as client:
        yield client

