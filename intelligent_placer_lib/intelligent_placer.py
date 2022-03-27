from intelligent_placer_lib.objects_detection import read_image, preprocess_image, find_contours, find_min_rect, find_approx_polygon
from intelligent_placer_lib.objects_arrangement import is_objects_placed


def check_image(path: str) -> bool:
    image = read_image(path)
    edge = preprocess_image(image)
    polygon, objects = find_contours(edge)
    if polygon is None or objects == []:
        print("Can't find polygon or objects")
        return False
    rectangles = find_min_rect(objects)
    polygon_angles = find_approx_polygon(polygon)
    return is_objects_placed(polygon_angles, rectangles)
