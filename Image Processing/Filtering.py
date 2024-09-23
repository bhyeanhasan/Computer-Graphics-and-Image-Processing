import time
from os import times
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

kernelSize = 3

def padding(img, kernelSize):
    w = kernelSize // 2
    fetchFirstRows = img[0: w, :]
    fetchLastRows = img[-w:, :]

    imgPadded = img.copy()
    imgPadded = np.insert(imgPadded, 0, fetchLastRows, axis=0)
    imgPadded = np.append(imgPadded, fetchFirstRows, axis=0)

    fetchFirstCols = imgPadded[:, 0: w]
    fetchLastCols = imgPadded[:, -w:]
    imgPadded = np.concatenate([fetchLastCols, imgPadded], axis=1)
    imgPadded = np.append(imgPadded, fetchFirstCols, axis=1)
    return imgPadded

def meanFilter(originalImg, imgPadded, kernelSize: int):
    filteredImage = np.zeros(originalImg.shape, dtype=np.int32)
    image_h, image_w = originalImg.shape[0], originalImg.shape[1]
    w = kernelSize // 2

    for i in range(w, image_h - w):
        for j in range(w, image_w - w):
            total = [0, 0, 0]
            for m in range(kernelSize):
                for n in range(kernelSize):
                    total += imgPadded[i - w + m][j - w + n]
            filteredImage[i - w][j - w] = total // (kernelSize * kernelSize)
    return filteredImage.astype(np.uint8)

def medianFilter(originalImg, imgPadded, kernelSize: int):
    filteredImage = np.zeros(originalImg.shape, dtype=np.int32)
    image_h, image_w = originalImg.shape[0], originalImg.shape[1]
    w = kernelSize // 2

    for i in range(w, image_h - w):
        for j in range(w, image_w - w):
            overlapImg = imgPadded[i - w: i + w + 1, j - w: j + w + 1]
            filteredImage[i][j] = np.median(overlapImg.reshape(-1, 3), axis=0)

    return filteredImage.astype(np.uint8)

def midPointFilter(originalImg, imgPadded, kernelSize: int):
    filteredImage = np.zeros(originalImg.shape, dtype=np.int32)
    image_h, image_w = originalImg.shape[0], originalImg.shape[1]
    w = kernelSize // 2

    for i in range(w, image_h - w):
        for j in range(w, image_w - w):
            overlapImg = imgPadded[i - w: i + w + 1, j - w: j + w + 1]
            overlapImg = overlapImg.astype('int32')
            maxVal = np.max(overlapImg.reshape(-1, 3), axis=0)
            minVal = np.min(overlapImg.reshape(-1, 3), axis=0)
            filteredImage[i][j] = np.add(maxVal, minVal) // 2

    return filteredImage.astype(np.uint8)

def main():
    originalImg = cv2.imread('img.webp')
    originalImg = cv2.cvtColor(originalImg, cv2.COLOR_BGR2RGB)

    imgPadded = padding(originalImg, kernelSize)

    mean_filtered = meanFilter(originalImg, imgPadded, kernelSize)
    median_filtered = medianFilter(originalImg, imgPadded, kernelSize)
    midpoint_filtered = midPointFilter(originalImg, imgPadded, kernelSize)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(originalImg)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(mean_filtered)
    plt.title('Mean Filter')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(median_filtered)
    plt.title('Median Filter')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(midpoint_filtered)
    plt.title('Midpoint Filter')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()
