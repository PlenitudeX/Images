# Pythono3 code to rename multiple files with fix names
# files in a directory or folder

# importing os module
import os, csv, re

# nome da pasta a ser varrida 
folder = 'simple_images'

# arquivo CSV a ser gerado e importado no Magento.
productsImagesFolder = open('importImagesFolderProducts.csv', 'w', newline='')
outputWriter = csv.writer(productsImagesFolder,)
header = ["sku", "base_image", "small_image", "thumbnail_image", "additional_images"]
outputWriter.writerow(header)

productsCarajasData = {}
productsCarajasData['sku'] = ''
productsCarajasData['files'] = []

for count, subfolder in enumerate(os.listdir(folder)):
    print(subfolder)
    if os.path.isdir(f"{folder}/{subfolder}") == True:
        images = list()
        for count1, filename in enumerate(os.listdir(f"{folder}/{subfolder}")):
            if os.path.isdir(f"{folder}/{subfolder}/{filename}") == False:
                dst = re.sub(r'\(|\)|\\|\+|\s|\"|\-|\%|\'|\&|\:', '_', filename)
                dst = dst.replace('ç', 'c')
                dst = dst.replace('ã', 'a')
                dst = dst.replace('é', 'e')
                dst = dst.replace('ú', 'u')
                dst = dst.replace('â', 'a') #789604208850
                dst = dst.replace('°', '') #789822665003
                dst = dst.replace('º', '')
                dst = dst.replace('D+', 'Dmais')
                dst = dst.replace('__', '_')
                dst = dst.replace('õ', 'o')
                images.append(dst)
                src =f"{folder}/{subfolder}/{filename}"
                dst =f"{folder}/{subfolder}/{dst}"
                os.rename(src, dst)
        productsCarajasData[subfolder] = images
        sku = subfolder
        base_image = subfolder+'/'+productsCarajasData[subfolder][0]
        small_image  = ''
        thumbnail_image = subfolder+'/'+productsCarajasData[subfolder][0]
        additional_images = subfolder+'/'+productsCarajasData[subfolder][1]
        outputWriter.writerow ([sku, base_image, small_image, thumbnail_image, additional_images])
productsImagesFolder.close()
