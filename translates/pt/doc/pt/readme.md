# Manual do utilizador: Tradutor Avançado para NVDA

<h2 id="index">Índice</h2>

- [1 - Introdução](#introdução)
  - [1.1 - Requisitos](#requisitos)
  - [1.2 - Limitações e avisos](#limitações-e-avisos)
  - [1.3 - Informações do autor](#autor-informações)
- [2 - Descrição e configuração](#description-configuration)
  - [2.1 - Descrição do serviço](#service-description)
    - [Google](#google)
    - [DeepL](#deepl)
    - [LibreTranslate](#libretranslate)
    - [Microsoft Traduzir](#microsoft-translate)
  - [2.2 - Configuração](#configuração)
    - [Menu de extras](#menu-extra)
    - [Teclas de atalho do extra](#teclas de atalho do extra)
- [3 - Solução de problemas](#solução de problemas)
  - [Problemas e soluções comuns](#problemas e soluções comuns)
  - [Como consultar o log do NVDA](#how-to-consult-the-nvda-log)
- [4 - Agradecimentos](#agradecimentos)
  - [Tradutores](#tradutores)
- [5 - Registo de versão](#registo de versão)
  - [Versão 1.0](#versão-1-0)

<h2 id="introdução">1 - Introdução</h2>

**O  Advanced Translator for NVDA** é um extra que permite traduzir textos usando diversos serviços de tradução online, como Google Translate, DeepL, LibreTranslate e Microsoft Translator. Este extra oferece funcionalidades avançadas como tradução simultânea, histórico de tradução, tradução do selecionado, suporte para vários idiomas e muito mais.

[Voltar ao índice](#índice)

<h3 id="requirements">1.1 - Requisitos</h3>

- NVDA (NonVisual Desktop Access) 2024.1 ou superior
- Conexão com a internet

[Voltar ao índice](#índice)

<h3 id="limitations-and-warnings">1.2 - Limitações e avisos</h3>

O extra envia informações pela Internet para cada serviço correspondente para realizar a tradução simultânea. É importante observar que as informações traduzidas podem incluir dados confidenciais e sensíveis. A utilização do extra é de responsabilidade exclusiva dos utilizadores, que deverá avaliar a natureza das informações enviadas. O desenvolvedor do extra não se responsabiliza pelos dados enviados aos serviços que o extra utiliza.

Como desenvolvedor, declino qualquer responsabilidade por qualquer eventualidade que possa surgir com o uso do extra. A responsabilidade total é dos utilizadores.

Além disso, o extra requer uma conexão com a Internet para funcionar. A velocidade de resposta do extra depende de vários fatores, como:
- A qualidade da nossa conexão com a Internet.
- O possível atraso (lag) dos serviços de tradução utilizados.
- Fatores relacionados à infraestrutura de rede dos utilizadores.

Recomenda-se que os utilizadores estejam atentos a esses aspectos e realizem os testes necessários para garantir que o extra atenda às suas expectativas e requisitos de segurança.

[Voltar ao índice](#índice)

<h3 id="author-information">1.3 - Informações do autor</h3>

**Informações Técnicas e Medidas de Segurança do extra para NVDA**

Trabalhei muito para tornar o extra o mais robusto possível, contabilizando e lidando com possíveis bugs. Todos os erros são capturados e registados no log do NVDA, facilitando o rastreamento e a rápida resolução dos problemas.

**Problemas com certificados do Windows**

Recentemente, percebi que computadores Windows recém-instalados podem ter problemas com certificados, o que pode ser frustrante. Por esse motivo, incluí uma verificação no início do extra. Caso seja detectada alguma falha relacionada aos certificados, o extra irá regenerá-los automaticamente, garantindo o correto funcionamento tanto do Windows quanto do próprio extra.

**Medidas de segurança**

O extra inclui várias medidas de segurança:
- Não é permitido rodar em telas seguras.
- Não inicia se uma conexão com a Internet não for detectada.

Às vezes, o NVDA pode iniciar mais rápido do que conectar-se à rede Wi-Fi. Nesses casos, será necessário reiniciar o NVDA após a conexão ser estabelecida para utilizar o extra corretamente.

**Gestão de chaves de API**

O extra cria um ficheiro JSON que armazena as chaves de API necessárias para os serviços que as exigem. Este ficheiro, chamado `apis.json`, está localizado na pasta de utilizadores do Windows.

**Principais considerações sobre ficheiros**

Foi decidido armazenar este ficheiro fora do ambiente do extra para evitar que ele, por conter informações confidenciais, seja compartilhado inadvertidamente com uma cópia portátil do NVDA ou em outras situações. Caso o utilizador decida parar de usar o extra, deverá excluir manualmente este ficheiro.

Estas medidas garantem uma melhor gestão e segurança do extra, facilitando a sua utilização e manutenção.

[Voltar ao índice](#índice)

<h2 id="description-configuration">2 - Descrição e configuração</h2>

<h3 id="description-services">2.1 - Descrição dos serviços</h3>

Na sua primeira versão, o extra oferece 7 serviços de tradução:

<h4 id="google">Google</h4>

**4 Serviços do Google**

- **2 Serviços de Web Scraping:** Cada serviço desempenha a mesma função, mas de forma diferente, garantindo que sempre haja uma alternativa disponível caso um deles falhe.
- **2 Serviços via API:** Esses serviços também são ilimitados e gratuitos, mas o abuso deles pode resultar em banimento temporário de IP por algumas horas, após o qual o serviço será restabelecido.
- Todos esses serviços do Google não requerem chaves API e são ilimitados e gratuitos.

<h4 id="deepl">DeepL</h4>

**2 Serviços DeepL**

- **API gratuita:**Esta opção requer a obtenção de uma chave API gratuita na página do DeepL, que oferece 500.000 caracteres por mês.
- **API Pro:** Esta opção também requer uma chave API obtida no site do DeepL. A sua utilização está condicionada ao saldo e ao plano contratado na conta DeepL do utilizador.
- Os termos de uso da API DeepL podem ser encontrados em seu [website](https://www.deepl.com/en/pro/change-plan#developer), e o extra é limitado por estes termos.

<h4 id="libretranslate">LibreTranslate</h4>

**1 serviço LibreTranslate**

- Este serviço está em constante melhoria graças ao seu aprendizado neural contínuo. Embora atualmente não atinja a qualidade do Google, é perfeitamente utilizável.
- Baseado na tecnologia Argos Translate.
- Para utilizar este serviço é necessária uma chave API, que pode ser obtida fazendo uma doação à comunidade [NVDA.es](https://nvda.es/donaciones/).
  - Após a doação, pode solicitar a chave API através do formulário da seguinte [página](https://nvda.es/contacto/), indicando no assunto "Solicitação de chave API" e fornecendo a referência do PayPal, transferência, etc. .
- Além disso, é possível configurar outros serviços LibreTranslate adicionando a chave API e modificando a URL do serviço na secção de configuração do extra.

<h4 id="microsoft-translate">Microsoft Tradutor</h4>

**1 serviço Microsoft Translate**

- Este serviço tem a limitação de que o uso contínuo pode resultar no banimento temporário do IP por alguns minutos.
- Esta proibição só ocorre com uso muito intensivo e em traduções de textos longos.
- O serviço funciona muito bem, mas é recomendável não o utilizar continuamente para evitar interrupções.

Estas opções permitem aos utilizadores escolher entre vários serviços de tradução, garantindo a disponibilidade e flexibilidade do extra com base nas necessidades e preferências individuais.

À medida que o extra recebe atualizações, serviços podem ser adicionados ou removidos. As alterações serão relatadas na seção de atualizações.

[Voltar ao índice](#índice)

<h3 id="configuration">2.2 - Configuração</h3>

**Configurações do extra**

Esta secção detalha como configurar cada um dos serviços disponíveis no extra, incluindo como adicionar chaves de API, modificar URLs de serviço e outras configurações necessárias para personalizar o uso do extra de acordo com as necessidades dos utilizadores.

<h4 id="extra-menu">Menu de extras</h4>

Em NVDA > Preferências > Tradutor Avançado temos um menu que contém o seguinte:

- **Configurações avançadas do tradutor**

  Se clicarmos nesta opção, a janela de configuração do extra será aberta. Esta janela possui 2 áreas:

  - **Em geral**

    Neste separador serão adicionadas as opções gerais do extra. No momento,Possui apenas uma caixa de seleção para ativar ou desativar o cache do extra.

    O extra pode guardar um cache dessas traduções para cada aplicação, o que tornará a tradução mais fácil e rápida em traduções futuras. Além disso, agora ele cria um cache para cada idioma, podendo haver mais de um aplicativo que possua cache para idiomas diferentes.

  - **Módulos de tradução**

    Neste separador podemos escolher o serviço que queremos usar para traduzir. Nos serviços que requerem uma chave API, o gestor de chaves API também será mostrado.

    Podemos ter mais de uma chave API para o mesmo serviço; Por exemplo, no LibreTranslate podemos ter diferentes chaves e URLs para conectar. Podemos adicionar, editar, excluir e definir a chave API padrão que desejamos para o serviço atual.

    A área de gestão de chaves API muda dependendo do serviço que temos. Podemos dar a cada chave de API um nome de identificação para saber rapidamente a qual API estamos nos referindo. Quando tivermos mais de uma chave API para um serviço, o item que tiver um asterisco na lista será o padrão. Isto pode ser alterado com o botão “Padrão”, tornando a chave definida para o referido serviço a chave em que nos concentramos naquele momento.

    Se o serviço de tradução que escolhermos não exigir uma chave API, o gestor não será mostrado.

    Depois temos o botão “OK” e “Cancelar”. Todas as opções têm uma tecla de atalho sobre a qual o NVDA nos informará.

- **Documentação do extra**

  Se clicarmos em "Documentação do extra" esta documentação será aberta.

- **Convide-me para um café se você gosta do meu trabalho**

  Se clicarmos nesta opção, será aberta a página do PayPal onde existe um link que diz “Enviar”. Se clicarmos neste link, ele nos pedirá para fazer login em nossa conta e nos deixar na página de doações.

  Direi apenas que tomei muito café a fazer este extra.

[Voltar ao índice](#índice)

<h4 id="extra-hotkeys">extra-hotkeys</h4>

Em NVDA > Preferências > definir comandos... > Tradutor Avançado temos as seguintes teclas que podemos configurar.

As teclas padrão não estão atribuídas para que os utilizadores possam escolher a sua melhor distribuição. São as seguintes:

- **Abre as configurações do extra**

  Este acesso abrirá rapidamente a configuração do extra.

- **Ativar ou desativar o cache de tradução**

  Este acesso ativará ou desativará o cache sem a necessidade de entrar na configuração.

- **Ativar ou desativar tradução simultânea online**

  Este acesso ativa ou desativa a tradução. É o acesso principal que começará a ser traduzido à medida que avançamos com as setas do cursor. Se tudo estiver correto, ouviremos a tradução; Se ouvirmos o texto original, teremos que olhar o log do NVDA e ver o que aconteceu.- **Alterar o módulo de tradução**

  Este acesso abrirá uma janela com todos os serviços de tradução disponíveis. Podemos mover com as setas e selecionar com “Enter”. O serviço que selecionarmos será o que temos por padrão.

- **Alterar idioma de destino**

  Este acesso abrirá uma janela com os idiomas de destino disponíveis no serviço que selecionamos. Cada serviço possui idiomas e, por exemplo, se estamos traduzindo um texto que está em russo e queremos ouvi-lo em inglês, nesta caixa de diálogo teremos que selecionar Inglês. Percorremos a caixa de diálogo com as setas do cursor e "Enter" para selecionar o idioma que desejamos.

  Os nomes dos idiomas são obtidos no nosso idioma do NVDA, admitindo apenas aqueles que o NVDA suporta. Por esta razão, os nomes dos idiomas que estão em inglês podem aparecer na lista, uma vez que o NVDA não os tem traduzidos. O código ISO do idioma é adicionado ao lado de cada nome de idioma.

- **Alterar idioma de origem**

  Igual ao anterior, mas esta caixa de diálogo só é válida para o tradutor Microsoft. O serviço da Microsoft não permite que você defina o idioma de origem como automático para detectar qual idioma é enviado para você, então teremos que escolhê-lo nós mesmos.

  Os demais serviços não poderão utilizar esta caixa de diálogo, pois a sua opção padrão é detectar qual idioma está sendo enviado.

- **Copiar o último texto traduzido para a área de transferência**

  Este acesso copiará o último texto que foi traduzido para a área de transferência.

- **Excluir o cache de tradução do aplicativo em foco no momento**

  Se clicarmos uma vez neste acesso, ele nos dará informações; Se pressioná-lo duas vezes rapidamente, ele limpará o cache do aplicativo que está em foco no momento e nos informará o resultado.

- **Excluir todas as traduções armazenadas em cache para todos os aplicativos**

  Este acesso, pressionado uma vez, nos dará informações; Pressionado duas vezes rapidamente, limpará todo o cache do extra, oferecendo também informações.

- **Mostrar o histórico de tradução**

  Irá mostrar uma caixa de diálogo com as últimas 500 traduções de uma lista. Podemos pesquisar e rever o texto fonte e o texto traduzido em caixas somente leitura. Esta caixa de diálogo nos permitirá pesquisar todo o histórico, copiar o texto fonte e o texto traduzido para a área de transferência ou ambos.

  Também permite que alterne entre o texto fonte e o texto traduzido e os trabalhe de qualquer maneira. Além disso, podemos deletar todo o histórico para começar do zero.

  Apagar o histórico sempre que o NVDA é reiniciado.

- **Traduzir o texto selecionado**

  Esta ação irá traduzir o texto que selecionamos e focamos. Se for um texto grande, será aberta uma caixa de diálogo com a percentagem da tradução. O referido diálogo pode ser cancelado, o que também cancelará a tradução.

  Assim que a tradução for concluída,o texto será mostrado em uma caixa de diálogo para que possamos explorá-lo.

  Esta opção utiliza o serviço Google Translate e este serviço não pode ser alterado, sendo escolhido internamente por ser o que dá melhores resultados para textos longos.

[Voltar ao índice](#índice)

<h2 id="solução de problemas">3 - Solução de problemas</h2>

<h3 id="common-problems-and-solutions">Problemas e soluções comuns</h3>

**Conexão com a internet**
- Verifique se a sua conexão com a Internet está ativa e funcionando corretamente.
- Reinicie seu roteador ou modem, se necessário.

**Erros de certificado**
- Se ocorrerem erros de certificado, certifique-se de que a data e a hora do sistema estejam corretas.
- Verifique se os certificados necessários estão instalados e atualizados.

**Problemas de desempenho**
- Certifique-se de que o seu computador atenda aos requisitos mínimos de sistema.
- Feche outros aplicativos que possam estar a consumir muitos recursos.

[Voltar ao índice](#índice)

<h3 id="how-to-consult-the-nvda-log">Como consultar o log do NVDA</h3>

1. Abra o NVDA.
2. Vá para `NVDA > Ferramentas > Ver Log`.
3. Na janela de registo, procure erros ou mensagens relacionadas ao Advanced Translator.

[Voltar ao índice](#índice)

<h2 id="agradecimentos">4 - Agradecimentos</h2>

Agradeço a todos os programadores do NVDA pelo seu excelente trabalho.

E não quero deixar de dizer que o início deste extra é o extra (TRANSLATE) do Yannick PLASSIARD, com o qual aprendi e utilizei algumas funções.

Também a Alexy Sadovoy, também conhecido como Lex, ruslan, beqa, Mesar Hameed, Alberto Buffolino e outros colaboradores do NVDA também pelo extra (Instant Translate) do qual um dos métodos para o Google foi obtido e foi modificado para implementá-lo no Advanced Translator.

Este extra é o trabalho de vários anos lançando versões não oficiais e o estudo do uso de traduções offline.

A aprendizagem é o resultado deste complemento, tendo em conta que no futuro trará novidades surpreendentes.

[Voltar ao índice](#índice)

<h3 id="translators">Tradutores</h3>

- **Nome do Colaborador 1:** Descrição da contribuição.

[Voltar ao índice](#índice)

<h2 id="version-record">5 - Registo de versão</h2>

Nesta secção será adicionado um registro de versões, onde serão postadas as novidades de cada versão.

O manual é baseado na primeira versão, portanto, não será atualizado continuando a servir de base.

Notícias serão adicionadas nesta secção.

[Voltar ao índice](#índice)

<h3 id="version-1-0">Versão 2024.06.06</h3>

- Lançamento inicial do extra.
- Suporte para 7 serviços de tradução.
- Funcionalidades básicas de tradução simultânea e gestão de chaves API.

[Voltar ao índice](#índice)