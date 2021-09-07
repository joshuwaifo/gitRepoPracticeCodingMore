# install pytorch, in order to do so I ran the following in the terminal:
# pip3 install torch torchvision torchaudio

try:
    print(x@y)
except NameError:
    print("x or y or maybe both have not been defined")

# import the pytorch library
import torch

# create a tensor with 1,000 values with each value being a decimal number ranging from negative numbers to positive numbers
x_type_Tensor = torch.randn(10, 10, 10)

# increase the number of rows ie first axis (axis = 0)
z_type_Tensor = torch.cat([x_type_Tensor, x_type_Tensor], axis=0) # np.concatenate()
print('Cat axis 0:', x_type_Tensor.shape, z_type_Tensor.shape)


# increase the number of columns ie second axis (axis = 1)
z_type_Tensor = torch.cat([x_type_Tensor, x_type_Tensor], axis=1) # np.concatenate()
print('Cat axis 1:', x_type_Tensor.shape, z_type_Tensor.shape)


# create a tensor of 25 integer values from 0 to 24 of shape 5 by 5
x_type_Tensor = torch.arange(25).reshape(5, 5)
print('Max:', x_type_Tensor.shape, x_type_Tensor.max())

print(x_type_Tensor.max(dim=0))

# torch.return_types.max(values=tensor([20, 21, 22, 23, 24]),
# indices = tensor([4, 4, 4, 4, 4])

m_type_Tensor, argm_type_Tensor = x_type_Tensor.max(dim=0)
print('Max in axis 0:\n', m_type_Tensor, argm_type_Tensor)

m_type_Tensor, argm_type_Tensor = x_type_Tensor.max(dim=1)
print('Max in axis 1:\n', m_type_Tensor, argm_type_Tensor)


x_type_Tensor = torch.randn(10, 20, 30)
# rearrange axis using index to be of whatever size you choose using numpy's permute function but from PyTorch
z_type_Tensor = x_type_Tensor.permute(2, 0, 1) # np.permute()
print('Permute dimensions:', x_type_Tensor.shape, z_type_Tensor.shape)

# import the opencv-python library called cv2
import cv2
import matplotlib.pyplot as plt
# Crop image
try:
    img = img[50:250, 40:240]

    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Show image
    plt.imshow(img_gray, cmap='gray')
except NameError:
    print("img variable not defined")



def accuracy(x, y, model):
    model.eval() # <- let's wait till we get to the dropout section
    # get the prediction matrix for a tensor of `x` images
    prediction = model(x)
    # compute if the location of maximum in each row coincides with the ground truth
    max_values, argmaxes = prediction.max(-1)
    is_correct = argmaxes == y
    return is_correct.cpu().numpy().tolist()
