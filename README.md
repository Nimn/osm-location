OSM location: A Plugin for Pelican
====================================================

[![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/osm-location/build)](https://github.com/pelican-plugins/osm-location/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-osm-location)](https://pypi.org/project/pelican-osm-location/)
![License](https://img.shields.io/pypi/l/pelican-osm-location?color=blue)

ap at the begin of a page if a location is defined

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-osm-location

Usage
-----

<<Add plugin details here>>



Include Leaflet CSS and JavaScript in the head section of your base.html template:

``` html
<!-- Insert before your custom CSS -->
 <link rel="stylesheet" href="https://unpkg.com/leaflet@1.8.0/dist/leaflet.css"
   integrity="sha512-hoalWLoI8r4UszCkZ5kL8vayOGVae1oxXe/2A4AO6J9+580uKHDO3JdHb7NzwwzK5xr/Fs0W40kiNHxM9vyTtQ=="
   crossorigin=""/>
 <!-- Make sure you put this AFTER Leaflet's CSS -->
 <script src="https://unpkg.com/leaflet@1.8.0/dist/leaflet.js"
   integrity="sha512-BB3hKbKWOc9Ez/TAwyWxNXeoV9c1v6FIeYiBieIWkpLjauysF18NzgR1MBNBXf8/KABdlkX68nAhlwcDFLGPCQ=="
   crossorigin=""></script>
```

Add this entry to your CSS:

``` css
.osm-map {
    height: 180px;
    border: 1px solid #CCC;
    border-radius: 4px;
}
.osm-map img { /* could be necessary if your theme change all img CSS */
    box-shadow: 0; 
    border: 0;
}
   
```


Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/osm-location/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

License
-------

This project is licensed under the AGPL-3.0 license.
