import numpy as np
import cv2
import matplotlib.pyplot as plt

# Convolution function to apply the filter to the image
def convolution(image, kernel, verbose=False):
    image_h, image_w = image.shape
    kernel_h, kernel_w = kernel.shape

    pad_h = kernel_h // 2
    pad_w = kernel_w // 2

    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

    output = np.zeros_like(image, dtype=float)

    for i in range(image_h):
        for j in range(image_w):
            region = padded_image[i:i + kernel_h, j:j + kernel_w]  # Extract the region of interest
            output[i, j] = np.sum(region * kernel)  # Apply the kernel to the region

    return output

def sobel_edge_detection(image, filter, verbose=False):
    # Apply Sobel filter for the x direction
    new_image_x = convolution(image, filter, verbose)

    if verbose:
        plt.imshow(new_image_x, cmap='gray')
        plt.title("Horizontal Edge")
        plt.show()

    # Apply Sobel filter for the y direction
    new_image_y = convolution(image, np.flip(filter.T, axis=0), verbose)

    if verbose:
        plt.imshow(new_image_y, cmap='gray')
        plt.title("Vertical Edge")
        plt.show()

    # Calculate the gradient magnitude
    gradient_magnitude = np.sqrt(np.square(new_image_x) + np.square(new_image_y))

    # Normalize to the range [0, 255]
    gradient_magnitude *= 255.0 / gradient_magnitude.max()

    if verbose:
        plt.imshow(gradient_magnitude, cmap='gray')
        plt.title("Gradient Magnitude")
        plt.show()

    return gradient_magnitude

def main():
    image_path = 'img.webp'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)



    sobel_filter = np.array([[-1, 0, 1],
                             [-2, 0, 2],
                             [-1, 0, 1]])

    edge_image = sobel_edge_detection(image, sobel_filter, verbose=True)

    plt.imshow(edge_image, cmap='gray')
    plt.title("Sobel Edge Detection Result")
    plt.axis('off')
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()
