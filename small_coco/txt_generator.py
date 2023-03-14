import json
f = open("C:/Users/efeml/Downloads/tiny-coco-master/tiny-coco-master/small_coco/instances_train2017_small.json")
labels = json.load(f)
custom_dataset_ids={4: 0, 
13: 5, 
1: 6 ,
14: 7 ,
8: 8,
5: 10,
2: 12,
15: 14,
19: 18,
16: 19,
26: 23,
17: 26,
3: 31,
0: 32,
18: 34,
28: 39,
9: 40,
11: 41, #stop sign
7: 44,
25: 45}
for i in labels['images']:
    f_name = i['file_name']
    f_id = i['id']
    height=i['height']
    width=i['width']
    anno_list=[]
    f = open('{}.txt'.format(f_name), 'w')
    for a in labels['annotations']:
        if a['image_id'] == f_id and (a['category_id'] in custom_dataset_ids.keys()):
            bbox = a['bbox']
            ### normalize bbox
            normalized_bbox = [bbox[0]/width,bbox[1]/height,bbox[2]/width,bbox[3]/height]
            #temp = [custom_dataset_ids[a['category_id']], normalized_bbox]
            f.write("{} {} {} {} {}\n".format(custom_dataset_ids[a['category_id']],normalized_bbox[0],normalized_bbox[1],normalized_bbox[2],normalized_bbox[3]))
            #f.write("{} {} {} {} {}\n".format(a['category_id'],normalized_bbox[0],normalized_bbox[1],normalized_bbox[2],normalized_bbox[3]))

