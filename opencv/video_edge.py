import cv2
import argparse

parser = argparse.ArgumentParser(
    description='display canny of video'
    )
parser.add_argument(
    '--input', '-i', help='path to video',
    type=str, required=True
    )
args = vars(parser.parse_args())

def vid_canny(video_path):
  capture = cv2.VideoCapture(video_path)
  if capture.isOpened is False:
    print('cant open video')
  while capture.isOpened():
    ret, img = capture.read()
    if ret is not True:
      break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 200, 400)
    cv2.imshow('edged', canny)
    if cv2.waitKey(1) == ord('q'):
      break
    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
  vid_canny(args['input'])
