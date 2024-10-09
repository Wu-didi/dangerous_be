# python train.py --device 6,7 --batch 256 --cfg yolov5s-p2-v2.yaml
# python train.py --device 6,7 --batch 128 --cfg yolov5s_hefei_v2.4.yaml
# python train.py --device 2,3 --batch 64 --cfg yolov5m-p2.yaml
# yolov5s-p2-hefei-v2.4.yaml
#  python train.py --cfg yolov5s_hefei_v2.4_CA.yaml  --batch 32 --imgsz 640

#  python train.py --cfg /home/wudidi/code_v2/dangerous_be/models/dangerous_be.yaml --batch 16 --noautoanchor --imgsz 1280 --data /home/wudidi/code_v2/dangerous_be/data/dangerous_be.yaml


python val.py --data /home/wudidi/code_v2/dangerous_be/data/dangerous_be.yaml \
--weights /home/wudidi/code_v2/dangerous_be/runs/train/exp/weights/best.pt --img 1280