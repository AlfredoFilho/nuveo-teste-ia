import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

class SpamDetector:
    def __init__(self):

        self.s_model = self.__load_model()
        self.tokenizer = self.__load_tokenizer()

   
    def __load_model(self):
        '''Import model.'''
        s_model = tf.keras.models.load_model("Model/spam_model")
        return s_model
    
       
    def __load_tokenizer(self):
        '''Import tokenizer.'''
        with open('Model/spam_model/tokenizer.pkl', 'rb') as input:
            tokenizer = pickle.load(input)
        return tokenizer


    def __predictSpam(self, sms):
        """Predict function
            - Convert text into numbers
            - Apply padding to keep the maximum numbers (10) that were used to create the model

        Parameters:
        sms (string): Sms message for prediction

        Returns:
        Float:Returns a number between 0 and 1 to be spam

        """
        sms_proc = self.tokenizer.texts_to_sequences([sms])
        sms_proc = pad_sequences(sms_proc, maxlen=10, padding='post')
        pred = (self.s_model.predict(sms_proc)).item()
        return pred


    def prob_spam(self, sms):
        """Spam probability function

        Parameters:
        sms (string): Sms message

        Returns:
        Float:Returns a number between 0 and 1 formatted without scientific notation

        """
        pred = self.__predictSpam(str(sms))
        if int(pred) == 1:
            return "1"
        else:
            return '{:.20f}'.format(pred)


    def is_spam(self, sms):
        """Returns a bool if it's spam

        Parameters:
        sms (string): Sms message

        Returns:
        Bool:Returns True if the message is spam and False if not.

        """
        pred = self.__predictSpam(str(sms))
        if pred > 0.5:
            return True

        else:
            return False