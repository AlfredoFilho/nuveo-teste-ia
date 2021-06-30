## 02 - SMS Spam Detection

### Preparar ambiente

**1.** Clone do repositório
```bash
git clone https://github.com/AlfredoFilho/teste-ia-Private && cd "teste-ia-Private/02 - SMSSpamDetection"
```

**2.** Criar e ativar um ambiente: (Pulável se preferir instalar na máquina)
```bash
python3 -m venv env && source env/bin/activate
```

**3.** Instalar dependências:
```bash
pip3 install -r requirements.txt
```
<hr>

### Como usar
```python
import spamdetection as sp

SpamDetect = sp.SpamDetector()
stringSms = "Hello whats your name"

prob = SpamDetect.prob_spam(stringSms)
is_spam = SpamDetect.is_spam(stringSms)
```
**Nota**:
O arquivo python precisa estar na pasta `02 - SMSSpamDetection`, caso crie em outro diretório, precisará mudar o import da primeira linha
<br><br>Há um [arquivo de exemplo](https://github.com/AlfredoFilho/nuveo-teste-ia/blob/main/02%20-%20SMSSpamDetection/ExampleOfUse.py) no diretório, para testá-lo:
```bash
python3 ExampleOfUse.py
```
<hr>

### Testes
Para rodar os testes
```bash
python3 test_spamdetection.py
```

## Arquivos de treino
Código usado para treino do modelo: [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/130poRnYzaHV1JJId7acQZ15F_qBAYBTY?usp=sharing)

Ou o Jupyter Notebook: [Google Colab - Train_Model_Spam.ipynb](https://github.com/AlfredoFilho/nuveo-teste-ia/blob/main/02%20-%20SMSSpamDetection/Google%20Colab%20-%20Train_Model_Spam.ipynb)
