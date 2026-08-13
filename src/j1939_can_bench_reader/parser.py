from __future__ import annotations

import csv
from pathlib import Path


def parse_can_id(can_id: str) -> dict:
    normalized = can_id.lower().removeprefix("0x")
    value = int(normalized, 16)
    if value > 0x1FFFFFFF:
        raise ValueError("J1939 uses a 29-bit CAN identifier")

    priority = (value >> 26) & 0x7
    reserved = (value >> 25) & 0x1
    data_page = (value >> 24) & 0x1
    pdu_format = (value >> 16) & 0xFF
    pdu_specific = (value >> 8) & 0xFF
    source_address = value & 0xFF
    is_pdu1 = pdu_format < 240
    pgn = (data_page << 16) | (pdu_format << 8)
    destination_address = pdu_specific if is_pdu1 else None
    if not is_pdu1:
        pgn = pgn | pdu_specific
    return {
        "priority": priority,
        "reserved": reserved,
        "data_page": data_page,
        "pdu_format": pdu_format,
        "pdu_specific": pdu_specific,
        "pgn": pgn,
        "source_address": source_address,
        "source": source_address,
        "destination_address": destination_address,
        "pdu_type": "PDU1" if is_pdu1 else "PDU2",
    }


def parse_frames(path: Path) -> list[dict]:
    rows = list(csv.DictReader(path.read_text(encoding="utf-8").splitlines()))
    parsed = []
    for row in rows:
        parsed.append({**row, **parse_can_id(row["can_id"]), "data_length": len(row["data"]) // 2})
    return parsed
