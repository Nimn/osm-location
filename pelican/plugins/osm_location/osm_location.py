from pelican import signals


def sequence_gen(genlist):
    for gen in genlist:
        yield from gen


MAP_TEMPLATE = """
 <div class="osm-map" id="map-{slug}"></div>
"""
JS_TEMPLATE = """
<script>
var map_{slug} = L.map('map-{slug}').setView([{lat}, {lon}], 13);
L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}}).addTo(map_{slug});
L.control.scale().addTo(map_{slug});
{markers}
</script>
"""
MARKER_TEMPLATE = """
var marker_{slug}_{idx} = L.marker([{lat}, {lon}]).addTo(map_{slug});
"""
MARKER_POP = """
marker_{slug}_{idx}.bindPopup("{text}");
"""


def add_location(article_or_page_generator):
    all_content = [
        getattr(article_or_page_generator, attr, None)
        for attr in ["articles", "drafts", "pages"]
    ]
    all_content = [x for x in all_content if x is not None]
    for article in sequence_gen(all_content):
        metadata_keys = list(article.metadata.keys())
        locations = []
        for key in sorted(metadata_keys):
            if key.startswith("location"):
                location = article.metadata[key]
                locations.append([
                    item.strip()
                    for item in location.split(";")
                ])
        if not locations:
            return
        slug = article.slug.replace("-", "_")
        content, markers, lat, lon = "", "", None, None
        for idx, location in enumerate(locations):
            if len(location) < 2:
                continue
            try:
                lat, lon, desc = float(location[0]), float(location[1]), ";".join(location[2:])
            except ValueError:
                continue
            if not content:
                content = MAP_TEMPLATE.format(slug=slug)
                content += article._content
            markers += MARKER_TEMPLATE.format(slug=slug, idx=idx, lat=lat, lon=lon)
            if desc:
                markers += MARKER_POP.format(slug=slug, idx=idx, text=desc)

        if not content:
            return
        content += JS_TEMPLATE.format(slug=slug, lat=lat, lon=lon, markers=markers)
        article._content = content


def register():
    signals.article_generator_finalized.connect(add_location)
    signals.page_generator_finalized.connect(add_location)
