if __name__ == "__main__":
  try:
    import cv2
    print(cv2.__version__)
    text = open('cv2_info.txt', 'w')
    text.write(cv2.getBuildInformation())
    text.close()
  except ImportError as err:
    print('Cannot import cv2, make sure you install it')