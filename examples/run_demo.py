from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from pathlib import Path

from j1939_can_bench_reader.parser import parse_frames


ROOT = Path(__file__).resolve().parents[1]
frames = parse_frames(ROOT / "data" / "sample" / "synthetic_frames.csv")
print(f"Frames parsed: {len(frames)}")
print(f"First PGN: {frames[0]['pgn']}")
