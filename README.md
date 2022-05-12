## svglabel

Scripts for converting annotation files between svg (e.g. generated with *Gimp*) and json (e.g. generated with *labelme*).

To save paths as svg files in Gimp:
1. Make a selection
2. Select > To Path
3. Open the Paths Dialog and rename the path to the label name
4. Right click the path -> Export Path

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

### Examples

Image manipulation software provides several tools to make a selection. This can be especially useful when annotating complex objects.

In the example below, an annotation file can be easily created by using the color selection tool.

![tree_select](https://user-images.githubusercontent.com/20625381/94661688-5bee4980-0342-11eb-899b-2434b4525c09.jpg)
![tree_labelme](https://user-images.githubusercontent.com/20625381/94661709-60b2fd80-0342-11eb-99e4-fa3e9d49ac9e.jpg)
