from fastapi import HTTPException

class NotFoundException(HTTPException):
    """
    Exception for resource not found.
    """
    def __init__(self, detail: str = "Not Found"):
        super().__init__(status_code=404, detail=detail)

class ConflictException(HTTPException):
    """
    Exception for conflict errors.
    """
    def __init__(self, detail: str = "Conflict"):
        super().__init__(status_code=409, detail=detail)
