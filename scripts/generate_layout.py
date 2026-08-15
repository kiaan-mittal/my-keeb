#!/usr/bin/env python3
"""Generate the my-keeb layout SVG and KiCad starter files."""

from __future__ import annotations

import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
U = 19.05  # MX unit, mm

# (x_u, y_u, w_u, label, row, col, stab_or_none)
# Encoder is off-matrix.
KEYS: list[tuple[float, float, float, str, int | None, int | None, str | None]] = [
    # Row 0
    (0, 0, 1, "Esc", 0, 0, None),
    (1, 0, 1, "1", 0, 1, None),
    (2, 0, 1, "2", 0, 2, None),
    (3, 0, 1, "3", 0, 3, None),
    (4, 0, 1, "4", 0, 4, None),
    (5, 0, 1, "5", 0, 5, None),
    (6, 0, 1, "6", 0, 6, None),
    (7, 0, 1, "7", 0, 7, None),
    (8, 0, 1, "8", 0, 8, None),
    (9, 0, 1, "9", 0, 9, None),
    (10, 0, 1, "0", 0, 10, None),
    (11, 0, 1, "-", 0, 11, None),
    (12, 0, 1, "=", 0, 12, None),
    (13, 0, 2, "Bksp", 0, 13, "2u"),
    (15, 0, 1, "Del", 0, 14, None),
    (16.25, 0, 1, "Enc", None, None, "encoder"),
    # Row 1
    (0, 1, 1.5, "Tab", 1, 0, None),
    (1.5, 1, 1, "Q", 1, 1, None),
    (2.5, 1, 1, "W", 1, 2, None),
    (3.5, 1, 1, "E", 1, 3, None),
    (4.5, 1, 1, "R", 1, 4, None),
    (5.5, 1, 1, "T", 1, 5, None),
    (6.5, 1, 1, "Y", 1, 6, None),
    (7.5, 1, 1, "U", 1, 7, None),
    (8.5, 1, 1, "I", 1, 8, None),
    (9.5, 1, 1, "O", 1, 9, None),
    (10.5, 1, 1, "P", 1, 10, None),
    (11.5, 1, 1, "[", 1, 11, None),
    (12.5, 1, 1, "]", 1, 12, None),
    (13.5, 1, 1.5, "\\", 1, 13, None),
    (15, 1, 1, "PgUp", 1, 14, None),
    # Row 2
    (0, 2, 1.75, "Caps", 2, 0, None),
    (1.75, 2, 1, "A", 2, 1, None),
    (2.75, 2, 1, "S", 2, 2, None),
    (3.75, 2, 1, "D", 2, 3, None),
    (4.75, 2, 1, "F", 2, 4, None),
    (5.75, 2, 1, "G", 2, 5, None),
    (6.75, 2, 1, "H", 2, 6, None),
    (7.75, 2, 1, "J", 2, 7, None),
    (8.75, 2, 1, "K", 2, 8, None),
    (9.75, 2, 1, "L", 2, 9, None),
    (10.75, 2, 1, ";", 2, 10, None),
    (11.75, 2, 1, "'", 2, 11, None),
    (12.75, 2, 2.25, "Enter", 2, 12, "2u"),
    (15, 2, 1, "PgDn", 2, 14, None),
    # Row 3
    (0, 3, 2.25, "Shift", 3, 0, "2u"),
    (2.25, 3, 1, "Z", 3, 1, None),
    (3.25, 3, 1, "X", 3, 2, None),
    (4.25, 3, 1, "C", 3, 3, None),
    (5.25, 3, 1, "V", 3, 4, None),
    (6.25, 3, 1, "B", 3, 5, None),
    (7.25, 3, 1, "N", 3, 6, None),
    (8.25, 3, 1, "M", 3, 7, None),
    (9.25, 3, 1, ",", 3, 8, None),
    (10.25, 3, 1, ".", 3, 9, None),
    (11.25, 3, 1, "/", 3, 10, None),
    (12.25, 3, 1.75, "Shift", 3, 11, None),
    (14, 3, 1, "Up", 3, 12, None),
    (15, 3, 1, "End", 3, 14, None),
    # Row 4
    (0, 4, 1.25, "Ctrl", 4, 0, None),
    (1.25, 4, 1.25, "Win", 4, 1, None),
    (2.5, 4, 1.25, "Alt", 4, 2, None),
    (3.75, 4, 6.25, "Space", 4, 3, "6.25u"),
    (10, 4, 1, "Alt", 4, 8, None),
    (11, 4, 1, "Fn", 4, 9, None),
    (12, 4, 1, "Ctrl", 4, 10, None),
    (13, 4, 1, "Left", 4, 11, None),
    (14, 4, 1, "Down", 4, 12, None),
    (15, 4, 1, "Right", 4, 13, None),
]


def uid() -> str:
    return str(uuid.uuid4())


def write_svg(path: Path) -> None:
    scale = 54
    pad = 28
    gap = 3
    width_u = 17.25
    height_u = 5
    w = pad * 2 + width_u * scale
    h = pad * 2 + height_u * scale + 36

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.1f}" height="{h:.1f}" '
        f'viewBox="0 0 {w:.1f} {h:.1f}" role="img" aria-label="my-keeb 65 percent layout">',
        "<style>",
        "  .key { fill: #f4efe4; stroke: #1b1b1b; stroke-width: 1.4; }",
        "  .enc { fill: #ff8c37; }",
        "  .stab { fill: #338eda; }",
        "  .wide { fill: #f0e6d2; }",
        "  .mod { fill: #e8e0d2; }",
        "  text { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; "
        "fill: #1b1b1b; text-anchor: middle; dominant-baseline: middle; }",
        "  .label { font-size: 11px; font-weight: 700; }",
        "  .rc { font-size: 8px; fill: #5c5c5c; }",
        "  .title { font-size: 16px; font-weight: 800; text-anchor: start; }",
        "  .sub { font-size: 11px; fill: #5c5c5c; text-anchor: start; }",
        "</style>",
        '<rect width="100%" height="100%" fill="#fff8f0"/>',
        f'<text class="title" x="{pad}" y="18">my-keeb — planned ANSI 65%</text>',
        f'<text class="sub" x="{pad}" y="34">Hack Club KEEB · MX 19.05mm · encoder is off-matrix</text>',
    ]

    mods = {"Esc", "Tab", "Caps", "Shift", "Ctrl", "Win", "Alt", "Fn", "Bksp", "Enter", "Del", "PgUp", "PgDn", "End"}
    for x, y, kw, label, row, col, extra in KEYS:
        px = pad + x * scale + gap / 2
        py = pad + 24 + y * scale + gap / 2
        pw = kw * scale - gap
        ph = scale - gap
        cls = "key"
        if extra == "encoder":
            cls += " enc"
        elif extra:
            cls += " stab"
        elif kw > 1.05:
            cls += " wide"
        elif label in mods:
            cls += " mod"
        rx = ph / 2 if extra == "encoder" else 6
        parts.append(
            f'<rect class="{cls}" x="{px:.2f}" y="{py:.2f}" width="{pw:.2f}" '
            f'height="{ph:.2f}" rx="{rx:.1f}"/>'
        )
        parts.append(
            f'<text class="label" x="{px + pw / 2:.2f}" y="{py + ph / 2 - 5:.2f}">{_xml(label)}</text>'
        )
        rc = "ENC GP20/21" if extra == "encoder" else f"R{row} C{col}"
        parts.append(
            f'<text class="rc" x="{px + pw / 2:.2f}" y="{py + ph / 2 + 10:.2f}">{rc}</text>'
        )

    parts.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def _xml(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\\", "\\\\")
    )


def write_kicad_pro(path: Path) -> None:
    path.write_text(
        """{
  "board": {
    "3dviewports": [],
    "design_settings": {
      "defaults": {
        "board_outline_line_width": 0.1,
        "copper_line_width": 0.2,
        "copper_text_size_h": 1.5,
        "copper_text_size_v": 1.5,
        "copper_text_thickness": 0.3,
        "other_line_width": 0.15,
        "silk_line_width": 0.15,
        "silk_text_size_h": 1.0,
        "silk_text_size_v": 1.0
      },
      "diff_pair_dimensions": [],
      "drc_exclusions": [],
      "rules": {
        "min_clearance": 0.2,
        "min_track_width": 0.2,
        "min_via_diameter": 0.6,
        "min_via_drill": 0.3,
        "solder_mask_to_copper_clearance": 0.0
      },
      "track_widths": [0.0, 0.25, 0.4, 0.6],
      "via_dimensions": [
        { "diameter": 0.0, "drill": 0.0 },
        { "diameter": 0.6, "drill": 0.3 }
      ],
      "zones_allow_external_fillets": true
    }
  },
  "boards": [],
  "libraries": {
    "pinned_footprint_libs": [],
    "pinned_symbol_libs": []
  },
  "meta": {
    "filename": "my-keeb.kicad_pro",
    "version": 3
  },
  "net_settings": {
    "classes": [
      {
        "bus_width": 12,
        "clearance": 0.2,
        "diff_pair_gap": 0.25,
        "diff_pair_via_gap": 0.25,
        "diff_pair_width": 0.2,
        "line_style": 0,
        "microvia_diameter": 0.3,
        "microvia_drill": 0.1,
        "name": "Default",
        "pcb_color": "rgba(0, 0, 0, 0.000)",
        "schematic_color": "rgba(0, 0, 0, 0.000)",
        "track_width": 0.25,
        "via_diameter": 0.6,
        "via_drill": 0.3,
        "wire_width": 6
      }
    ],
    "meta": { "version": 3 }
  },
  "pcbnew": {
    "last_paths": {
      "gencad": "",
      "idf": "",
      "netlist": "",
      "plot": "gerbers/",
      "pos_files": "",
      "specctra_dsn": "",
      "step": "",
      "svg": "",
      "vrml": ""
    },
    "page_layout_descr_file": ""
  },
  "schematic": {
    "annotate_start_nums": [],
    "drawing": {
      "dashed_lines_dash_length_ratio": 12.0,
      "dashed_lines_gap_length_ratio": 3.0,
      "default_line_thickness": 6.0,
      "default_text_size": 50.0,
      "field_names": [],
      "intersheets_ref_own_page": false,
      "intersheets_ref_prefix": "",
      "intersheets_ref_short": false,
      "intersheets_ref_show": false,
      "intersheets_ref_suffix": "",
      "junction_size_choice": 3,
      "label_size_ratio": 0.375,
      "operating_point_overlay_i_precision": 3,
      "operating_point_overlay_i_range": "~A",
      "operating_point_overlay_v_precision": 3,
      "operating_point_overlay_v_range": "~V",
      "overbar_offset_ratio": 1.23,
      "pin_symbol_size": 25.0,
      "text_offset_ratio": 0.15
    },
    "legacy_lib_dir": "",
    "legacy_lib_list": [],
    "meta": { "version": 1 },
    "net_format_name": "",
    "page_layout_descr_file": "",
    "plot_directory": "",
    "spice_current_sheet_as_root": false,
    "spice_external_command": "",
    "spice_model_current_sheet_as_root": true,
    "spice_save_all_currents": false,
    "spice_save_all_dissipations": false,
    "spice_save_all_voltages": false,
    "subsheet_field_names": [],
    "version": 1
  },
  "sheets": [
    ["my-keeb.kicad_sch", "Root"]
  ],
  "text_variables": {}
}
""",
        encoding="utf-8",
    )


def _text(x: float, y: float, value: str, size: float = 2.54) -> str:
    return f"""  (text "{value}"
    (exclude_from_sim no)
    (at {x} {y} 0)
    (effects (font (size {size} {size}) (thickness 0.3)) (justify left))
    (uuid "{uid()}")
  )"""


def _label(x: float, y: float, name: str) -> str:
    return f"""  (label "{name}"
    (at {x} {y} 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{uid()}")
  )"""


def _wire(x1: float, y1: float, x2: float, y2: float) -> str:
    return f"""  (wire
    (pts (xy {x1} {y1}) (xy {x2} {y2}))
    (stroke (width 0) (type default))
    (uuid "{uid()}")
  )"""


def write_schematic(path: Path) -> None:
    # Embedded 2-pin symbols so the starter sheet opens without extra libs.
    lib_symbols = r"""
  (lib_symbols
    (symbol "Device:D"
      (pin_names (offset 1.016))
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "D" (at 0 2.54 0)
        (effects (font (size 1.27 1.27))))
      (property "Value" "D" (at 0 -2.54 0)
        (effects (font (size 1.27 1.27))))
      (property "Footprint" "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide))
      (symbol "D_0_1"
        (polyline (pts (xy -1.27 1.27) (xy -1.27 -1.27))
          (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 0) (xy -1.27 0))
          (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 1.27) (xy 1.27 -1.27) (xy -1.27 0) (xy 1.27 1.27))
          (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "D_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54)
          (name "K" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54)
          (name "A" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "Switch:SW_Push"
      (pin_names (offset 1.016) hide)
      (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "SW" (at 1.27 2.54 0)
        (effects (font (size 1.27 1.27)) (justify left)))
      (property "Value" "SW_Push" (at 0 -2.54 0)
        (effects (font (size 1.27 1.27))))
      (property "Footprint" "PCM_marbastlib-mx:SW_MX_1u" (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide))
      (symbol "SW_Push_0_1"
        (circle (center 0 0) (radius 0.508)
          (stroke (width 0) (type default)) (fill (type none)))
        (polyline (pts (xy 1.016 0) (xy 2.54 1.016) (xy 3.81 1.016))
          (stroke (width 0) (type default)) (fill (type none)))
      )
      (symbol "SW_Push_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54)
          (name "1" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54)
          (name "2" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
  )
"""

    body: list[str] = [
        f"""(kicad_sch
  (version 20231120)
  (generator "eeschema")
  (generator_version "8.0")
  (uuid "{uid()}")
  (paper "A3")
  (title_block
    (title "my-keeb")
    (date "2026-08-15")
    (rev "0.1")
    (company "Kiaan Mittal")
    (comment 1 "Hack Club KEEB — starter schematic, replicate the switch-diode unit")
  )
{lib_symbols}
"""
    ]

    body.append(_text(12.7, 12.7, "my-keeb  —  Hack Club KEEB starter schematic", 3.0))
    body.append(
        _text(
            12.7,
            20.32,
            "Replicate SW+D for every key. Labels: COL -> SW pin1, SW pin2 -> D anode, D cathode -> ROW.",
            1.8,
        )
    )
    body.append(
        _text(
            12.7,
            25.4,
            "Pico: ROW0-4 = GP0-4   COL0-14 = GP5-19   ENC A/B/SW = GP20/21/22   OLED SDA/SCL = GP26/27",
            1.8,
        )
    )

    # Example switch-diode unit
    sw_x, sw_y = 50.8, 60.96
    d_x, d_y = 68.58, 60.96
    body.append(
        f"""  (symbol
    (lib_id "Switch:SW_Push")
    (at {sw_x} {sw_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (fields_autoplaced yes)
    (uuid "{uid()}")
    (property "Reference" "SW1" (at {sw_x} {sw_y - 5.08} 0)
      (effects (font (size 1.27 1.27))))
    (property "Value" "Esc" (at {sw_x} {sw_y + 5.08} 0)
      (effects (font (size 1.27 1.27))))
    (property "Footprint" "PCM_marbastlib-mx:SW_MX_1u" (at {sw_x} {sw_y} 0)
      (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{uid()}"))
    (pin "2" (uuid "{uid()}"))
    (instances
      (project "my-keeb"
        (path "/{path.stem}" (reference "SW1") (unit 1))
      )
    )
  )"""
    )
    body.append(
        f"""  (symbol
    (lib_id "Device:D")
    (at {d_x} {d_y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (fields_autoplaced yes)
    (uuid "{uid()}")
    (property "Reference" "D1" (at {d_x} {d_y - 5.08} 0)
      (effects (font (size 1.27 1.27))))
    (property "Value" "1N4148" (at {d_x} {d_y + 5.08} 0)
      (effects (font (size 1.27 1.27))))
    (property "Footprint" "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" (at {d_x} {d_y} 0)
      (effects (font (size 1.27 1.27)) hide))
    (pin "1" (uuid "{uid()}"))
    (pin "2" (uuid "{uid()}"))
    (instances
      (project "my-keeb"
        (path "/{path.stem}" (reference "D1") (unit 1))
      )
    )
  )"""
    )
    body.append(_wire(sw_x + 3.81, sw_y, d_x - 3.81, d_y))
    body.append(_wire(sw_x - 3.81, sw_y, sw_x - 10.16, sw_y))
    body.append(_wire(d_x + 3.81, d_y, d_x + 10.16, d_y))
    body.append(_label(sw_x - 10.16, sw_y, "COL0"))
    body.append(_label(d_x + 10.16, d_y, "ROW0"))
    body.append(_text(38.1, 73.66, "Example unit = Esc (R0 C0). Copy this pair 67 more times.", 1.5))

    # Row / column label bank so nets exist on the sheet
    body.append(_text(120.65, 45.72, "Row nets (to Pico GP0-GP4)", 1.8))
    for i in range(5):
        y = 53.34 + i * 7.62
        body.append(_label(120.65, y, f"ROW{i}"))
    body.append(_text(120.65, 96.52, "Column nets (to Pico GP5-GP19)", 1.8))
    for i in range(15):
        x = 120.65 + (i % 8) * 20.32
        y = 104.14 + (i // 8) * 10.16
        body.append(_label(x, y, f"COL{i}"))

    body.append(_text(12.7, 96.52, "Off-matrix extras (wire to Pico after placing symbols)", 1.8))
    for i, name in enumerate(("ENC_A", "ENC_B", "ENC_SW", "SDA", "SCL", "GND", "+3V3")):
        body.append(_label(12.7, 104.14 + i * 7.62, name))

    body.append(
        _text(
            12.7,
            175.26,
            "Next: Tools -> Annotate Schematic, then Assign Footprints (see pcb/README.md).",
            1.5,
        )
    )
    body.append(")\n")
    path.write_text("\n".join(body), encoding="utf-8")


def write_pcb(path: Path) -> None:
    margin = 8.0
    layout_w = 17.25 * U
    layout_h = 5 * U
    board_w = layout_w + margin * 2
    board_h = layout_h + margin * 2 + 18  # extra for Pico USB along the top

    items: list[str] = []
    items.append(
        f"""  (gr_rect
    (start 0 0)
    (end {board_w:.3f} {board_h:.3f})
    (stroke (width 0.15) (type default))
    (fill none)
    (layer "Edge.Cuts")
    (uuid "{uid()}")
  )"""
    )
    items.append(
        f"""  (gr_text "my-keeb  v0.1  Hack Club KEEB  (placement guide — not a finished board)"
    (at {board_w / 2:.3f} {board_h - 3:.3f} 0)
    (layer "F.SilkS")
    (uuid "{uid()}")
    (effects (font (size 2 2) (thickness 0.3)))
  )"""
    )

    origin_x = margin
    origin_y = margin + 16  # leave room above row 0 for Pico / USB
    for x, y, kw, label, row, col, extra in KEYS:
        cx = origin_x + (x + kw / 2) * U
        cy = origin_y + (y + 0.5) * U
        layer = "Eco1.User" if extra == "encoder" else "Dwgs.User"
        items.append(
            f"""  (gr_rect
    (start {cx - (kw * U) / 2 + 0.4:.3f} {cy - U / 2 + 0.4:.3f})
    (end {cx + (kw * U) / 2 - 0.4:.3f} {cy + U / 2 - 0.4:.3f})
    (stroke (width 0.12) (type default))
    (fill none)
    (layer "{layer}")
    (uuid "{uid()}")
  )"""
        )
        rc = "ENC" if extra == "encoder" else f"R{row}C{col}"
        items.append(
            f"""  (gr_text "{label}\\n{rc}"
    (at {cx:.3f} {cy:.3f} 0)
    (layer "Dwgs.User")
    (uuid "{uid()}")
    (effects (font (size 1.2 1.2) (thickness 0.18)))
  )"""
        )

    # Pico keepout / USB hint along the top edge, centered
    pico_w, pico_h = 21.0, 51.0
    pico_x = board_w / 2
    pico_y = 2.0
    items.append(
        f"""  (gr_rect
    (start {pico_x - pico_w / 2:.3f} {-4:.3f})
    (end {pico_x + pico_w / 2:.3f} {pico_y + 18:.3f})
    (stroke (width 0.15) (type dash))
    (fill none)
    (layer "Cmts.User")
    (uuid "{uid()}")
  )"""
    )
    items.append(
        f"""  (gr_text "Pico / Orpheus Pico\\nUSB-C hangs off top edge"
    (at {pico_x:.3f} 6 0)
    (layer "Cmts.User")
    (uuid "{uid()}")
    (effects (font (size 1.4 1.4) (thickness 0.2)))
  )"""
    )

    # Mounting hole markers (M3)
    holes = [
        (5, 5),
        (board_w - 5, 5),
        (5, board_h - 5),
        (board_w - 5, board_h - 5),
        (board_w / 2, 5),
        (board_w / 2, board_h - 5),
    ]
    for hx, hy in holes:
        items.append(
            f"""  (gr_circle
    (center {hx:.3f} {hy:.3f})
    (end {hx + 1.6:.3f} {hy:.3f})
    (stroke (width 0.15) (type default))
    (fill none)
    (layer "Dwgs.User")
    (uuid "{uid()}")
  )"""
        )

    pcb = f"""(kicad_pcb
  (version 20240108)
  (generator "pcbnew")
  (generator_version "8.0")
  (general
    (thickness 1.6)
    (legacy_teardrops no)
  )
  (paper "A3")
  (title_block
    (title "my-keeb")
    (date "2026-08-15")
    (rev "0.1")
    (company "Kiaan Mittal")
  )
  (layers
    (0 "F.Cu" signal)
    (31 "B.Cu" signal)
    (32 "B.Adhes" user "B.Adhesive")
    (33 "F.Adhes" user "F.Adhesive")
    (34 "B.Paste" user)
    (35 "F.Paste" user)
    (36 "B.SilkS" user "B.Silkscreen")
    (37 "F.SilkS" user "F.Silkscreen")
    (38 "B.Mask" user)
    (39 "F.Mask" user)
    (40 "Dwgs.User" user "User.Drawings")
    (41 "Cmts.User" user "User.Comments")
    (42 "Eco1.User" user "User.Eco1")
    (43 "Eco2.User" user "User.Eco2")
    (44 "Edge.Cuts" user)
    (45 "Margin" user)
    (46 "B.CrtYd" user "B.Courtyard")
    (47 "F.CrtYd" user "F.Courtyard")
    (48 "B.Fab" user)
    (49 "F.Fab" user)
  )
  (setup
    (pad_to_mask_clearance 0)
    (allow_soldermask_bridges_in_footprints no)
    (pcbplotparams
      (layerselection 0x00010fc_ffffffff)
      (plot_on_all_layers_selection 0x0000000_00000000)
      (disableapertmacros no)
      (usegerberextensions no)
      (usegerberattributes yes)
      (usegerberadvancedattributes yes)
      (creategerberjobfile yes)
      (dashed_line_dash_ratio 12.000000)
      (dashed_line_gap_ratio 3.000000)
      (svgprecision 4)
      (plotframeref no)
      (viasonmask no)
      (mode 1)
      (useauxorigin no)
      (hpglpennumber 1)
      (hpglpenspeed 20)
      (hpglpendiameter 15.000000)
      (pdf_front_fp_property_popups yes)
      (pdf_back_fp_property_popups yes)
      (dxfpolygonmode yes)
      (dxfimperialunits yes)
      (dxfusepcbnewfont yes)
      (psnegative no)
      (psa4output no)
      (plotreference yes)
      (plotvalue yes)
      (plotfptext yes)
      (plotinvisibletext no)
      (sketchpadsonfab no)
      (subtractmaskfromsilk no)
      (outputformat 1)
      (mirror no)
      (drillshape 0)
      (scaleselection 1)
      (outputdirectory "gerbers/")
    )
  )
{chr(10).join(items)}
)
"""
    path.write_text(pcb, encoding="utf-8")


def write_coordinates(path: Path) -> None:
    lines = [
        "# Switch centers in mm (origin = top-left of key well, +x right, +y down)",
        "# Add 8mm board margin in X and 24mm in Y if using the starter Edge.Cuts.",
        "label,x_u,y_u,w_u,cx_mm,cy_mm,row,col,extra",
    ]
    for x, y, kw, label, row, col, extra in KEYS:
        cx = (x + kw / 2) * U
        cy = (y + 0.5) * U
        lines.append(
            f"{label},{x},{y},{kw},{cx:.3f},{cy:.3f},{row if row is not None else ''},"
            f"{col if col is not None else ''},{extra or ''}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    write_svg(ROOT / "layout" / "layout.svg")
    write_coordinates(ROOT / "layout" / "coordinates.csv")
    write_kicad_pro(ROOT / "pcb" / "my-keeb.kicad_pro")
    write_schematic(ROOT / "pcb" / "my-keeb.kicad_sch")
    write_pcb(ROOT / "pcb" / "my-keeb.kicad_pcb")
    print("wrote layout/layout.svg, layout/coordinates.csv, and pcb/my-keeb.kicad_*")


if __name__ == "__main__":
    main()
