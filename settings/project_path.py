import os

PROJECT_PATH = './'

MODELS_PATH = os.path.join(PROJECT_PATH, 'models')
MODEL_PATH = os.path.join(MODELS_PATH, 'cats_and_dogs.h5')

DATA_PATH = os.path.join(PROJECT_PATH, 'data')
ORIGINAL_DATASET_DIR = os.path.join(DATA_PATH, 'kaggle_original_data')
BASE_DIR = os.path.join(DATA_PATH, 'cats_and_dogs')

TRAIN_DIR = os.path.join(BASE_DIR, 'train')
VALIDATION_DIR = os.path.join(BASE_DIR, 'validation')
TEST_DIR = os.path.join(BASE_DIR, 'test')

TRAIN_CATS_DIR = os.path.join(TRAIN_DIR, 'cats')
TRAIN_DOGS_DIR = os.path.join(TRAIN_DIR, 'dogs')
VALIDATION_CATS_DIR = os.path.join(VALIDATION_DIR, 'cats')
VALIDATION_DOGS_DIR = os.path.join(VALIDATION_DIR, 'dogs')
TEST_CATS_DIR = os.path.join(TEST_DIR, 'cats')
TEST_DOGS_DIR = os.path.join(TEST_DIR, 'dogs')


PREDICT_DIR = os.path.join(PROJECT_PATH, 'test')
PREDICTED_DIR = os.path.join(PROJECT_PATH, 'predicted')

CATS_DIR = os.path.join(PREDICTED_DIR, 'cats')
DOGS_DIR = os.path.join(PREDICTED_DIR, 'dogs')
