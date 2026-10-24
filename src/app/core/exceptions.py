from fastapi.responses import JSONResponse
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError


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
