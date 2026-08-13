from __future__ import annotations

import csv
from pathlib import Path


def parse_can_id(can_id: str) -> dict:
    value = int(can_id, 16)
    priority = (value >> 26) & 0x7
    pgn = (value >> 8) & 0x3FFFF
    source = value & 0xFF
    return {"priority": priority, "pgn": pgn, "source": source}


def parse_frames(path: Path) -> list[dict]:
    rows = list(csv.DictReader(path.read_text(encoding="utf-8").splitlines()))
    parsed = []
    for row in rows:
        parsed.append({**row, **parse_can_id(row["can_id"])})
    return parsed
