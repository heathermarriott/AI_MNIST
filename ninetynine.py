#https://github.com/nusco/progml-code/tree/main/15_development

import neural_network_quieter as nn
import mnist_standardized as data

import drawNumbersAndPredict2
import numpy as np

w1, w2 = nn.train(data.X_train, data.Y_train, data.X_test, data.Y_test,
         n_hidden_nodes=1200, epochs=200, batch_size=600, lr=0.8)

seeMe = 0
print("doneTraining")
#for i in range(28):
#    print("".join(["*" if j > 0 else " " for j in data.X_train[0][i*28:i*28+28]])
def AI(inp):
    global seeMe
    inp2 = [[inp[j][i] for j in range(28)] for i in range(28)]
    npar = np.array(inp2)
    # Scale to match MNIST value range
    img = (npar * 255).astype(np.uint8)

    # Flatten to one row of 784 pixels
    img_flat = img.reshape(1, 784)

    # --- Proper MNIST standardization ---
    mnist_mean = np.average(data.X_train_raw)
    mnist_std  = np.std(data.X_train_raw)
    img_std = (img_flat - mnist_mean) / mnist_std
    # ------------------------------------

    seeMe = img_std
    #for i in range(28):
    #    print("".join(["*" if j > 0 else " " for j in seeMe[0][i*28:i*28+28]]))
    return nn.classify(img_std, w1, w2)
##    flat = npar.flatten()
##    tims = (flat * 255)
##    astype=(tims.astype(np.uint8))
##    resape=astype.reshape(1, 784)
##    inpReshaped,_ = data.standardize(resape,resape)
##    seeMe=inpReshaped
##    print(seeMe)
##    return nn.classify(inpReshaped, w1, w2)
drawNumbersAndPredict2.run(AI)
