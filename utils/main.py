import uuid

file = open("data.txt", "w")

for i in range(10):
    file.write("{}\n".format(uuid.uuid4()))

file.close()