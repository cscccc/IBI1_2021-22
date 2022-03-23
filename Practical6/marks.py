import numpy as np
import matplotlib.pyplot as plt
scores = [45,36,86,57,53,92,65,45]
print ("Rob’s marks across the semester are ",sorted(scores))
plt.boxplot(scores,labels=["Rob"],patch_artist = True)
plt.title("IBI scores")
plt.ylabel('scores')
plt.show()

avg = sum(scores)/len(scores)
print("The average mark Rob has received across the eight practicals is ",avg)

if avg>=60:
    print("Rob has passed")
else:
    print("Rob has failed")
