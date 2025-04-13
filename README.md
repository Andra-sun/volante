
# 🕹️ Arduino + vJoy: Volante DIY para Euro Truck Simulator 2

Projeto utilizando Arduino Uno como controlador para simular um volante e botões no Euro Truck Simulator 2, via vJoy.

---

## 🧰 Componentes Utilizados

### Hardware

- Arduino Uno
    
- 1x Potenciômetro (para simular o volante)
    
- 3x Botões (acelerador, subir marcha e descer marcha)
    
- Fios de conexão
    

### Software

- [vJoy](https://sourceforge.net/projects/vjoystick/) (emulador de joystick)

- Python (script de integração entre Arduino e vJoy)

- Arduino IDE (para passar o códigoArduino pra o Arduino) 

---

## ⚙️ Instalação do vJoy

1. Baixe e instale o **vJoy**.
    
2. Abra o configurador do vJoy.
    
3. No _Device 1_, configure assim:
    
    - **Axes**: Marque `X` e `Y`
        
    - **Number of Buttons**: `8`
        
    - **POVs**: Selecione `Continuous` e `0`
        
    - Clique em **Apply**
        
4. Marque a opção **Enable vJoy**
    

---

## 🚀 Rodando o Projeto

1. Monte o circuito com o Arduino e os componentes listados.
    
2. Conecte o Arduino ao PC.
    
3. Execute o script Python responsável por enviar os dados do Arduino para o vJoy.
    
4. Abra o **Euro Truck Simulator 2** e siga os passos:
    
    ### Configuração no Jogo
    
    - Vá até as opções de **Controles**
        
    - Selecione: `Teclado + vJoy Device`
        
    - Role até a opção de **Volante**, clique nela e gire o potenciômetro → ele deve ser reconhecido como **eixo X**
        
    - Para o **acelerador**, pressione o botão 2 → ele será mapeado como **eixo Y**
        
    - Vá até a aba de **Teclas**
        
        - Substitua o comando de **Subir Marcha** pressionando o botão 3
            
        - Faça o mesmo para **Descer Marcha** com o botão restante
            

---

## 📦 Observações

- Certifique-se de que o script Python esteja com a porta correta da sua placa Arduino.
    
- O vJoy deve estar ativo sempre que for usar o projeto.
    

---
