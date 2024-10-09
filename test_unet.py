import torch  
import torchvision.models as models  
import torchvision.transforms as transforms  
from PIL import Image  
  
# 确保模型在GPU上运行（如果有的话）  
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  
  
# 加载预训练的模型  
model = models.Unet(pretrained=True)  
model = model.to(device)  
model.eval()  # 设置模型为评估模式  
  
# 加载并预处理图像  
# 假设我们有一个名为 'image.jpg' 的图像文件  
image_path = '/home/wudi/code/yolov5-6.0/data/images/bus.jpg'  
image = Image.open(image_path)  
  
# 图像预处理：调整为模型所需的输入大小，转换为Tensor，归一化等  
preprocess = transforms.Compose([  
    transforms.Resize(256),  
    transforms.CenterCrop(224),  
    transforms.ToTensor(),  
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  
])  
  
input_tensor = preprocess(image)  
input_batch = input_tensor.unsqueeze(0).to(device)  # create a mini-batch as expected by the model  
  
# 如果模型接受多个输入（例如，用于多视图分类），请确保输入张量是一个列表  
# input_batch = [input_tensor.to(device)]  
  
# 进行推理  
with torch.no_grad():  
    output = model(input_batch)  
  