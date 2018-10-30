## svglabel

Scripts for converting annotation files between svg (e.g. generated with *Gimp*) and json (e.g. generated with *labelme*).

### Basic usage

```
cd svglabel

# Convert svg to json
./svg2json.py examples/with-gimp.svg examples/image.jpg

# Convert json to svg
./json2svg.py examples/with-labelme.json
```
