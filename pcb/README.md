# PCB (KiCad)

Follow [Designing the PCB](https://keeb.hackclub.com/docs/pcb-design). This folder is the KiCad project. Gerbers go in `gerbers/` once the board passes DRC.

## Before opening KiCad

1. Install the latest KiCad from [kicad.org](https://www.kicad.org/)
2. Install **marbastlib** via Plugin and Content Manager
   - Repository URL: `https://raw.githubusercontent.com/ebastler/ebastler-KiCad-repository/main/repository.json`
3. Open `my-keeb.kicad_pro`

The starter schematic is a **worksheet**: Pico nets, one example switch-diode unit, and a legend. Replicate the unit for every key using [`../layout/matrix.md`](../layout/matrix.md).

## Footprints (from the KEEB guide)

| Symbol | Footprint |
| --- | --- |
| Raspberry Pi Pico / Orpheus Pico | `RaspberryPi_Pico_Common_THT` |
| 1N4148 | `Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal` |
| MX switch | `PCM_marbastlib-mx:SW_MX_1u` |
| Stabilizer | `PCM_marbastlib-mx:STAB_MX` |

## Placement

- MX grid: **19.05mm**
- Pico on the top edge so USB-C hangs off the board
- Columns on `F.Cu`, rows on `B.Cu`
- 45° corners, no autoroute
- Ground pour on both layers after routing
- Export Gerbers with the [guide settings](https://keeb.hackclub.com/docs/pcb-design), then zip `gerbers/` into the repo

`scripts/generate_layout.py` can reprint switch coordinates if the KLE layout changes.
