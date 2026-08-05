from dataclasses import dataclass
from core.role import Role

@dataclass(frozen=True)
class Message:
    role: Role
    content: str