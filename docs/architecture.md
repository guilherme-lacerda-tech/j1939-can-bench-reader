# Architecture

## Design Goal

Provide a public CAN/J1939 bench parser using only synthetic frames and public protocol concepts.

## Parser Flow

```mermaid
flowchart LR
    Frame["Synthetic CAN frame"] --> ID["29-bit CAN ID"]
    ID --> Fields["Priority, DP, PF, PS, SA"]
    Fields --> PGN["PGN calculation"]
    Fields --> Address["Source and destination"]
    PGN --> Report["Parsed frame output"]
```

## J1939 Boundary

The parser decomposes 29-bit identifiers into generic J1939 fields. For PDU1 frames, `pdu_specific` is treated as destination address and excluded from PGN. For PDU2 frames, `pdu_specific` is part of the PGN.
