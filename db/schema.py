from typing import Optional

from pydantic import BaseModel , validator

class EmployeeBase(BaseModel):
	name : str
	email : str
	location : str


class EmployeeCreate(EmployeeBase):
	pass

class Employee(EmployeeBase):
	id : int
	is_active : Optional[bool]
	class Config:
		orm_mode = True

	@validator('is_active')
	def set_name(cls, is_active):
		return is_active or True

class EmployeeUpdate(BaseModel):
	name: Optional[str] = None
	location : Optional[str] = None
	is_active : Optional[str] = None

class CompanyBase(BaseModel):
	name : str
	contact : str
	location : str

class CompanyProductUpdate(CompanyBase):
	active_products : str
	inactive_products : str


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "mycoolapp"
    LOG_FORMAT: str = "%(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "format": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
			"default": {
			"class": "logging.handlers.RotatingFileHandler",
			"level": LOG_LEVEL,
			"formatter": "default",
			"filename": "info.log",
			"maxBytes": 10485760,
			"backupCount": 40,
			"encoding": "utf8"
		}
    }
    loggers = {
        "mycoolapp": {"handlers": ["default"], "level": LOG_LEVEL},
    }