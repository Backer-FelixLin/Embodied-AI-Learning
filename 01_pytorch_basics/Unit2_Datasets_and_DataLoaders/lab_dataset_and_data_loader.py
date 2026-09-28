# 1. Dataset 是什么
"""

Dataset 就是"数据集对象"。它负责保存很多样本，每个样本通常是：
(image, label)

如：
training_data = datasets.FashionMNIST(...)
training_data就是一个 Dataset

也可以像列表一样取一个样本：
img, label = training_data[0]
意思是：取第0个训练样本，得到一张图片 img 和它的标签 label。

对 FashionMNIST 来说：
img = 衣服图片
label = 这张图片属于哪一类，比如 T-Shirt, Trouser, Sneaker

”"""

# 2. DataLoader 是什么
"""

Dataset 一次智能很方便地拿一个样本，但训练模型时通常不会一张一张喂，而是一批一批喂。

所以DataLoader的作用是：
把 Dataset 包装起来，自动帮你按 batch 取数据。

代码：
train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
意思是：
从training_data里面取数据，每次取64个样本，训练时打乱顺序

然后可以这样拿一批数据：
train_features,train_labels = next(iter(train_dataloader))
这里：
train_features = 一批图片
train_labels = 这一批图片对应的标签
如果batch_size=64，FashionMNIST的shape通常是：
train_features.shape # [64, 1, 28, 28]
train_labels.shape # [64]
意思是：
64张图片
每张图片一个通道
图片大小28x28
对应64个标签

"""

# 3. batch_size 是什么
"""

batch_size就是“一次喂给模型多少个样本”。

比如：
batch_size=64
就是一次给模型64张图片。

如果有60000张训练图片，batch_size=64，那训练一整轮大概会分成很多批：
第一批：64张
第二批：64张
第三批：64张
...

"""

# 4. shuffle=True 为什么用于训练集
"""

shuffle=True的意思是：每一轮训练时，把训练数据顺序打乱。

如果数据顺序是：
先全是T-Shirt
再全是Trouser
再全是Sneaker
模型可能会受到顺序影响。打乱后，每个batch里数据更混合，训练通常更稳定。

所以训练集通常写：
train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
测试集通常可以写：
train_dataloader = DataLoader(test_data, batch_size=64, shuffle=False)

"""

# 5. train_dataset 和 test_dataset 区别
"""

training_data = datasets.FashionMNIST(train=True, ...)
test_data = datasets.FashionMNIST(train=False, ...)
train_data是给模型学习用的。模型会根据训练集不断调整参数。
test_data是考试用的。模型不能用测试集来学习，只能训练完之后拿它检查效果。

"""