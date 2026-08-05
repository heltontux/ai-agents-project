from dataclasses import dataclass
from core.role import Role

@dataclass
class Message:
    role: Role
    content: str