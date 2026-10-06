from fastapi import APIRouter

from app.gemini import generate_gemini_response
from app.schemas import GeminiRequest


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post("/gemini")
def generate_response(request: GeminiRequest):
    response = generate_gemini_response(request.prompt)

    return {
        "response": response
    }