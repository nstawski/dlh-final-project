import os

base_path = 'C:\\Nina\\e-root\\data'

#-------------------------------------------
# image_paths = {
#     'MIMIC': r'/Volumes/Passport-2TB 2/data/mimic/physionet.org/files/mimic-cxr-jpg/2.0.0/files', # MIMIC-CXR
#     'CXP': '/Users/noemi/ood-generalization/data/CheXpert', # CheXpert
#     'NIH': '/Users/noemi/ood-generalization/data/chestxray8', # ChestX-ray8
#     'PAD': '/Users/noemi/ood-generalization/data/PadChest/images-224', # PadChest
# }

# meta_paths = {
#     'MIMIC': r'/Volumes/Passport-2TB 2/data/mimic/physionet.org/files/mimic-cxr-jpg/2.0.0', # MIMIC-CXR
#     'CXP': '/Users/noemi/ood-generalization/data/CheXpert', # CheXpert
#     'NIH': '/Users/noemi/ood-generalization/data/chestxray8', # ChestX-ray8
#     'PAD': '/Users/noemi/ood-generalization/data/PadChest', # PadChest
# }

# cache_dir = '/Users/noemi/ood-generalization/data/cache'


image_paths = {
    'MIMIC': 'C:\\Nina\\e-root\\data\\mimic\\physionet.org\\files\\mimic-cxr-jpg\\2.0.0\\files', # MIMIC-CXR
    'CXP': 'C:\\Nina\\e-root\\data\\CheXpert', # CheXpert
    'NIH': 'C:\\Nina\\e-root\\data\\chestxray8', # ChestX-ray8
    'PAD': 'C:\\Nina\\e-root\\data\\PadChest\\images-224', # PadChest
}

meta_paths = {
    'MIMIC': 'C:\\Nina\\e-root\\data\\mimic\\physionet.org\\files\\mimic-cxr-jpg\\2.0.0', # MIMIC-CXR
    'CXP': 'C:\\Nina\\e-root\\data\\CheXpert', # CheXpert
    'NIH': 'C:\\Nina\\e-root\\data\\chestxray8', # ChestX-ray8
    'PAD': 'C:\\Nina\\e-root\\data\\PadChest', # PadChest
}

cache_dir = 'C:\\Nina\\e-root\\data\\cache'
#-------------------------------------------

df_paths = {
    dataset: os.path.join(meta_paths[dataset], 'clinicaldg', f'preprocessed.csv')
    for dataset in meta_paths 
}

take_labels = ['No Finding', 'Atelectasis', 'Cardiomegaly',  'Effusion',  'Pneumonia', 'Pneumothorax', 'Consolidation','Edema' ]

IMAGENET_MEAN = [0.485, 0.456, 0.406]         # Mean of ImageNet dataset (used for normalization)
IMAGENET_STD = [0.229, 0.224, 0.225]          # Std of ImageNet dataset (used for normalization)

LABEL_SHIFTS = [0.1, 0.2, 0.5, 0.8, 0.9]
NURD_RATIOS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

HOSPITALS = ['CXP', 'MIMIC', 'NIH', 'PAD']
NUM_HOSPITALS = len(HOSPITALS)