import os, glob, random

dataset_path = os.path.join('dataset')

def split_dataset(dataset_path):
    if 'test' not in os.listdir(dataset_path):
        os.makedirs(os.path.join(dataset_path,'test'))

    train_path = os.path.join(dataset_path,'train')
    test_path = os.path.join(dataset_path,'test')

    print(train_path)
    print(test_path)

    total_files = 0
    for folder in os.listdir(train_path):
        for file in os.listdir(os.path.join(train_path,folder)):
            total_files += 1

    train_files = int(total_files * 0.80)                   # training sample has to be 80% of total dataset
    test_files = total_files - train_files                  # validation/testing sample has to be 20%
    
    print(total_files)
    print('train files are supposed to be', train_files)
    print('test files are supposed to be', test_files)

    while test_files > 0:
        for folder in os.listdir(train_path):
            file = random.choice(os.path.join(train_path, folder))
            if os.path.isfile(os.path.join(train_path,folder,file)):
                print(file)
                os.rename(os.path.join(train_path,folder,file), os.path.join(test_path,file))
                test_files -= 1

    for folder in os.listdir(train_path):
        if len(os.listdir(os.path.join(train_path,folder))) == 0:
            print("Directory", os.path.join(train_path,folder), "will be deleted as it's empty")
            os.rmdir(os.path.join(train_path,folder))

    return train_path, test_path

split_dataset(dataset_path)