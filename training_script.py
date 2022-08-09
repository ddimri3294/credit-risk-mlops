import argparse
import os
import json


# Define main training function
def main():
    with open('/opt/ml/input/config/hyperparameters.json', 'r') as json_file:
        hyperparameters = json.load(json_file)
        print(hyperparameters)

    with open('/opt/ml/input/config/inputdataconfig.json', 'r') as json_file:
        inputdataconfig = json.load(json_file)
    print(inputdataconfig)

    with open('/opt/ml/input/config/resourceconfig.json', 'r') as json_file:
        resourceconfig = json.load(json_file)
    print(resourceconfig)

if __name__ == '__main__':
    main()


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#
#     # hyperparameters sent by the client are passed as command-line arguments to the script.
#     parser.add_argument('--epochs', type=int, default=10)
#     parser.add_argument('--batch-size', type=int, default=100)
#     parser.add_argument('--learning-rate', type=float, default=0.1)
#
#     # an alternative way to load hyperparameters via SM_HPS environment variable.
#     parser.add_argument('--sm-hps', type=json.loads, default=os.environ['SM_HPS'])
#
#     # input data and model directories
#     parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
#     parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAINING'])
#     parser.add_argument('--test', type=str, default=os.environ['SM_CHANNEL_TESTING'])
#
#     args = parser.parse_args()
#
#     training_data_path = os.path.join(args.train, "housing.csv")
#     testing_data_path = os.path.join(args.test, "housing.csv")
#
#     # using it as variable
#     model_dir = os.environ['SM_MODEL_DIR']
#
#     print(training_data_path)
#     print(testing_data_path)
#     print(model_dir)
