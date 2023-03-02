# Overview
The main goal of this baseline is to have a skeleton code base structure for pytorch lightning with some nice configurations. Some of the libraries and frameworks I will be usign are listed below.

* <a href="https://pypi.org/project/tqdm/">tqdm</a>
* <a href="https://docs.python.org/3/library/logging.html">logging</a>
* <a href="https://pypi.org/project/rich/">rich</a>
* <a href="https://github.com/lebrice/SimpleParsing">simple-parsing</a>
* <a href="https://clear.ml/docs/latest/docs">clearML</a>
* <a href="https://pypi.org/project/split-folders/">split-folders</a>

# Requirements
```
pytorch
pytorch-lightning
clearml
rich
tqdm
split-folders
simple-parsing
```

# Details
## Dataset
I downloaded and use <a href="https://www.kaggle.com/datasets/alessiocorrado99/animals10">Animal-10</a> function directly. dataset to make this demo. Then I useds `utils/reduce.py` to reduce the datatset size to approx. 50 examples per category for quick testing.

I wrote custom dataloader to process and load this data located at `utils/dataloader.py`. It can be modified depending on the use case. We can also just use <a href="https://pytorch.org/vision/main/generated/torchvision.datasets.ImageFolder.html">ImageFolder</a> dataloader directly.

## Configuration
I defined some custom configuration inside the `config` folder. 

The first one is `args.py` which contains the hyperparameters. In my baseline, I am using <a href="https://github.com/lebrice/SimpleParsing">simple-parsing</a> to parse the arguments due to its clean interface. For that purpose, I define a simple `dataclass` in the `args.py` file which we later use to aprse our arguments.

The `config.py` mainly consists of some paths configurations and logging behavior. I am also writing logs into `.log` files but you can configure it according to your requriements. In case you wan tto write *logs*, create a `logs` folder first in the main directory.
## Training script
This is the `main` file of the project. FIrst of all, I am using <a href="https://albumentations.ai/">albimentations</a> to preprocess the data. Then I have some functions to create dataloaders.

After that we initialize clearML task. I am using clearML to track my experiments. Results will be shown at `app.clear.ml`.

Then we define our checkpoint and progress bar behavior. Initialize the `Trainer` and then fit the model.

## Test script
I am not including any test script here. That behavior depends on the pplication. Also I am planning to create some web apps using this baseline, so I will be wrtigin test scripts there. If I have time, I will include it here later.

# License
Feel free to use these baselines in your projects.
