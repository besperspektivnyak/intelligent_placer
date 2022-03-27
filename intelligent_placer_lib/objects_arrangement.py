import cv2 as cv

# is polygon area larger than sum of objects area
def check_area(polygon: list, objects: list) -> bool:
    poly_area = cv.contourArea(polygon)
    obj_area = 0
    for obj in objects:
        obj_area += cv.contourArea(obj)
    return poly_area > obj_area


# except check_area there will be other checks, ex. geometric shapes
def is_objects_placed(polygon: list, objects: list) -> bool:
    if check_area(polygon, objects):
        return True
    else:
        return False
