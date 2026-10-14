# convert photo to binary by file handiling
import matplotlib.pyplot as plt


photo = open("PYTHON\\python-w3-schools\\images.jpg", "rb")

binary_photo = photo.read()

print(binary_photo)

# binary to photo

with open("converted_image.jpg", "wb") as new_photo:
    new_photo.write(binary_photo)

plt.imshow(plt.imread("converted_image.jpg"))
plt.axis('off')  # Hide axes
plt.show()    



