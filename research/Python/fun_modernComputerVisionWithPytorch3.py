import pydrive.settings
import torch
import numpy as np, cv2, pandas as pd, glob, time
import matplotlib.pyplot as plt
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchvision
from torchvision import transforms, models, datasets
device_type_str = 'cuda' if torch.cuda.is_available() else 'cpu'

# pip install pydrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import oauth2client

# pip install google-colab
try:
    from google.colab import auth
except ModuleNotFoundError:
    print(" pip install google-colab not working for me at the moment")

from oauth2client.client import GoogleCredentials

try:
    auth.authenticate_user()
except NameError:
    print("Currently unable to import auth from google.colab")
gauth_type_GoogleAuth = GoogleAuth()

# run pip install oauth2client
try:
    gauth_type_GoogleAuth.credentials = GoogleCredentials.get_application_default()
except oauth2client.client.ApplicationDefaultCredentialsError:
    print("Credentials are currently not available")

drive_type_GoogleDrive = GoogleDrive(gauth_type_GoogleAuth)

def getFile_from_drive(file_id_type_str, name_type_str):
    downloaded_type_GoogleDriveFile = drive_type_GoogleDrive.CreateFile(
        {
            'id': file_id_type_str
        }
    )
    downloaded_type_GoogleDriveFile.GetContentFile(name_type_str)

try:
    getFile_from_drive( '1Z1RqRo0_JiavaZw2yzZG6WETdZQ8qX86', 'fairface-img-margin025-trainval.zip')
    getFile_from_drive( '1k5vvyREmHDW5TSM9QgB04Bvc8C8_7dl-', 'fairface-label-train.csv')
    getFile_from_drive( '1_rtz1M1zhvS0d5vVoXUamnohB6cJ02iJ', 'fairface-label-val.csv' )
except pydrive.settings.InvalidConfigError:
    print("Due to the Google drive credentials being missing here from the tutorial I am following, the getFile_from_drive function doesn't work at the moment")



# run this command in the terminal:     unzip -qq fairface-img-margin025-trainval.zip
try:
    trn_df = pd.read_csv('fairface-label-train.csv')
    val_df = pd.read_csv('fairface-label-val.csv')
    trn_df.head()
except FileNotFoundError:
    print("Unable to read the csv files as they are unavailable at the moment")

IMAGE_SIZE_type_int = 224
class GenderAgeClass(Dataset):
    def __init__(self, df, tfms=None):
        self.df = df
        self.normalize = transforms.Normalize(
            mean = [0.485, 0.456, 0.406],
            std = [0.229, 0.224, 0.225]
        )

    def __len__(self):
        return len(self.df)

    def __getitem__(self, ix):
        f = self.df.iloc[ix].squeeze
        file = f.file
        gen = f.gender == 'Female'
        age = f.age
        im = cv2.imread(file)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        return im, age, gen