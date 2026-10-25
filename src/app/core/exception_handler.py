from fastapi.responses import JSONResponse
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from src.app.core.exceptions import AppException


# standard exception handler
def standard_exception_handler(
    status_code: int, message: str, errors: list | None = None
):
    content = {
        "success": False,
        "status_code": status_code,
        "message": message,
        "error": errors if errors is not None else [],
    }
    return JSONResponse(status_code=status_code, content=content)


def validation_exception_handler(request: Request, exc: RequestValidationError):
    formatted_errors = []
    for err in exc.errors():
        field_path = ".".join(str(loc) for loc in err["loc"] if loc != "body")
        formatted_errors.append(
            {
                "field": field_path or "body",
                "message": err["msg"],
            }
        )

    return standard_exception_handler(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        message="Request validation failed",
        errors=formatted_errors,
    )


def app_exception_handler(request: Request, exc: AppException):
    return standard_exception_handler(
        status_code=exc.status_code, message=exc.message, errors=exc.errors
    )


def internal_exception_handler(request: Request, exc: Exception):
    return standard_exception_handler(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message="Internal Server Error",
    )
