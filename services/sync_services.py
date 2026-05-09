from services.drive_auth_service import _list_shared_notebooks, _get_notebook_content
from sqlalchemy.future import select
from models.model import Files
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from datetime import datetime


async def notebook_exists(session: AsyncSession, title: str) -> bool:
    query = select(Files).where(Files.title == title)
    result = await session.execute(query)
    return result.scalar_one_or_none() is not None

async def sync_notebooks(session: AsyncSession):

    files = _list_shared_notebooks()

    for file in files:

        if file["name"].endswith(".ipynb") and not await notebook_exists(session, file["name"]): 

            content = await asyncio.to_thread(_get_notebook_content, file["id"])

            with open(f"notebooks/{file['name']}", "wb") as f:
                f.write(content)

            modified_at = datetime.fromisoformat(file["modifiedTime"].replace("Z", "+00:00")).replace(tzinfo=None)
            new_file = Files(title=file["name"], modified_at=modified_at)
            session.add(new_file)
            await session.commit()

if __name__ == "__main__":
    asyncio.run(sync_notebooks(None))