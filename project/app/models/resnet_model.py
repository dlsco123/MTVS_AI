import torch
import torchvision
import torchvision.transforms as transforms
from PIL import Image
import io

model = torchvision.models.resnet34()
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, 10)
model.load_state_dict(torch.load("data/cifar_resnet34.pth"))
model.eval()

transform = transforms.Compose(
    [transforms.Resize((224, 224)),
     transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

def classify_image(image_data):
    image = Image.open(io.BytesIO(image_data))
    image = transform(image).unsqueeze(0)
    outputs = model(image)
    _, predicted = torch.max(outputs, 1)
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    label = class_names[predicted[0].item()]
    return label