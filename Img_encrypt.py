from PIL import Image
import numpy as np

def swap_pixels(np_image):
    """Swap pixels in a simple pattern (e.g., swap every pair of pixels)"""
    height, width, channels = np_image.shape
    for i in range(height):
        for j in range(0, width - 1, 2):
            for c in range(channels):
                np_image[i, j, c], np_image[i, j + 1, c] = np_image[i, j + 1, c], np_image[i, j, c]
    return np_image

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    np_image = np.array(image)

    # Apply pixel swapping
    np_image = swap_pixels(np_image)
    
    # Apply encryption: Add key to each pixel value
    encrypted_image = (np_image + key) % 256  # Modulo 256 to wrap around pixel values

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_image.astype('uint8'))
    encrypted_image.save(output_path)

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    image = Image.open(image_path)
    image = image.convert("RGB")
    np_image = np.array(image)

    # Apply decryption: Subtract key from each pixel value
    decrypted_image = (np_image - key) % 256  # Modulo 256 to wrap around pixel values
    
    # Swap the pixels back to their original positions
    decrypted_image = swap_pixels(decrypted_image)

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_image.astype('uint8'))
    decrypted_image.save(output_path)

def main():
    print("Image Encryption Tool")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice!")
        return
    
    image_path = input("Enter the path to the image: ").strip('"')
    output_path = input("Enter the output path for the processed image: ").strip('"')
    key = int(input("Enter an integer key for encryption/decryption: "))

    if choice == 'e':
        encrypt_image(image_path, output_path, key)
        print(f"Image encrypted and saved to {output_path}")
    else:
        decrypt_image(image_path, output_path, key)
        print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    main()
