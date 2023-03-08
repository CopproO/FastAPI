from enum import Enum

class Build(Enum):
    DEBUG = "hello"
    OPTIMIZED = "world"
    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None
    
Build("hello")