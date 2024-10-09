from yolov5.detect_extract_feature import run,main,parse_opt




def get_features():
    opt = parse_opt()
    features =  main(opt)
    return features

    


print(get_features())
