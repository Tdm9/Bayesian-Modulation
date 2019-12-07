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

# CNN (Convulutional Neural Netowrks):
In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of deep neural networks, most commonly applied to analyzing visual imagery. They are also known as shift invariant or space invariant artificial neural networks (SIANN), based on their shared-weights architecture and translation invariance characteristics. They have applications in image and video recognition, recommender systems,[3] image classification, medical image analysis, and natural language processing.

# Bibliography:

-https://nordicapis.com/5-best-speech-to-text-apis/  
-https://machinelearningmastery.com/recurrent-neural-network-algorithms-for-deep-learning/  
-https://www.quora.com/Which-neural-network-type-is-best-for-speech-recognition-and-speech-synthesis  
-https://www.coursera.org/lecture/nlp-sequence-models/different-types-of-rnns-BO8PS  
-https://medium.com/towards-artificial-intelligence/introduction-to-the-architecture-of-recurrent-neural-networks-rnns-a277007984b7  
-https://medium.com/@datamonsters/artificial-neural-networks-for-natural-language-processing-part-1-64ca9ebfa3b2   
-https://towardsdatascience.com/beginners-guide-to-understanding-convolutional-neural-networks-ae9ed58bb17d  

# CNN (Convolutional Neural Networks) VS RNN(Recurrent neural networks)

In some cases like Image Recognition on which the set of input/output nodes are static basically on every time independent problem CNN is at most the optimal Neural Network option, with the introduction of time as variable RNN comes in handy.  Output for a given input is now not only based on the input at a given time, but also the inputs that came previously. 



# Redes de convolução: Introdução

Na área de redes neuronais, CNN (redes de convolução) são uma das principais categorias para análise e classificação de imagens, como tal o uso deste tipo de rede torna-se bastante reincidente quando o objetivo é detetar objetos, reconhecer individuos ou até ler textos manuscritos.
Na nossa abordagem ao reconhecimento de voz, iremos dissecar a utilidade desta rede quando o assunto de estudo se trata não de uma simples imagem de duas dimensões (alturaxlargura), mas sim de reconhecer uma voz, algo dependente de uma quantidade descomunal de variaveis.


# Convolução

Uma convolução é a primeira camada de acesso a dados, que extrai com base num input uma amostra.
Com essa amostra são depois extrapolados detalhes acerca do input aplicando um filtro/kernel.
Um kernel é uma matrix menor que a matrix de input, também denominada de matrix de convolução, cuja função é iterar a matriz de input
aplicando-lhe um produto.


![](convolucao.gif)

Quando o objetivo é extrair do output multiplas propriedades usamos vários kernels do mesmo tamanho, de modo a que o resultado destes filtros seja empilhavel.

![Processo de convolução com mais de um kernel](https://miro.medium.com/max/979/1*DmAwcMCcHqZdF62J0hNWlQ.png)

Numa última fase da convolução é aplicada á matrix filtrada uma função de activação (normalmente sendo esta uma função de ReLu ou de Tanh) com o intuito de deslinearizar o output. ![Processo completo de convolução](https://miro.medium.com/max/1146/1*u2el-HrqRPVk7x0xlvs_CA.png)


