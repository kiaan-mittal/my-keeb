# 001 — Repo setup and planning

- **Date:** 2026-08-15
- **Hours:** 2.0
- **Photos:** [`layout/layout.svg`](../layout/layout.svg) (planning sketch — no hardware yet)

## What I did

Read the KEEB docs in order: getting started, [GitHub repo](https://keeb.hackclub.com/docs/github-repo/), grants, planning, PCB design, case design, firmware, extras, and submitting.

The repo was an empty `# my-keeb` README. I turned it into the structure the submission checklist asks for:

- writeup in `README.md`
- `bom.csv` using grant-friendly parts (Orpheus Pico, MX, DSA blanks, 1N4148, EC11, OLED, M3 hardware)
- folders for PCB, case, firmware, photos, and journal entries
- a 65% plan with a matrix and Pico pinout
- a Keyboard Layout Editor JSON plus an SVG sketch so the layout is visible in the repo
- a starter RMK `keyboard.toml`

Design decisions I locked for v1:

- **65% ANSI** so I keep arrows (docs suggest 60% or 65% for a first board)
- **Orpheus Pico** as the MCU
- **EC11 encoder** top-right for volume
- **0.91" OLED** next to USB, watching the **GND-VCC-SCL-SDA** pin order
- **tray-mount case, split in half** because a 16–17u board is wider than a 220mm printer

## What I got stuck on

The case docs say a 60% is already ~285mm, so a 65% will not print in one piece. I planned a mid-board split with a tongue-and-groove instead of shrinking the layout.

Also: do not use GP23–GP25 on the Pico (SMPS, VBUS sense, LED). Rows and columns start at GP0.

## Next

Install KiCad + marbastlib and start the schematic from `layout/matrix.md`. After each KiCad session, add photos and hours here.
