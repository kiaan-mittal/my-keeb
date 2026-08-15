# Firmware (RMK)

KEEB recommends [RMK](https://rmk.rs/docs/user_guide/guide_overview.html) for the Pico / Orpheus Pico.

`keyboard.toml` is a starter. **Do not flash it until the schematic pinout is locked** — the GPIO list matches [`layout/matrix.md`](../layout/matrix.md), not a finished PCB.

## Setup

1. Install Rust: https://rustup.rs
2. Install the RMK CLI from the [user guide](https://rmk.rs/docs/user_guide/guide_overview.html)
3. Generate or open an RP2040 project and copy this `keyboard.toml` in
4. After the PCB is routed, confirm every `PIN_n` against the KiCad netlist
5. Build, then hold BOOTSEL (or Esc if bootmagic is wired) and drop the `.uf2` on the Pico drive

## Layers (planned)

| Layer | Role |
| --- | --- |
| 0 | ANSI 65% |
| 1 | F-row, media, extra nav |

Encoder: volume on layer 0, mouse wheel on layer 1.

OLED (later): layer name + WPM on I2C1 (`PIN_26` / `PIN_27`).
