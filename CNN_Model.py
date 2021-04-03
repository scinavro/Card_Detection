import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.init
from torch.utils.data import DataLoader
from Custom_Dataset import CustomDataset

device = "cuda" if torch.cuda.is_available() else "cpu"

learning_rate = 0.001
training_epochs = 3
batch_size = 50
num_types = 5


dataset = CustomDataset(
    csv_file="mycsv.csv", root_dir="Resources", transform=transforms.ToTensor()
)

train_set = torch.utils.data.random_split(dataset, len(dataset))
train_loader = DataLoader(
    dataset=train_set, batch_size=batch_size, shuffle=True, drop_last=True
)


class CNN(torch.nn.Module):
    def __init__(self):
        super(CNN, self).__init__()

        self.layer1 = torch.nn.Sequential(
            torch.nn.Conv2d(1, 32, kernel_size=(3, 3), stride=1, padding=(1, 1)),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=(2, 2), stride=2),
        )

        self.layer2 = torch.nn.Sequential(
            torch.nn.Conv2d(32, 64, kernel_size=(3, 3), stride=1, padding=(1, 1)),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=(2, 2), stride=2),
        )

        self.fc = torch.nn.Linear(50 * 50 * 64, num_types, bias=True)

        torch.nn.init.xavier_uniform_(self.fc.weight)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.view(out.size(0), -1)
        out = self.fc(out)
        return out


def save_checkpoint(state, filename="my_checkpoint.pth.tar"):
    print("Saving checkpoint")
    torch.save(state, filename)


model = CNN().to(device)

criterion = torch.nn.CrossEntropyLoss().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


total_batch = len(train_loader)

if __name__ == "__main__":
    for epoch in range(training_epochs):
        avg_cost = 0

        for X, Y in train_loader:

            X = X.to(device)
            Y = Y.to(device)

            optimizer.zero_grad()
            hypothesis = model(X)
            cost = criterion(hypothesis, Y)
            cost.backward()
            optimizer.step()

            avg_cost += cost / total_batch

        print("[Epoch: {:>4}] cost = {:>.9}".format(epoch + 1, avg_cost))

    checkpoint = {"state_dict": model.state_dict()}
    save_checkpoint(checkpoint)