import png 
from os import walk 

backplate = False 

filenames = next(walk('inputs'), (None, None, []))[2]

for img_path in filenames: 

    read_image = png.Reader(filename=f'inputs//{img_path}').asDirect() 
    rgb_matrix = [list(row) for row in read_image[2]] 

    new_rgb_matrix = []
    black = lambda val: 0 <= val <= 100
    white = lambda val: 155 <= val <= 255

    mass_count = 0
    dist_sum = 0 
    for row in rgb_matrix: 
        new_rgb_matrix.append([]) 
        for i in range(0, len(row), 4): 
            if black(row[i]) and black(row[i+1]) and black(row[i+2]): 
                new_rgb_matrix[-1].extend([0,0,0,255])
                mass_count += 3 if backplate else 1
                dist_sum += ((i+1) // 4) * (3 if backplate else 1)
            elif backplate and white(row[i]) and white(row[i+1]) and white(row[i+2]): 
                new_rgb_matrix[-1].extend([255,0,0,255])
                mass_count += 1
                dist_sum += (i+1) // 4
            else: 
                new_rgb_matrix[-1].extend([255,0,0,255])

    final_com = dist_sum // mass_count
    for row in new_rgb_matrix: 
        for i in range(-3, 3, 1): 
            row[(final_com + i) * 4] = 0

    write_image = png.Writer(read_image[3]['size'][0], read_image[3]['size'][1], greyscale=False, bitdepth=read_image[3]['bitdepth'], alpha=True) 
    write_image.write(open(f'outputs//{img_path}', 'wb'), new_rgb_matrix)
