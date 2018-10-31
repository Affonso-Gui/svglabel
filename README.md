## svglabel

Scripts for converting annotation files between svg (e.g. generated with *Gimp*) and json (e.g. generated with *labelme*).

### Setup

```bash
git clone https://github.com/Affonso-Gui/svglabel.git
sudo pip install -e svglabel/
```

### Basic usage

```bash
cd svglabel/examples

# Convert svg to json
svg2json with-gimp.svg image.jpg

# Test with:
labelme with-gimp.json

# Convert json to svg
json2svg with-labelme.json

# Test with:
gimp image.jpg # Paths Dialog > Import Path > with-labelme.svg
```
