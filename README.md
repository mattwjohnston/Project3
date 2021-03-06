### Malware Detection Machine Learning Project

Built two models, one random forest and two neural networks with the same purpose, to weigh different factors of computer builds to determine its vulnerability to a virus attack.

  *Original data was sourced from Kaggle on this page: https://www.kaggle.com/c/microsoft-malware-prediction/data . 
  *Data has over 9 million entries, each representing a computer, in the form of a .csv .  
  *Source of data is Microsoft, and all machines are running different versions of Windows.  
  *Data was released to the public as part of a contest.   
  *Winner constructed a model with 67% rate of accuracy.  
  *my top neural network accuracy was 63%, uses tanh activation and a lbfgs solver .  
  *Other data were regroup and reclassified to make the models run more efficiently and to make categorical data.   
  *Tried Keras and SkLearn to construct deep learning module    
  *Used Keras model .  
  *Neural network was constructed to have 3 layers comprised of a total of 8 neurons.   
  *Under these conditions the model was able to predict the likelihood of vulnerability with a 60% accuracy value.   
  *Broke down 1% of data, about 89k rows.  
  *Used OneHotEncoder, resulted in 6K columns .   
  *Ran grid search on min sample leaves .  
  *With 192 variations, 3 runs .  
  *Took over 24 hours to run .  
  *Reduced to 2 min leaves .   
