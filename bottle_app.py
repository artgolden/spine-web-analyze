'''Read JSON file and output svg'''
import json
import math
import numpy as np
from bottle import default_app, route, run, static_file, post, request
import SVG as svg


def parse_markers(marker_list):
    vertebras = [[], [], []]
    for i in marker_list:
        location = i["id"].split(".")[-1]
        # location = location[-1]
        if i["id"].split(".")[0] == "Klu":
            pass
        elif location == "r":
            vertebras[0].append(i)
        elif location == "c":
            vertebras[1].append(i)
        elif location == "l":
            vertebras[2].append(i)
        else:
            print "Wrong marker name"    
    return vertebras

def add_linfit_lines(vertebras, scene):
    colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0)]
    angle = 0
    for j in range(3):
        x, y = [], []
        for i in vertebras[j]:
            x.append(i["x"])
            y.append(i["y"])
        f = linear_fit(x, y)
        angle += f[0]
        fit = np.poly1d(f) 
        first_y, last_y = y[0], y[-1]
        scene.add(svg.Line((100+fit(first_y), first_y),(100+fit(last_y), last_y),colors[j],3))
    angle /= 3
    angle = math.atan(angle)/math.pi*180    
    return scene

def main(json_obj):
    image_resolution = json_obj["resolution"]
    scene = svg.Scene("Lines", image_resolution[0], image_resolution[1])
    neck_markers = [x for x in json_obj["marker_list"] if x["id"].split(".")[0][0] == 'C']
    back_markers = [x for x in json_obj["marker_list"] if x["id"].split(".")[0][0] == 'T']
    
    neck_vertebras = parse_markers((neck_markers))
    back_vertebras = parse_markers((back_markers))
    scene = add_linfit_lines(neck_vertebras, scene)
    scene = add_linfit_lines(back_vertebras, scene)


    # print "Angle average = ", angle
    # scene.add(svg.Text((200,100),"Angle = " + str(round(angle, 2)), 12))
    # scene.display()
    return scene.return_svg()


def linear_fit(y, x):
    fit = np.polyfit(x, y, 1) # returns line equation coefficients
    fit_fn = np.poly1d(fit) 
    print fit_fn
    return fit

@route('/main/<filepath:path>', method="get")
def server_static(filepath):
    return static_file(filepath, root='/home/Temason/spine/spine-web-analyze/spine-ui-prototype')

@post('/svg')
def get_json():
    json_obj = json.load(request.body)
    print "Recieved: ", json_obj
    return main(json_obj)
if __name__ == "__main__":
    run(debug=True, reloader=True)

application = default_app()
