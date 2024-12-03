
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..core.status_handler import StatusHandler

router = APIRouter(prefix="/api/status", tags=["status"])


@router.get("/")
async def status() -> JSONResponse:
    """
    This method will check the status of the server.

    Path:
    -------
        GET: /api/status/

    Parameters:
    -------
        None

    Returns:
    -------
        200: JSON response with the server status as {"Status": ["Server is up and running"]}

    Exception to handle:
    -------
        500: For any unexpected errors.
        503: Service not available<br>
    """
    return StatusHandler.app_status()
