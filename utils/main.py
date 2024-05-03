import uuid

file = open("data.txt", "w")

for i in range(100000):
    file.write("{}\n".format(uuid.uuid4()))

file.close()