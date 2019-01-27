def ReplaceIds(landmarks,vertices_id_map,map_mode=1):

    id_id_dict = {}
    for i in range(vertices_id_map.shape[0]):
        if map_mode==1:
            id_id_dict[vertices_id_map[i, 0]] = vertices_id_map[i, 1]
        else:
            id_id_dict[vertices_id_map[i, 1]] = vertices_id_map[i, 0]


    for i in range(landmarks.shape[0]):
        if landmarks[i] in id_id_dict.keys():
            landmarks[i] = id_id_dict[landmarks[i]]
        else:
            print("no this id = ", landmarks[i])
            landmarks[i] = 0
    return landmarks