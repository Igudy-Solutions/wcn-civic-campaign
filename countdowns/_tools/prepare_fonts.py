#!/usr/bin/env python3
"""Create fixed-weight Sora instances with valid overlap flags.

Requires fonttools and skia-pathops. Run once when replacing the source font.
"""
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import OverlapMode, instantiateVariableFont
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates

assets = Path(__file__).resolve().parents[1] / '_assets'
output = assets / 'static'
output.mkdir(exist_ok=True)
for weight in (500, 600, 800):
    with TTFont(assets / 'Sora.ttf') as source:
        instance = instantiateVariableFont(
            source, {'wght': weight}, overlap=OverlapMode.REMOVE)
        if weight == 800:
            # Smooth the display-size Y shoulder steps and G crossbar overhang.
            # They look like cracks when the tightly fitted label is reduced.
            glyph_y = instance['glyf']['Y']
            assert list(glyph_y.coordinates) == [
                (211,274),(4,730),(194,730),(329,414),(354,414),(474,730),
                (654,730),(465,274),(429,274),(429,0),(247,0),(247,274)]
            kept = [i for i in range(12) if i not in (0, 7)]
            glyph_y.coordinates = GlyphCoordinates([glyph_y.coordinates[i] for i in kept])
            glyph_y.flags = bytearray(glyph_y.flags[i] for i in kept)
            glyph_y.endPtsOfContours = [len(kept) - 1]
            glyph_g = instance['glyf']['G']
            assert glyph_g.coordinates[37] == (813, 388)
            assert glyph_g.coordinates[38] == (813, 258)
            glyph_g.coordinates[37] = (753, 388)
            glyph_g.coordinates[38] = (753, 258)
        # The source is preserved. Name the adapted display instances distinctly.
        style = {500: 'Medium', 600: 'SemiBold', 800: 'ExtraBold'}[weight]
        names = {1: 'WCN Countdown', 2: style,
                 4: f'WCN Countdown {style}', 6: f'WCNCountdown-{style}',
                 16: 'WCN Countdown', 17: style}
        for record in instance['name'].names:
            if record.nameID in names:
                instance['name'].setName(names[record.nameID], record.nameID,
                                         record.platformID, record.platEncID, record.langID)
        instance.save(output / f'WCNCountdown-{weight}.ttf')
    print(f'WCNCountdown-{weight}.ttf')
