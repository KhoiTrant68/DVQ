from easydict import EasyDict as edict

DefaultDataPath = edict()

DefaultDataPath.ImageNet = edict()

# DefaultDataPath.ImageNet.root = "Your Data Path/Datasets/ImageNet"
# DefaultDataPath.ImageNet.train_write_root = "Your Data Path/Datasets/ImageNet/train"
# DefaultDataPath.ImageNet.val_write_root = "Your Data Path/Datasets/ImageNet/val"

DefaultDataPath.ImageNet.root = "/kaggle/input/imagenetmini-1000/imagenet-mini"
DefaultDataPath.ImageNet.train_write_root = "/kaggle/input/imagenetmini-1000/imagenet-mini/train"
DefaultDataPath.ImageNet.val_write_root = "/kaggle/input/imagenetmini-1000/imagenet-mini/val"