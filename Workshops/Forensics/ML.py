from datetime import datetime, time
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, linear_model
import pandas as pd
import numpy as np 
import mnist
import logging
import logging.handlers
import sys
import os
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical

#logging environment
handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE","WORKSHOP2.log"))
format = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(format)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)



def readData():
    iris = datasets.load_iris()
    print(type(iris.data), type(iris.target))
    X = iris.data
    Y = iris.target
    df = pd.DataFrame(X, columns=iris.feature_names)
    print(df.head())

    #log details of the file and data types of dataframe
    logging.info(df.dtypes)
    logging.info(iris.__class__)


    return df 

def makePrediction():
    #see if dtaset was imported successfully
    try:
        iris = datasets.load_iris()
    except:
        logging.error(getTime() + " iris dataset not imported")

    knn = KNeighborsClassifier(n_neighbors=6)
    knn.fit(iris['data'], iris['target'])
    X = [
        [5.9, 1.0, 5.1, 1.8],
        [3.4, 2.0, 1.1, 4.8],
    ]
    prediction = knn.predict(X)
    print(prediction)

    #data and data types
    logging.info(iris.__sizeof__)
    logging.info(iris.__class__)

    #Log the algorithm type
    logging.info("type " + knn.algorithm)


def doRegression():
    #check if the dataset was imported
    try:
        diabetes = datasets.load_diabetes()
        logging.info(getTime() + " diabetes dataset loaded")
    except:
        logging.error(getTime + " diabetes dataset not imported")

    #diabetes = datasets.load_diabetes()
    diabetes_X = diabetes.data[:, np.newaxis, 2]
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]
    regr = linear_model.LinearRegression()
    regr.fit(diabetes_X_train, diabetes_y_train)
    
    logging.info(getTime() + str(regr._get_tags()))

    diabetes_y_pred = regr.predict(diabetes_X_test)

    #log source and data
    logging.info(diabetes.__class__)
    logging.info(diabetes.__len__)


def doDeepLearning():
    #log errors with imported data
    try:
        train_images = mnist.train_images()
        train_labels = mnist.train_labels()
        test_images = mnist.test_images()
        test_labels = mnist.test_labels()

        logging.info(getTime() + " mnist datasets loaded successfully")
    except:
        logging.error(getTime() + " mnist dataset failed to load")

    train_images = (train_images / 255) - 0.5
    test_images = (test_images / 255) - 0.5


    train_images = np.expand_dims(train_images, axis=3)
    test_images = np.expand_dims(test_images, axis=3)

    num_filters = 8
    filter_size = 3
    pool_size = 2

    model = Sequential([
    Conv2D(num_filters, filter_size, input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=pool_size),
    Flatten(),
    Dense(10, activation='softmax'),
    ])

    #log model status
    #logging.info(getTime() + " " + model.__class__)
    logging.info(getTime() + " compiling the model")
    # Compile the model.
    model.compile(
    'adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
    )

    logging.info(getTime() + "training the model")
    # Train the model.
    model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=3,
    validation_data=(test_images, to_categorical(test_labels)),
    )

    model.save_weights('cnn.h5')

    #
    logging.info(getTime() + " prediciton")
    predictions = model.predict(test_images[:5])

    print(np.argmax(predictions, axis=1)) # [7, 2, 1, 0, 4]

    print(test_labels[:5]) # [7, 2, 1, 0, 4]

def getTime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")

if __name__=='__main__': 
    #log program start, version of the system
    logging.info(getTime() + sys.version)
    logging.info(getTime() + " program started")
    #log if file not found
    try:
        data_frame = readData()
        logging.info(getTime() + " file loaded")
    except OSError as e:
        logging.critical("OS Error: {0}".format(e))
        
    #log beginning of knn prediction
    logging.info(getTime() + " Prediction")
    makePrediction() 

    #log start of linear regresssion
    logging.info(getTime() + " starting regression")
    doRegression()

    #log start of deep learning
    logging.info(getTime() + " starting deeplearning")
    doDeepLearning() 

    #end of program
    logging.info(getTime() + " end")