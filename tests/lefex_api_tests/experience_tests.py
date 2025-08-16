from http.client import responses
from typing import Any
from global_fixtures import app,async_client
from pytest import mark, fixture
from fastapi import FastAPI
from httpx import AsyncClient

@fixture
def fake_experience() -> dict[str,Any]:

    return {
        "decision" : "I Decided to employee",
        "experience" : "it was amazing , i have a more better life now :D"
    }

async def create_fake_experience(
        app : FastAPI,
        async_client: AsyncClient,
        fake_experience : dict[str,Any]
) -> dict[str,Any]:
    response = await async_client.post("/experience/create", json=fake_experience)
    response.raise_for_status()

    return response.json()



@mark.asyncio
async def test_create_experience(
        app: FastAPI,
        async_client: AsyncClient,
        fake_experience: dict[str, Any]
) -> None:

    experience = await create_fake_experience(app,async_client,fake_experience)

    assert "id" in experience
    assert "decision" in experience
    assert "experience" in experience
    assert experience["decision"] == fake_experience["decision"]
    assert experience["experience"] == fake_experience["experience"]

@mark.asyncio
async def test_update_experience(
        app: FastAPI,
        async_client: AsyncClient,
        fake_experience: dict[str, Any]
):
    experience = await create_fake_experience(app, async_client, fake_experience)

    assert "id" in experience

    new_experience = "Oh, now i think that was a bad idea"
    experience["experience"] = new_experience

    responses = await async_client.put("/experience/update", json=experience)
    responses.raise_for_status()
    assert responses.json().get("experience") == new_experience

@mark.asyncio
async def test_read_many_experiences(
        app: FastAPI,
        async_client: AsyncClient
):
    responses = await async_client.get("/experience/read_many")
    responses.raise_for_status()

    assert isinstance(responses.json(),list)


@mark.asyncio
async def test_read_one_experience(
        app: FastAPI,
        async_client: AsyncClient,
        fake_experience: dict[str, Any]
):
    experience = await create_fake_experience(app, async_client, fake_experience)
    id = experience['id']

    response = await async_client.get("/experience/read_one", params={"id" : id})
    response.raise_for_status()

    assert experience['id'] == response.json().get("id")
    assert experience['experience'] == response.json().get("experience")
    assert experience['decision'] == response.json().get("decision")


@mark.asyncio
async def test_delete_experience(
        app: FastAPI,
        async_async_client: AsyncClient,
        fake_experience: dict[str, Any]
):
    experience = await create_fake_experience(app, async_async_client, fake_experience)
    id = experience['id']

    response = await async_async_client.delete("/experience/delete", params={"id": id})
    response.raise_for_status()

    response = await async_async_client.get("/experience/read_one", params={"id" : id})

    assert response.status_code not in [200,201,202,203,204,404]
