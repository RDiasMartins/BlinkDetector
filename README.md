# SOFTWARE PARA AUXILIAR A COMUNICAÇÃO POR MEIO DO MOVIMENTO DAS PÁLPEBRAS.
## Projeto de iniciação ciêntifica realizado através da instituição IFSP - Câmpus Araraquara

### RESUMO:

  Em 2018, dados da Organização Mundial da Saúde (OMS) mostraram que um sétimo da população apresenta algum tipo de deficiência motora ou intelectual, resultando em mais de um bilhão de pessoas no mundo. Neste sentido, tecnologias assistivas vêm sendo desenvolvidas com o intuito de melhorar a qualidade de vida das pessoas que apresentam algum tipo de deficiência. Este trabalho visa integrar a ferramenta COSEM a um ambiente inteligente por meio de um módulo, a fim de dar autonomia de ações às pessoas que portam algum tipo de deficiência. 

### INTRODUÇÃO:

  Muitas vezes, portadores de algum tipo de deficiência são impossibilitados de realizar a execução de tarefas simples, como acender e apagar uma luz, ou, ligar e desligar um aparelho eletrônico. Este projeto visa automatizar de tarefas por meio do desenvolvimento de um módulo que permita que os usuários com dificuldade motora severa e de fala sejam capazes de interagir com um ambiente físico de forma autônoma por meio da integração com tecnologias voltadas para a Internet das Coisas (do inglês *Internet of Things* (IoT)). 
  Para que tal automatização seja possível, a ferramenta COSEM (KANEGAE; NUNES, 2020) será utilizada para que seja captado os movimentos das pálpebras do usuário, e a partir do processamento desses movimentos, este trabalho proverá uma interface de comunicação com o ambiente inteligente no qual o usuário está inserido permitindo assim a sua interação.

### FUNDAMENTAÇÃO TEÓRICA:

  A análise de dados e estatísticas mostram que em 2010, o contingente de pessoas que possuem algum tipo de deficiência foi de 45,77 milhões de pessoas, representando 23,9% da população Brasileira de acordo com o Instituto Brasileiro de Geografia e Estatística (IBGE, 2010). 
  Tecnologias assistivas têm sido desenvolvidas para melhorar a qualidade de vida das pessoas com deficiência e para expandir sua capacidade de interagir com o ambiente por meio do uso de computadores, sensores e atuadores (NUNES; MACHADO; MORAES, 2014). A IoT é considerada uma tecnologia assistiva, pois possibilita que as pessoas superem quase qualquer tipo de limitação física em tempo hábil (HOLLIER;ABOU-ZAHRA, 2018). Esse tipo de tecnologia visa auxiliar todos os tipos de deficiências como, por exemplo, um sistema de acionamento de uma cadeira de rodas utilizando um sistema embarcado equipado com um sensor acelerômetro, visando sua utilização como tecnologia assistiva para pessoas portadoras de necessidades especiais (BEHNCK, 2010). 
  Este trabalho visa complementar a ferramenta denominada COSEM, a qual é um protótipo funcional que permite a comunicação de pessoas com deficiência por meio dos olhos. Tal protótipo se baseia na sequência de piscadas emitidas pelos usuários, que são interpretadas e convertidas em ações. A finalidade de cada ação é Edição 2021 ISSN: 2526-6772 dinâmica e baseada em ações predefinidas pelo usuário na ferramenta (KANEGAE; NUNES, 2020). Assim, este trabalho visa estender as funcionalidades do protótipo COSEM para permitir que seus usuários possam atuar em ambientes inteligentes. 
  
 ### METODOLOGIA:
  A ferramenta COSEM é um protótipo de baixa fidelidade apresentada ao usuário como uma interface elaborada nas linguagens HTML, JAVASCRIPT e CSS. A integração entre a interface com o usuário e o processamento de imagens é realizada pelo framework FLASK (FLASK, 2020) juntamente com a biblioteca OpenCV (OPENCV, 2020) na linguagem python que recebe a imagem do usuário enviada através de uma webcam e converte as piscadas emitidas pelo movimento das pálpebras do usuário em ações predefinidas no sistema. Na Figura 1 é mostrada a ideia do funcionamento da sua interface gráfica.
  Neste sentido, a ferramenta COSEM servirá como um dispositivo de entrada, em que após a interpretação das piscadas do usuários esta enviará uma mensagem ao módulo desenvolvido neste trabalho. Ao receber a mensagem, o módulo será responsável por interpretá-la e realizar a ação necessária para interagir com o ambiente. 
 
![image](https://user-images.githubusercontent.com/60942670/159397979-0056dce2-909e-4c32-9960-d221810286a4.png)

  Para realizar a integração com o módulo desenvolvido, foi necessário realizar a refatoração do código da ferramenta COSEM a fim de torná-la orientada a objetos e viabilizar a implementação de outras tecnologias semelhantes. Com a aplicação do paradigma orientado a objetos, o software pode ser exemplificado por meio de três módulos.
  O primeiro módulo é responsável pela ferramenta que enviará a mensagem de entrada para processamento. O segundo é o módulo encarregado de interpretar e processar a ação predefinida pelo usuário no mesmo. E o último, é responsável pela emissão da mensagem de saída do sistema, sendo o primeiro e o terceiro módulos capazes de receberem outras ferramentas que auxiliarão diferentes tipos de deficiências motoras ou intelectuais como mostrado no exemplo da Figura 2.

![image](https://user-images.githubusercontent.com/60942670/159398023-3ba6b1bf-2fc4-426b-921c-684addf4e316.png)

  Para realizar a transmissão da mensagem do módulo para a assistente virtual foi preciso avaliar qual ferramenta se desenvolveria melhor no sistema como dispositivo de saída. A assistente utilizada para os testes foi a Alexa. Diante disso, inicialmente foi realizado uma revisão das ferramentas para desenvolvedor disponibilizados pela Amazon (AMAZON, [2020]), com o objetivo de planejar a integração do sistema com a Alexa de forma que a assistente virtual executasse a ação após receber o comando processado no módulo. Foi concluído que a integração ainda seria limitada se utilizadas apenas essas ferramentas, devido às limitações impostas pela mesma, então descartamos o uso, partindo assim para o desenvolvimento da aplicação em Python utilizando bibliotecas nativas.
  A integração da ferramenta COSEM com a assistente virtual Alexa foi realizada com base no estudo e aplicação da biblioteca Python pyttsx3 (BAHT, 2017). Com a utilização dela foi possível elaborar um sintetizador de voz que efetuasse a emissão do comando em som onde a assistente virtual fica responsável por reconhecer e executar a ação.
  
### RESULTADOS E DISCUSSÃO:
  Como resultado deste projeto até o momento, pode-se destacar o desenvolvimento de um protótipo funcional do sistema. Na Figura 3 é possível observar como ocorre o funcionamento do sistema, como mensagem de entrada o usuário emite as piscadas e o módulo do sistema processa e determina qual ação foi escolhida, ação essa estabelecida pelo usuário nos métodos do sistema, depois de processada, a informação é enviada a tecnologia aplicada como saída de mensagem que nesse caso é o sintetizador de voz para realização da comunicação com a assistente virtual, que executa a interação com o ambiente físico como acender ou apagar uma lâmpada, controlar remotamente uma televisão ou executar ações em um smartphone. 

![image](https://user-images.githubusercontent.com/60942670/159398123-bfa68ffd-fe0e-449e-a64c-bccbeda65435.png)


### CONCLUSÕES:
  Este trabalho apresentou um protótipo funcional de um software que permite a comunicação de pessoas com deficiências por meio do movimento das pálpebras com uma assistente virtual que realiza a execução de tarefas em um ambiente, como apagar ou acender as luzes. As tarefas que a assistente executará será definida pelo usuário no sistema, predefinindo assim os comandos que o sintetizador de voz emitirá. Os próximos passos deste trabalho serão compostos pela adequação do código de forma que viabilize o uso do sistema por múltiplos clientes, sem a necessidade da configuração de um servidor em uma máquina local e também da avaliação qualitativa e quantitativa desse sistema.

### Referências:

- [PDF Relatório final do projeto](https://arq.ifsp.edu.br/eventos/index.php/enict/6EnICT/paper/view/555)
- [AMAZON Developer Services. [S. l.]: Amazon, [201-?]](https://developer.amazon.com) Acesso em: 8 abr. 2021.
- [BAHT, Natesh. PYTTSX3. [S. l.], 2017.](https://pyttsx3.readthedocs.io/en/latest/) Acesso em: 4 jun. 2021
- [BEHNCK, Lucas Pluceno. Desenvolvimento de um sistema de acionamento para uma cadeira de rodas utilizando
acelerômetros para uso como tecnologia assistiva. [s. l.], 2010.](https://lume.ufrgs.br/handle/10183/46338) Acesso em: 18 set. 2021.
- [FLASK. Flask. Flask, 2020.](https://flask.palletsprojects.com/en/1.1.x/) Acesso em: 21 set. 2020.
- [KANEGAE, Yuri; NUNES, Luiz Henrique. Proposta de aplicação para auxiliar a comunicação por meio do
movimento de pálpebras. [s. l.], 2020.](https://arq.ifsp.edu.br/eventos/index.php/enict/5EnICT/paper/view/498) Acesso em: 17 set. 2021.
- [OPENCV. OpenCV. OpenCV, 2020.](https://opencv.org/): Acesso em: 21 set. 2020.
- [PYTHON do zero. Direção: Weuler Borges. [S. l.: s. n.], [2020].](https://programadorsagaz.com.br/python-do-zero/) Acesso em: 13 mar. 2021.

#### Agradecimentos:

- Prof. Dr. Luiz Henrique Nunes  - Docente na instituição IFSP Câmpus Araraquara 
- Yuri Kanegae - Discente formado na instituição IFSP Câmpus Araraquara 

