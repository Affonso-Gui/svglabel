import base64
import json
import os.path
from PIL import Image
import svgpathtools as svg


# svg2json

def get_points(path, seg):
    acc = []
    close_shape = None
    last_end = None
    for p in path:
        # close any open shapes before proceeding to the next point
        if last_end and p.start != last_end:
            # quickfix: labelme not recognizing exactly same points?
            acc.append([last_end.real, last_end.imag + 0.001])
            if close_shape:
                acc.append(close_shape)
            else:
                close_shape = acc[-1]

        # add the point
        acc.append([p.start.real, p.start.imag])
        # add any additional segment points
        for i in range(seg):
            val = float(i) / (seg + 1)
            point = p.point(val)
            acc.append([point.real, point.imag])
        last_end = p.end
    acc.append([last_end.real, last_end.imag + 0.001])
    return acc

def make_obj(filename):
    with open(filename, 'rb') as f: imageData = f.read()
    imageData = base64.b64encode(imageData).decode('utf-8')
    imagePath = os.path.relpath(filename)
    return dict(
        imagePath = imagePath,
        imageData = imageData,
        lineColor = [0,255,0,128],
        fillColor = [255,0,0,128],
        shapes = [],
    )

def make_shape():
    return dict(
        label = '',
        points = [],
        line_color = None,
        fill_color = None,
    )

def svg2json(svgfile, imfile, outfile=None, labelfile=None, segments=10):
    paths, attributes = svg.svg2paths(svgfile)
    obj = make_obj(imfile)

    if labelfile: label_lst = [l.rstrip('\n') for l in open(labelfile)]

    for path, attr in zip(paths,attributes):
        if labelfile:
            label_name = attr['id'].split()[0]
            if label_name not in label_lst:
                raise Exception('No such label: {}'.format(label_name))

        shape = make_shape()
        shape['points'] = get_points(path,segments)
        shape['label'] = attr['id']
        obj['shapes'].append(shape)

    obj['shapes'].reverse()
    outfile = outfile or os.path.splitext(svgfile)[0] + '.json'
    with open(outfile,'w') as f: json.dump(obj,f,indent=True)
    print('Wrote to {}'.format(outfile))

# json2svg

def get_path(points):
    acc = []
    start = complex(*points[0])
    points = points[1:] + points[:1]
    for p in points:
        end = complex(*p)
        line = svg.Line(start, end)
        acc.append(line)
        start = end
    return svg.Path(*acc)

def make_attributes(id):
    return {
        'id': id,
        'fill': 'none',
        'stroke': 'black',
        'stroke-width': 1
    }

def make_svg_attributes(imfile):
    im = Image.open(imfile)
    w,h = im.size
    return dict(
        width = w,
        height = h,
        viewBox = '0 0 {} {}'.format(w,h),
        xmlns = 'http://www.w3.org/2000/svg',
    )    

def json2svg(jsonfile, outfile=None):
    with open(jsonfile) as f: obj = json.load(f)
    svg_attributes = make_svg_attributes(obj['imagePath'])
    attributes = []
    paths = []

    for shape in obj['shapes']:
        path = get_path(shape['points'])
        attr = make_attributes(shape['label'])
        paths.append(path)
        attributes.append(attr)

    paths.reverse()
    attributes.reverse()
    outfile = outfile or os.path.splitext(jsonfile)[0] + '.svg'
    svg.wsvg(
        paths=paths,
        filename=outfile,
        attributes=attributes,
        svg_attributes=svg_attributes,
    )
    print('Wrote to {}'.format(outfile))
