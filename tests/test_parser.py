from __future__ import annotations

from pathlib import Path

import pytest

from j1939_can_bench_reader.parser import parse_can_id, parse_frames


def test_parse_pdu2_can_id() -> None:
    parsed = parse_can_id("18FF0101")

    assert parsed["priority"] == 6
    assert parsed["pgn"] == 65281
    assert parsed["source_address"] == 1
    assert parsed["destination_address"] is None
    assert parsed["pdu_type"] == "PDU2"


def test_parse_pdu1_can_id_uses_destination_address() -> None:
    parsed = parse_can_id("18EAFF33")

    assert parsed["pgn"] == 59904
    assert parsed["source_address"] == 51
    assert parsed["destination_address"] == 255
    assert parsed["pdu_type"] == "PDU1"


def test_parse_frames_includes_data_length() -> None:
    root = Path(__file__).resolve().parents[1]
    frames = parse_frames(root / "data" / "sample" / "synthetic_frames.csv")

    assert len(frames) == 3
    assert frames[0]["data_length"] == 8


def test_rejects_identifier_outside_29_bits() -> None:
    with pytest.raises(ValueError):
        parse_can_id("3FFFFFFF")
