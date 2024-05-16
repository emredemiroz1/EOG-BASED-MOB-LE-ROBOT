import os
import kaggle

# Kaggle API kimlik bilgileri dosyasının yolu
os.environ['KAGGLE_CONFIG_DIR'] = 'C:\\Users\\emred\\.kaggle'

# Datasetin adı
dataset_name = "keras/gemma/keras/gemma_1.1_instruct_2b_en"

# Dataseti indir
kaggle.api.dataset_download_files(dataset_name, unzip=True)

print("Model dosyalarının yolu:", dataset_name)
