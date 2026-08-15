# Matrix map

Physical layout → electrical matrix. Use this when placing net labels in KiCad and when filling `firmware/keyboard.toml`.

Convention: **COL → switch → diode → ROW**. Unused intersections are blank.

## Rows and columns

| | C0 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | C13 | C14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **R0** | Esc | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | - | = | Bksp | Del |
| **R1** | Tab | Q | W | E | R | T | Y | U | I | O | P | [ | ] | \ | PgUp |
| **R2** | Caps | A | S | D | F | G | H | J | K | L | ; | ' | Enter |  | PgDn |
| **R3** | LSft | Z | X | C | V | B | N | M | , | . | / | RSft | ↑ |  | End |
| **R4** | LCtl | LGUI | LAlt | Space |  |  |  |  | RAlt | Fn | RCtl | ← | ↓ | → |  |

Encoder is **not** in the matrix: `ENC_A=GP20`, `ENC_B=GP21`, `ENC_SW=GP22`.

## Pico pinout

| Function | Pin |
| --- | --- |
| ROW0–ROW4 | GP0 GP1 GP2 GP3 GP4 |
| COL0–COL14 | GP5 GP6 GP7 GP8 GP9 GP10 GP11 GP12 GP13 GP14 GP15 GP16 GP17 GP18 GP19 |
| Encoder A/B/SW | GP20 GP21 GP22 |
| OLED SDA/SCL | GP26 GP27 |
| Spare / RGB | GP28 |
| Do not use | GP23 GP24 GP25 |

## Stabilizer centers (1u = 19.05mm)

Coordinates are the key's top-left in u, then the stab bar is centered on the key.

| Key | Top-left (u) | Width | Stab |
| --- | --- | ---: | --- |
| Backspace | (13, 0) | 2 | 2u |
| Enter | (12.75, 2) | 2.25 | 2u |
| Left Shift | (0, 3) | 2.25 | 2u |
| Space | (3.75, 4) | 6.25 | 6.25u |
