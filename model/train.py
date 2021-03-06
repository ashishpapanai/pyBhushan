import keras
from keras.callbacks import TensorBoard, ReduceLROnPlateau
from numpy.core.numeric import False_
import preprocessing
import models, checkTraining

class Training():
    def __init__(self, ticker):
        self.preprocessing = preprocessing.data_preprocessing(ticker)
        self.models = models.Models(ticker)
        self.learning_rate_reduction = ReduceLROnPlateau(monitor='val_loss',
                                            patience=25,
                                            verbose=1,
                                            factor=0.25,
                                            min_lr=0.00001)
        self.tensorboard = keras.callbacks.TensorBoard(
                                                        log_dir='TensorBoard_Logs',
                                                        histogram_freq=1,
                                                        embeddings_freq=1
                                                    )  
        #self.lstm_history, self.mix_history = self.train_model()
        self.models.lstm_model.save_weights("model/lstm_weights.h5")
        self.models.mix_lstm_model.save_weights("model/mix_lstm_weights.h5")
        self.y_pred_train_lstm = self.models.lstm_model.predict(self.preprocessing.X_train)
        self.y_pred_train_mix = self.models.mix_lstm_model.predict(self.preprocessing.X_train)
        self.y_pred_lstm = self.models.lstm_model.predict(self.preprocessing.X_test)
        self.y_pred_mix = self.models.mix_lstm_model.predict(self.preprocessing.X_test)

    def train_model(self):
        lstm_history = self.models.lstm_model.fit(self.preprocessing.X_train, self.preprocessing.y_train, epochs=400, batch_size=48, validation_data=(self.preprocessing.X_test, self.preprocessing.y_test),
                              verbose=1, callbacks=[self.learning_rate_reduction, self.tensorboard], shuffle=False)

        mix_history = self.models.mix_lstm_model.fit(self.preprocessing.X_train, self.preprocessing.y_train, epochs=400, batch_size=48, validation_data=(self.preprocessing.X_test, self.preprocessing.y_test),
                                 verbose=1, callbacks=[self.learning_rate_reduction, self.tensorboard], shuffle=False)
        return lstm_history, mix_history

