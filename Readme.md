# PyStray Test

Este é um simples exemplo de aplicação Python usando a biblioteca PyStray, que cria um ícone na bandeja do sistema (system tray) exibindo a temperatura. A temperatura é obtida de uma URL remota (`http://starts.sytes.net:7890/get_temp_now`) e é atualizada periodicamente.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o código:

```bash
pip install pystray pillow requests
```

## Uso

1. Clone este repositório:

   ```bash
   git clone git@github.com:samuelprogramer/temperatura-win.git
   ```

2. Navegue até o diretório do código:

   ```bash
   cd temperatura-win
   ```

3. Execute o script Python:

   ```bash
   python index.py
   ```

   Isso iniciará o aplicativo na bandeja do sistema, e você verá um ícone que exibe a temperatura.

4. Clique com o botão direito no ícone para abrir o menu de contexto, onde você pode escolher "Atualizar" para obter a última temperatura ou "Sair" para fechar o aplicativo.

## Personalização

Se desejar personalizar a fonte utilizada no ícone, altere a linha que define a fonte em `make_number_icon` no script:

```python
fnt = ImageFont.truetype("arial.ttf", 55)
```

Substitua `"arial.ttf"` pelo caminho da fonte desejada no seu sistema.

Esse é um exemplo básico, e você pode estendê-lo conforme necessário para atender aos seus requisitos específicos.

![temp](temp-win.png)


## Compilar ao app

```
pip install pyinstaller
```

```
pyinstaller --onefile index.py
```



