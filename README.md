# Todays Speech Recognition Example:  
-Cortana: Windows assistant  
-Siri:    Apple's assistant and apple homepod assistant  
-Google Assistant: Android assistant and Google Home assistant  
-Alexa    Amazon home assistant  


# Common Neural Networks:  
Multilayer perceptron (MLP)  
Convolutional neural network (CNN)  
Recursive neural network (RNN)  
Recurrent neural network (RNN)  
Long short-term memory (LSTM)  
Sequence-to-sequence models  
Shallow neural networks
  
  
#  Deep Speech:  
-Uses a well-optimized RNN training system  
-Does not require phoneme dictionary,  
-Employes multiple GPU's to process thousands of hours of data,  
  


# RNN(Recurrent neural networks):
Add additional weights to the network to create cycles in the network graph in an effort to maintain an internal state
By adding state to a neural network we will be able to explicitly learn and exploit context in sequence prediction problems,
like humans who can recognize something as they move towards that same thing, machines will also be able to recognize and make predictions base on movement and temporal data.  
In our Case of study the RNN is used to convert input sequences into a sequence of character probabilities for the transcription.

# Bibliography:

-https://nordicapis.com/5-best-speech-to-text-apis/  
-https://machinelearningmastery.com/recurrent-neural-network-algorithms-for-deep-learning/  
-https://www.quora.com/Which-neural-network-type-is-best-for-speech-recognition-and-speech-synthesis  
-https://www.coursera.org/lecture/nlp-sequence-models/different-types-of-rnns-BO8PS  
-https://medium.com/towards-artificial-intelligence/introduction-to-the-architecture-of-recurrent-neural-networks-rnns-a277007984b7  
-https://medium.com/@datamonsters/artificial-neural-networks-for-natural-language-processing-part-1-64ca9ebfa3b2  

# CNN (Convolutional Neural Networks) VS RNN(Recurrent neural networks)

In some cases like Image Recognition on which the set of input/output nodes are static basically on every time independent problem CNN is at most the optimal Neural Network option, with the introduction of time as variable RNN comes in handy.  Output for a given input is now not only based on the input at a given time, but also the inputs that came previously. 
