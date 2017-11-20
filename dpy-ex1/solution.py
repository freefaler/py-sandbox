def rotate_left(image):
    # create a new empty list with the desired size rotated`
    rotated_image = []
    img_w, img_h = len(image[0]), len(image)
    rotated_image = [[None] * img_h for i in range(img_w)]

    # for cycle to construct our new rotated image
    cur_row = 0
    for image_row in image:
        # fill backwards from end to begining (left rotation)
        cur_pos = 0
        for image_pixel in image_row:
            rotated_image[img_w - 1 - cur_pos][cur_row] = image_pixel
            cur_pos = cur_pos + 1
        cur_row = cur_row + 1

    return rotated_image


def rotate_right(image):
    # create a new empty list with the desired size rotated`
    rotated_image = []
    img_w, img_h = len(image[0]), len(image)
    rotated_image = [[None] * img_h for i in range(img_w)]

    # for cycle to construct our new rotated image
    row_numb = 0
    for image_row in image:
        col_numb = 0
        for image_pixel in image_row:
            rotated_image[col_numb][(img_h - 1) - row_numb] = image_pixel
            col_numb = col_numb + 1
        row_numb = row_numb + 1

    return rotated_image    


def invert(image):
    rotated_image = []
    
    row_numb = 0
    for image_row in image:
        # adding new empty list
        rotated_image.append([])
        for r, g, b in image_row:
            rotated_image[row_numb].append((abs(r - 255), abs(g - 255), abs(b - 255)))
            pass
        row_numb = row_numb + 1 
        pass

    return rotated_image


def lighten(image, lighten_by):
    rotated_image = []
    row_numb = 0
    for image_row in image:
        # adding new empty list
        rotated_image.append([])
        for r, g, b in image_row:
            rotated_image[row_numb].append((
                int(r + lighten_by * (255 - r)), 
                int(g + lighten_by * (255 - g)), 
                int(b + lighten_by * (255 - b))
            )
            )
        row_numb = row_numb + 1 

    return rotated_image


def darken(image, darken_by):
    rotated_image = []
    row_numb = 0
    for image_row in image:
        # adding new empty list
        rotated_image.append([])
        for r, g, b in image_row:
            rotated_image[row_numb].append((
                int(r - darken_by * (r - 0)), 
                int(g - darken_by * (g - 0)), 
                int(b - darken_by * (b - 0))
            )
            )
        row_numb = row_numb + 1 

    return rotated_image


def create_histogram(image):
    histogram = {'red': {}, 'green': {}, 'blue': {}}
    # for each row of the image
    for image_row in image:
        for r, g, b in image_row:
            if r not in histogram['red']:
                histogram['red'][r] = 0
            histogram['red'][r] += 1

            if g not in histogram['green']:
                histogram['green'][g] = 0
            histogram['green'][g] += 1

            if b not in histogram['blue']:
                histogram['blue'][b] = 0
            histogram['blue'][b] += 1
    
    return histogram


def row_to_column(arr, row, colmn):
    return arr


def column_to_row(arr, colmn, row):
    return arr


testpix = [
    (("ar1", "ag1", "ab1"), ("ar2", "ag2", "ab2"), ("ar3", "ag3", "ab3")),
    (("br1", "bg1", "bb1"), ("br2", "bg2", "bb2"), ("br3", "bg3", "bb3")),
    (("cr1", "cg1", "cb1"), ("cr2", "cg2", "cb2"), ("cr3", "cg3", "cb3")),
    (("dr1", "dg1", "db1"), ("dr2", "dg2", "db2"), ("dr3", "dg3", "db3"))
]


# img_w = 3, img_h = 4
newpix = [
    ("a1", "a2", "a3"),
    ("b1", "b2", "b3"),
    ("c1", "c2", "c3"),
    ("d1", "d2", "d3")
]


# print(rotate_right(newpix))

