# my-keeb plan

First-pass design so the schematic and PCB have a target. This can change.

## Vision

A daily-driver 65% that still looks like a Hack Club project: Orpheus Pico, a volume knob, a tiny OLED, and a silkscreen doodle on the back. Tray-mount, 3D-printed, split case.

```
  USB-C (Pico hangs off the top edge)
        ┌──────────────────────────────── OLED ── encoder
        │
  Esc 1 2 3 4 5 6 7 8 9 0 - = ⌫     Del
  Tab  Q W E R T Y U I O P [ ] \    PgUp
  Caps  A S D F G H J K L ; ' Enter PgDn
  Shift  Z X C V B N M , . / Shift ↑ End
  Ctrl Win Alt     Space    Alt Fn Ctrl ← ↓ →
```

## Layout

ANSI 65%, 68 MX keys, 16u × 5u plus a 1u encoder to the right of Delete.

| Item | Choice | Why |
| --- | --- | --- |
| Form factor | 65% | Recommended first board; keeps arrows |
| Profile | MX + DSA blanks | Grant parts; DSA ignores row profiles |
| Controller | Orpheus Pico | Official KEEB MCU, Pico footprint |
| Mount | Tray-mount | Matches the KiCad mounting-hole step |
| Case | Split 3D print | 65% is ~305mm; printer beds are ~220mm |
| Extras | EC11 + 0.91" OLED | Allowed grant add-ons, easy first extras |

Import [`layout/kle.json`](layout/kle.json) into [Keyboard Layout Editor](http://www.keyboard-layout-editor.com/) to tweak it.

## Matrix

5 rows × 15 columns = 75 intersections, 68 used. Pico has 26 usable GPIO after leaving GP23–GP25 alone (SMPS / VBUS / LED).

| Net | Pico pin | Notes |
| --- | --- | --- |
| ROW0–ROW4 | GP0–GP4 | Switch → diode cathode → row |
| COL0–COL14 | GP5–GP19 | Switch other pin → column |
| ENC_A / ENC_B | GP20 / GP21 | EC11 quadrature |
| ENC_SW | GP22 | Encoder push (or put it in the matrix later) |
| OLED SDA / SCL | GP26 / GP27 | I2C1, 0.91" module pin order **GND-VCC-SCL-SDA** |
| spare | GP28 | RGB data later if I add SK6812s |

Diode direction in the schematic: **column → switch → diode → row** (current into the row pin). RMK defaults to col2row. If the board is wired the other way, set `row2col = true` in `firmware/keyboard.toml`.

Per-key (row, col) addresses are in [`layout/matrix.md`](layout/matrix.md).

## Stabilizers (PCB-mount MX)

| Key | Width | Stab |
| --- | --- | --- |
| Backspace | 2u | 2u |
| Enter | 2.25u | 2u |
| Left Shift | 2.25u | 2u |
| Space | 6.25u | 6.25u |
| Right Shift | 1.75u | none |

## Board geometry

MX pitch is 19.05mm.

| Measure | Value |
| --- | --- |
| Layout width | 16u keys + 0.25u gap + 1u encoder |
| Layout height | 5u |
| PCB target | ~330mm × 110mm, 1.6mm FR4, 2 layers |
| Switch holes (plate) | 14mm × 14mm |
| USB | Pico USB-C hangs off the **top** edge, roughly centered |
| OLED | Behind a window in the top case, left of USB |
| Encoder | Top-right, aligned with the Delete column |

Front copper for columns, back copper for rows, 45° corners, ground pour on both sides after routing.

## Case

Onshape Education, tray-mount, then STEP export into `case/`.

1. Export the PCB as STEP from KiCad
2. Import into Onshape, create a Part Studio in context
3. Bottom: 3–5mm base, 2–3mm walls
4. USB cutout ~10mm × 5mm
5. M3 heatset bosses in the corners and along the long edges
6. Split the case near the middle with a tongue-and-groove so each half fits a 220mm bed
7. Optional 1.5–2mm plate if the tray-mount flex feels bad

## Firmware

[RMK](https://rmk.rs/) on RP2040, as the KEEB firmware page recommends.

- Base layer: standard 65% ANSI
- Fn layer: F1–F12, Delete (if I move it), media, RGB later
- Encoder: volume on base, scroll on Fn
- OLED: layer name + WPM
- Bootmagic on Esc (row 0, col 0) so I can recover without opening the case

Starter config lives in [`firmware/keyboard.toml`](firmware/keyboard.toml). Pin numbers get locked in when the schematic is annotated.

## Silkscreen / personality

- Back: Orpheus or a small Hack Club flag
- Front: `my-keeb` + version under the spacebar
- Open diode polarity marks so soldering is harder to mess up

## Build order

1. Repo + plan (this)
2. Schematic in KiCad
3. PCB place + route + DRC + Gerbers
4. Case in Onshape
5. Update `bom.csv` with real links and prices
6. Grant → order PCB and parts
7. Solder Pico, diodes, stabs, switches, extras
8. Flash RMK
9. Journal the whole way, then submit
