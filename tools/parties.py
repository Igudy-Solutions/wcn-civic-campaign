"""Party colours for candidate slides. Arkcore asked for party colours on
candidate posts (20 Nov 2026), overriding the content plan's note.

Colours are taken from each party's logo as best we can tell. CONFIRM each one
against the official logo before its candidate post goes out. Every candidate
gets the same layout; only these three colours and the photo change.

`ink` is the text colour on the first colour.
"""

PARTIES = {
    # abbr: (full name, [three band colours], ink, confirmed?)
    "A":   ("Accord", ["#1E88E5", "#FFFFFF", "#2E7D32"], "#fff", False),
    "AA":  ("Action Alliance", ["#1B5E20", "#FFFFFF", "#C62828"], "#fff", False),
    "AAC": ("African Action Congress", ["#D32F2F", "#111111", "#FBC02D"], "#fff", False),
    "ADC": ("African Democratic Congress", ["#0B7A3B", "#FFFFFF", "#F2B705"], "#fff", False),
    "ADP": ("Action Democratic Party", ["#1565C0", "#FFFFFF", "#2E7D32"], "#fff", False),
    "APC": ("All Progressives Congress", ["#0B8F3C", "#1E50A2", "#E0242B"], "#fff", False),
    "APM": ("Allied Peoples Movement", ["#1C4EA0", "#0B8F3C", "#E0242B"], "#fff", False),
    "APP": ("Action Peoples Party", ["#2E7D32", "#FFFFFF", "#1565C0"], "#fff", False),
    "BP":  ("Boot Party", ["#5D4037", "#FFFFFF", "#2E7D32"], "#fff", False),
    "DLA": ("Democratic Leadership Alliance", ["#283593", "#FFFFFF", "#C62828"], "#fff", False),
    "LP":  ("Labour Party", ["#00843D", "#FFFFFF", "#E31B23"], "#fff", False),
    "NDC": ("Nigeria Democratic Congress", ["#C8102E", "#FFFFFF", "#0B2F6B"], "#fff", False),
    "NDP": ("National Democratic Party", ["#2E7D32", "#FFFFFF", "#F9A825"], "#fff", False),
    "NRM": ("National Rescue Movement", ["#1565C0", "#FFFFFF", "#D32F2F"], "#fff", False),
    "PDP": ("Peoples Democratic Party", ["#D21F26", "#FFFFFF", "#0B8F3C"], "#fff", False),
    "PRP": ("Peoples Redemption Party", ["#C62828", "#FFFFFF", "#111111"], "#fff", False),
    "SDP": ("Social Democratic Party", ["#E65100", "#FFFFFF", "#1565C0"], "#fff", False),
    "YPP": ("Young Progressives Party", ["#6A1B9A", "#FFFFFF", "#F9A825"], "#fff", False),
    "ZLP": ("Zenith Labour Party", ["#F57F17", "#FFFFFF", "#2E7D32"], "#111", False),
}
