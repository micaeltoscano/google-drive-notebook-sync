from fastapi import (APIRouter, Depends, HTTPException, status, Response)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.model import Files
from schemas.schemas import  FileSchema
from core.deps import get_session

router = APIRouter()

@router.get('/notebooks', response_model=list[FileSchema]) 
async def get_notebooks(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Files)
        result = await session.execute(query)
        files = result.scalars().all()

    return files
    
@router.post('/notebooks', response_model=FileSchema, status_code=status.HTTP_201_CREATED)
async def post_notebook(file: FileSchema, db: AsyncSession = Depends(get_session)):
    new_file = Files(title=file.title, modified_at=file.modified_at)

    db.add(new_file)
    await db.commit()

    return new_file

@router.delete('/notebooks/{file_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_notebook(file_id: int, db: AsyncSession = Depends(get_session)):    
    async with db as session:
        query = select(Files).where(Files.id == file_id)
        result = await session.execute(query)
        file = result.scalar_one_or_none()

        if file is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

        await session.delete(file)
        await session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

