## 01 - WheresWally

### Objetivo
Encontrar o Wally automaticamente em imagens e calcular o centróide dele

### Solução usada
Transfer learning - retreinar o modelo [Mask R-CNN Inception](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) para detectar o wally nas imagens

### Limitações
O modelo escolhido marcava a box envolta do wally apenas na horizontal, então os centróides acabam tendo um pequeno desvio de lugar
<br>Exemplo:

<p align="center">
  <img src="Images Predicted with Centroid/wally_109.jpg" width="300" height="400"/>
</p>

### Respostas
- [Imagens com wallys detectados e centróides marcados](https://github.com/AlfredoFilho/nuveo-teste-ia/tree/main/01%20-%20WheresWally/Images%20Predicted%20with%20Centroid)
- [CSV de entrega com centróides](wheres_wally_train.csv)

## Arquivos do retreino
Código usado para retreino do modelo: [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-nDvp6VEyX1-s4ReSluXsUQE23oRKGsD?usp=sharing)

Ou o Jupyter Notebook: [Google Colab - Train_Model_Spam.ipynb](https://github.com/AlfredoFilho/nuveo-teste-ia/blob/main/01%20-%20WheresWally/Google%20Colab%20-%20Training_and_Detection_Wally.ipynb)
