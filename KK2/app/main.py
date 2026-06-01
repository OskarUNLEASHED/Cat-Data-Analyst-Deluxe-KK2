from typing import Any

from fastapi import FastAPI, File, HTTPException, UploadFile

from app.data import DatasetError, get_stats, load_csv
from app.schemas import ErrorResponse, UploadMetadata

app = FastAPI(title="KK2 Oraklet")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/data/upload",
    response_model=UploadMetadata,
    responses={400: {"model": ErrorResponse}},
)
async def upload_data(file: UploadFile = File(...)) -> UploadMetadata:
    if file.filename is None or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are accepted.")

    try:
        return load_csv(file.file)
    except DatasetError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get(
    "/data/stats",
    responses={404: {"model": ErrorResponse}},
)
def data_stats() -> dict[str, dict[str, Any]]:
    stats = get_stats()
    if stats is None:
        raise HTTPException(status_code=404, detail="No dataset has been uploaded.")

    return stats
