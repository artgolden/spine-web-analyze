'''Read JSON file and output svg and data'''
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

def single_vert_angle(vert_r, vert_l, proj):
    x = vert_l["x"] - vert_r["x"]
    y = vert_l["y"] - vert_r["y"]
    yyy = float(abs(y))
    horiz_angle = round(math.atan(yyy / x) * 180 / math.pi, 2)
    if proj == "FRONT":
        if abs(y) < 2:
            y = 0
        if y > 0:
            tilt = "LEFT"
            horiz_angle_signed = horiz_angle * -1
        elif y == 0:
            tilt = "NONE"
            horiz_angle_signed = horiz_angle 
        else:
            tilt = "RIGHT"
            horiz_angle_signed = horiz_angle
    elif proj == "SIDE":
        if abs(y) < 2:
            y = 0
        if y > 0:
            tilt = "POSTERIOR"
            horiz_angle_signed = horiz_angle * -1
        elif y == 0:
            tilt = "NONE"
            horiz_angle_signed = horiz_angle
        else:
            tilt = "ANTERIOR"
            horiz_angle_signed = horiz_angle
    print horiz_angle, "Tilt to the ", tilt, "   (from the patients prespective)", y, x
    return str(abs(horiz_angle)) + "," + str(tilt), horiz_angle_signed
    # if proj == "FRONT":
    # else:
    #     return [abs(horiz_angle), str(tilt), horiz_angle_signed]


def average_angle(angle, proj):
    if angle < 0.01:
        angle = 0
    if proj == "FRONT":
        if angle > 0:
            tilt = "LEFT"
        elif angle == 0:
            tilt = "NONE"
        else:
            tilt = "RIGHT"
    elif proj == "SIDE":
        if angle > 0:
            tilt = "ANTERIOR"
        elif angle == 0:
            tilt = "NONE"
        else:
            tilt = "POSTERIOR"
    return str(round(angle, 2)) + "," + str(tilt) + "\n"

def between_angle(up_r, up_l, down_r, down_l, proj):
    angle_up = single_vert_angle(up_l, up_r, proj)[1]
    angle_down = single_vert_angle(down_l, down_r, proj)[1]
    if abs(angle_down) < abs(angle_up):
        angle = angle_up - angle_down
    else:
        angle = angle_down - angle_up

    if proj == "FRONT":
        if angle < 0:
            tilt = "LEFT"
        elif angle == 0:
            tilt = "NONE"
        else:
            tilt = "RIGHT"
    elif proj == "SIDE":
        if angle < 0:
            tilt = "POSTERIOR"
        elif angle == 0:
            tilt = "NONE"
        else:
            tilt = "ANTERIOR"
    return str(angle) + "," + tilt
 
def vert_horiz_angles(vertebras, proj, pair_switch):
    out = ""
    # out2 = ""
    # upper = single_vert_angle(vertebras[0][0], vertebras[2][0])
    if not pair_switch:
        for i in range(len(vertebras[0])):
            if vertebras[0][i]["id"].split(".")[0][0] == "C":
                curr = single_vert_angle(vertebras[0][i], vertebras[2][i], proj)[0]
                vert = vertebras[0][i]["id"].split(".")[0]
                out += curr + "," + vert + "\n"
    else:
        for i in range(len(vertebras[0]) - 1):
            if vertebras[0][i]["id"].split(".")[0][0] == "C" and vertebras[0][i + 1]["id"].split(".")[0][0] == "C":
                up_l, up_r = vertebras[0][i], vertebras[2][i]
                down_l, down_r = vertebras[0][i + 1], vertebras[2][i + 1]
                between = between_angle(up_r, up_l, down_r, down_l, proj)
                vert_up = vertebras[0][i]["id"].split(".")[0]
                vert_down = vertebras[0][i + 1]["id"].split(".")[0]
                out += between + "," + vert_up + "-" + vert_down + "\n"
    return out


def klukovidn_dist_angles(klukovidn, vertebras):
    print klukovidn, vertebras
    out = ""
    out += "Distance,,Vertebra to whitch\n"
    out += "Right Klukovidn\n"
    out += klu_dist(klukovidn[0], vertebras[1][0])
    out += klu_dist(klukovidn[0], vertebras[1][2])
    out += "Left Klukovidn\n"
    out += klu_dist(klukovidn[1], vertebras[1][0])
    out += klu_dist(klukovidn[1], vertebras[1][2])
    out += "Klukovidn angles\n"
    out += "Angle,Side\n"
    out += klu_angle(klukovidn[0], vertebras[1][0], vertebras[1][2])
    out += ",RIGHT\n"
    out += klu_angle(klukovidn[1], vertebras[1][0], vertebras[1][2])
    out += ",LEFT\n"
    return out

def pelvis_shift(vertebras):
    c3_center = vertebras[0][0]["x"] + abs((vertebras[0][0]["x"] - vertebras[2][0]["x"]) / 2)
    print c3_center
    shift = c3_center - vertebras[0][5]["x"]
    shift = round(shift)
    if shift > 0:
        direction = "ANTERIOR"
    elif shift < 0:
        direction = "POSTERIOR"
        shift = abs(shift)
    else:
        direction = "NO"
    return str(shift) + "," + direction
    
def klu_angle(klu, vert_up, vert_down):
    angle = three_dot_angle(klu["x"], klu["y"],\
     vert_up["x"], vert_up["y"], vert_down["x"], vert_down["y"])

    return str(angle)

def three_dot_angle(x1, y1, x2, y2, x3, y3): #points 2 and 3 on the sides of an angle
    ax = x1 - x2
    bx = x1 - x3
    ay = y1 - y2 
    by = y1 - y3
    a = math.sqrt(ax **2 + ay **2)
    b = math.sqrt(bx **2 + by **2)
    angle = math.acos((ax * bx + ay * by) / abs(a) / abs(b))
    angle = angle * 180 / math.pi
    return angle 

def klu_dist(klu, C_vert):
    dist = math.sqrt((klu["x"] - C_vert["x"])**2 + (klu["y"] - C_vert["y"])**2)
    return str(round(dist, 2)) + "," + "," + C_vert["id"].split(".")[0] + "\n"

def linear_fit(y, x):
    fit = np.polyfit(x, y, 1) # returns line equation coefficients
    # fit_fn = np.poly1d(fit) 
    # print fit_fn
    return fit
    
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
        scene.add(svg.Line((100+fit(first_y), first_y), (100+fit(last_y), last_y),colors[j],3))
    angle /= 3
    angle = math.atan(angle) / math.pi * 180    
    print "Angle average = ", angle
    # scene.add(svg.Text((200, 200), angle, 24, (255, 255, 255)))
    return scene, angle 

def front_proj_code(json_obj):
    proj = "FRONT"
    image_resolution = json_obj["resolution"]
    scene = svg.Scene("Lines", image_resolution[0], image_resolution[1])
    neck_markers = [x for x in json_obj["marker_list"] if x["id"].split(".")[0][0] == 'C']
    back_markers = [x for x in json_obj["marker_list"] if x["id"].split(".")[0][0] == 'T']
    klukovidn = [x for x in json_obj["marker_list"] if x["id"].split(".")[0][0] == 'K']
    neck_vertebras = parse_markers((neck_markers))
    back_vertebras = parse_markers((back_markers))
    scene, angle_neck = add_linfit_lines(neck_vertebras, scene)
    scene, angle_back = add_linfit_lines(back_vertebras, scene)
    # f = open("/home/Temason/spine/spine-web-analyze/angles.csv", "w")
    f = open("angles.csv", "w")
    f.write("Angles from vertical axis.\n")
    f.write("Angle,Tilt,Vertebra\n")
    f.write("Neck vertabras\n")
    f.write(vert_horiz_angles(neck_vertebras, proj, False))
    f.write("Neck vertabras angle average\n")
    f.write(average_angle(angle_neck, proj))
    f.write("Back vertabras\n")
    f.write(vert_horiz_angles(back_vertebras, proj, False))
    f.write("Back vertabras angle average\n")
    f.write(average_angle(angle_back, proj))
    f.write("Distances from klukovidni\n")
    f.write(klukovidn_dist_angles(klukovidn, neck_vertebras))
    # print klukovidn_dist_angles(klukovidn, neck_vertebras)
    f.close()
    # scene.add(svg.Text((200,100),"Angle = " + str(round(angle, 2)), 12))
    # scene.display()
    return scene.return_svg()

def side_proj_code(json_obj):
    proj = "SIDE"
    # image_resolution = json_obj["resolution"]
    neck_markers = [x for x in json_obj["marker_list"] if x["id"].split(".")[0][0] in ['C']]
    pelvis = [x for x in json_obj["marker_list"] if x["id"].split(".")[0][0] in ['S']]
    neck_vertebras = parse_markers((neck_markers))
    pelvis = pelvis[0]
    print pelvis, "==============="
    # f = open("/home/Temason/spine/spine-web-analyze/angles.csv", "w")
    f = open("angles.csv", "w")
    f.write("that SIDE projection------")
    f.write("Angles from vertical axis.\n")
    f.write("Angle,Tilt,Vertebra\n")
    f.write("Neck vertabras\n")
    f.write(vert_horiz_angles(neck_vertebras, proj, False))
    f.write("Pairwise angles between vertebras \n")
    f.write(vert_horiz_angles(neck_vertebras, proj, True))
    f.write("Pelvis shift \n")
    t = neck_vertebras
    t[0].append(pelvis)
    f.write(pelvis_shift(t))
    f.close()
    

def main(json_obj):
    if json_obj["projection"] == "FRONT": 
        front_proj_code(json_obj)
    elif json_obj["projection"] == "SIDE":
        side_proj_code(json_obj)


@route('/main/<filepath:path>', method="get")
def server_static(filepath):
    # return static_file(filepath, root='/home/Temason/spine/spine-web-analyze/spine-ui-prototype')
    return static_file(filepath, root='/home/tema/spine_web/spine-ui-prototype')
    
@route('/angles.csv', method="get")
def measurements_file():
    return static_file("angles.csv", root='/home/tema/spine_web/')
    # return static_file("angles.csv", root='/home/Temason/spine/spine-web-analyze/')
@post('/svg')
def get_json():
    json_obj = json.load(request.body)
    # print "Recieved: ", json_obj
    return main(json_obj)
if __name__ == "__main__":
    run(debug=True, reloader=True)

# application = default_app()
