import cv2

print(f'number of CUDA GPU availiable {cv2.cuda.getCudaEnabledDeviceCount()}\n')
print(cv2.cuda.printCudaDeviceInfo(0))
