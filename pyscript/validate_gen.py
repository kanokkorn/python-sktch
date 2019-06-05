import glob, os

current_dir = os.path.dirname(os.path.abspath(__file__))

current_dir = "./img"

percentage = 15

train_file = open("train.txt", "w")
test_file = open("test.txt", "w")

counter = 1
index = round(100 / percentage)
for _path_ in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(_path_))
    if counter == index:
        test_file.write(current_dir + "/" + title + ".jpg" + "\n")
    else:
        train_file.write(current_dir + "/" + title + ".jpg" + "\n")
        counter += 1
