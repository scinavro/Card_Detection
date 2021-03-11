import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.init
from torch.utils.data import DataLoader
from Custom_Dataset import CustomDataset
import CNN_Model as cnn

loaded_model = cnn.model

def load_checkpoint(checkpoint):
    print("Loading checkpoint")
    loaded_model.load_state_dict(checkpoint['state_dict'])

load_checkpoint(torch.load("my_checkpoint.pth.tar"))



dataiter = iter(cnn.test_loader)


X_test , Y_test = dataiter.next()

print(X_test.shape)

prediction = loaded_model(X_test)

print(prediction)

correct_prediction = torch.argmax(prediction, 1) == Y_test

print(torch.argmax(prediction, 1))
print(Y_test)

accuracy = correct_prediction.float().mean()
print('Accuracy:', accuracy.item())


# print(iter(cnn.test_loader).next())

# X_test = cnn.test_set