from fastapi import HTTPException


class KhelAIError(HTTPException):
    def __init__(self, code: str, message: str, field: str = None):
        super().__init__(
            status_code=400,
            detail={
                "error_code": code,
                "message": message,
                "field": field
            }
        )
