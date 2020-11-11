import matplotlib.pyplot as plt
plt.figure(figsize=(4,4))
face = plt.imread('raccoon1.jpeg')
print(type(face))
print(face.shape, face.dtype)
plt.imshow(face[:950,:950,0],cmap='gray')
plt.show()


#import matplotlib.pyplot as plt
# plt.figure(figsize=(5,5))
# face = plt.imread('raccoon1.jpeg')
# print(face.shape)
# print(face.dtype)
# plt.imshow(face[:900, :900, :])
# plt.show()





