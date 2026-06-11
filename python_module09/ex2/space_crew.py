#!/usr/bin/env python3
from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_requirements(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            member.rank in (Rank.captain, Rank.commander)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            exp_count = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if 2 * exp_count < len(self.crew):
                raise ValueError(
                    "Long missions (> 365 days) "
                    "require at least 50% experienced crew (5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 30)

    valid_mission = {
        "mission_id": "M2024 MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2024-06-01T08:00:00",
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Connor",
                "rank": "commander",
                "age": 40,
                "specialization": "Mission Command",
                "years_experience": 15,
                "is_active": True,
            },
            {
                "member_id": "CM002",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 35,
                "specialization": "Navigation",
                "years_experience": 8,
                "is_active": True,
            },
            {
                "member_id": "CM003",
                "name": "Alice Johnson",
                "rank": "officer",
                "age": 28,
                "specialization": "Engineering",
                "years_experience": 4,
                "is_active": True,
            },
        ],
    }

    try:
        mission = SpaceMission(**valid_mission)
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions:.1f}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            name_rank = f"{member.name} ({member.rank.value})"
            print(f"  {name_rank:<30} {member.specialization}")
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print()
    print("=" * 30)

    invalid_mission = valid_mission.copy()
    invalid_mission["crew"] = [
        {
            "member_id": "CM002",
            "name": "John Smith",
            "rank": "lieutenant",
            "age": 35,
            "specialization": "Navigation",
            "years_experience": 8,
            "is_active": True,
        },
        {
            "member_id": "CM003",
            "name": "Alice Johnson",
            "rank": "officer",
            "age": 28,
            "specialization": "Engineering",
            "years_experience": 4,
            "is_active": True,
        },
    ]

    print("Expected validation error:")
    try:
        SpaceMission(**invalid_mission)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
