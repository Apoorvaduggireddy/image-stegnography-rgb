import cv2
import os
import hashlib

# Specify the path to the encrypted image
encrypted_image_path = r"C:\Users\91938\Downloads\encryptedImage.jpg"

# Read the encrypted image
img = cv2.imread(encrypted_image_path)

# Check if the image is successfully loaded
if img is None:
    print("Image not found. Check the file path and make sure the image exists.")
    exit()

# Get the dimensions of the image
height, width, channels = img.shape

# Prompt the user to input the password
password = input("Enter the passcode: ")

# Hash the password using SHA-256
hash_object = hashlib.sha256(password.encode())  # Corrected from sha255 to sha256
hashed_password = hash_object.digest()

# Initialize dictionaries for mapping ASCII values to characters
c = {}
for i in range(256):
    c[i] = chr(i)  # ASCII to character

# Initialize variables for image coordinates and color channel
n = 0  # Row index
m = 0  # Column index
z = 0  # Color channel index

# Initialize an empty list to store the decrypted message characters
decrypted_message = []

# Decrypt the message from the image
while True:
    # Retrieve the encoded value from the image
    encoded_value = img[n, m, z]
    
    # Calculate the original ASCII value
    original_value = (encoded_value - hashed_password[len(decrypted_message) % len(hashed_password)]) % 256
    
    # Ensure original_value stays within 0-255 range
    if original_value < 0:
        original_value += 256
    
    # Append the corresponding character to the decrypted message
    decrypted_message.append(c[original_value])
    
    # Move to the next pixel
    m += 1
    
    # If the column index exceeds the image width, reset it and move to the next row
    if m >= width:
        m = 0
        n += 1
    
    # If the row index exceeds the image height, stop decoding (reached end of image)
    if n >= height:
        break
    
    # Cycle through the color channels (0, 1, 2) for RGB
    z = (z + 1) % 3

# Convert the list of characters into a string
decrypted_message = ''.join(decrypted_message)

print("Decrypted Message:", decrypted_message)
