def calc_length(point_1, point_2):
    assert len(point_1) == 2 and len(point_2) == 2

    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5
