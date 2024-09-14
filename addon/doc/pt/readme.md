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

À medida que o extra recebe atualizações, serviços podem ser adicionados ou removidos. As alterações serão relatadas na secção de atualizações.

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

- **Português:** Ângelo Abrantes.
- **Turco:** Umut Korkmaz.
- **Russo:** Valentin Kupriyanov.
- **Inglês:** Samuel Proulx.
- **Ucraniano:** Heorhii Halas e Volodymyr Pyrih.
- **Francês:** Rémy Ruiz.

[Voltar ao índice](#índice)

<h2 id="version-record">5 - Registro de versão</h2>

Nesta secção será adicionado um registo de versões, onde serão postadas as novidades de cada versão.

O manual é baseado na primeira versão; portanto, não será atualizado, servindo , continuamente, de base.

Notícias serão adicionadas nesta secção.

[Voltar ao índice](#índice)

<h3 id="version-2024-06-06">Versão 2024.06.06</h3>

- Lançamento inicial do extra.
- Suporte para 7 serviços de tradução.
- Funcionalidades básicas de tradução simultânea e gestão de chaves API.

[Voltar ao índice](#índice)

<h3 id="version-2024-06-16">Versão 2024.06.16</h3>

- **Adicionada a capacidade de copiar a tradução traduzida para a área de transferência por seleção em vez de mostrá-la em uma caixa de diálogo:**

Foi adicionada uma opção para copiar automaticamente o texto traduzido para a área de transferência, quando esta função for selecionada, evitando a necessidade de mostrar uma caixa de diálogo adicional.

Esta opção foi adicionada na caixa de diálogo de configuração do extra, em Geral.

Se esta opção estiver marcada, não será mais mostrada uma caixa de diálogo, quando traduzirmos um texto selecionado, mas sim copia diretamente para a área de transferência.

- **Traduzir o que estiver na área de transferência:**

Agora é possível traduzir diretamente o conteúdo localizado na área de transferência, proporcionando uma forma rápida e eficiente de traduzir textos copiados.

Se nada for traduzido, ele nos informará o que está na área de transferência ou, se não houver nada na área de transferência, nos notificará com uma mensagem.

- **Traduzir a última coisa falada pelo sintetizador:**

Foi incorporada uma funcionalidade que permite traduzir a última frase ou texto falado pelo sintetizador de voz, melhorando a acessibilidade e usabilidade do complemento.

Se a última coisa verbalizada não puder ser traduzida, ele nos dirá a última coisa que foi verbalizada no idioma de origem.

- **Mostrar traduções em linhas braille:**

A nova versão inclui suporte para mostrar  traduções em dispositivos de linhas Braille, facilitando o acesso às traduções.

Funcionará apenas em dispositivos que possuam uma linha braille configurada.

Esta função está em fase de testes.

- **Atualizador de idioma do extra:**

Foi implementado um atualizador para manter os idiomas do plugin sempre atualizados, garantindo a disponibilidade dos idiomas mais recentes e precisos.

Agora, no menu NVDA > Preferências > Tradutor Avançado

Teremos um novo item chamado Atualizar idiomas do extra (Sem atualizações).

Este item poderá nos informar se houver atualizações, por exemplo:Atualizar idiomas do extra (3 atualizações disponíveis)

Se o pressionar, aparecerá uma caixa de diálogo com os novos idiomas, com as atualizações ou com um dos dois se não houver em ambos.

Podemos instalar ou saltar.

Se clicarmos em instalar, os idiomas serão baixados e instalados e o NVDA será reiniciado.

O item de menu é atualizado a cada 30 minutos, verificando atualizações, ou a cada reinicialização.

O gasto de dados dessa verificação é ridículo porque para aqueles locais que têm problemas de dados, é menos de 1kb que precisa de verificar.

Este atualizador tornará mais fácil compartilhar atualizações de idiomas do extra com os usuários rapidamente assim que eles chegarem e sem a necessidade de lançar uma nova versão com os novos idiomas.

Cada nova versão do extra virá com todos os idiomas novos e atualizados que entretanto forem chegando.

- **Bug de leitura contínua corrigido:**

Corrigido um problema que causava erros de leitura contínua, melhorando a estabilidade e o desempenho do plugin durante o uso prolongado.

- **Notas do autor:**

Todas as novas funções, como traduzir a área de transferência, traduzir as últimas palavras faladas pelo sintetizador ou verificar atualizações de idioma, podem ser atribuídas por atalhos.

Recomendo que, se não vamos usar nenhuma opção, não lhe adicionemos qualquer atalho, para que possamos tê-lo em outros plugins. Vamos adicionar aqueles que podem ser úteis para nós.

À medida que utilitários são adicionados, mais atalhos serão necessários e um utilitário pode não funcionar para um e pode funcionar para outro, por isso atribuímos apenas aqueles que vamos usar.

[Voltar ao índice](#índice)

<h3 id="version-2024-06-23">Versão 2024.06.23</h3>

* Adicionado novo módulo DeepL Translator (gratuito)

Este novo módulo não necessita de chave API e é utilizado para tradução simultânea 

* Correções de bugs

[Voltar ao índice](#índice)

<h3 id="version-2024-09-07">Versão 2024.09.07</h3>
#### Interface de tradução

A **Interface de Tradução** é o componente principal do extra **Advanced Translator** para o NVDA. Esta interface permite ao utilizador traduzir textos entre diferentes idiomas de forma eficiente, mostrando o texto original e traduzido, além de oferecer diversas opções de personalização.

Para invocá-lo, teremos que lhe atribuir uma combinação de teclas, no "definir comandos" ou no menu virtual (explicado abaixo).

##### Principais características:

1. **Entrada de texto fonte**: Permite ao utilizador escrever ou colar o texto que deseja traduzir. Pode ser acedido rapidamente com a combinação de teclas `Alt+1`.
   
2. **Texto de destino (resultado)**: A área onde o texto traduzido é mostrado. Este campo é somente leitura e pode ser focado com `Alt+2`.

3. **Seleção do idioma de origem**: Permite selecionar o idioma do texto de origem. O idioma padrão é a opção "Detecção automática",o que permite ao sistema detectar automaticamente o idioma do texto. É acedido com `Alt+3`.

4. **Seleção do idioma de destino**: Permite selecionar o idioma para o qual deseja traduzir o texto. Pode ser focado com `Alt+4`.

5. **Contador de caracteres**: Mostra o número de caracteres no campo de texto de origem. É útil saber a quantidade de texto que será traduzido. Ele é acessado com `Alt+5`.

6. **Botões de ação**:
   - **Traduzir**: Inicia a tradução do texto inserido.
   - **Ouvir**: Obtém o áudio da tradução e permite que seja reproduzido através de um player integrado (ver secção abaixo).
   - **Trocar**: Troca o idioma de origem pelo idioma de destino, útil se desejar reverter os idiomas de tradução.
   - **Limpar**: Limpa os campos de texto de origem e de destino.
   - **Colar no foco**: Cola o texto traduzido na janela ativa ou campo de texto atrás da interface. Também pode ser ativado com `F3`.
   - **Fechar**: Fecha a janela de tradução.

##### Atalhos de teclado:

- `Alt+1`: Foca a caixa de texto fonte.
- `Alt+2`: Foca a caixa de texto de destino.
- `Alt+3`: Selecione o idioma de origem.
- `Alt+4`: Selecione o idioma de destino.
- `Alt+5`: Foca o contador de caracteres.
- `F3`: Cole o texto traduzido na janela ativa.
- `Esc`: Fecha a caixa de diálogo de tradução.

##### Comportamento em caso de erros:

- Caso não haja conexão com a Internet, o sistema mostrará uma mensagem informando a falta de conexão.
- Se a caixa de texto fonte estiver vazia, o utilizador receberá um aviso solicitando a inserção do texto antes de realizar a tradução.
- Se os idiomas de origem e de destino forem iguais, será mostrado um aviso indicando que o texto não precisa ser traduzido para o mesmo idioma.

##### Recursos adicionais:

- **Detecção automática de idioma**: Se "Detecção automática" for selecionado no idioma de origem, o plugin tentará identificar automaticamente o idioma do texto a ser traduzido.
- **Intercâmbio de idiomas**: Esta função é útil quando deseja traduzir um texto de volta para o idioma original.

#### Reprodutor de áudio

Quando o utilizador usa a opção **Ouvir** após realizar uma tradução, o extra converte o texto traduzido em um arquivo de áudio e o reproduz através de um player integrado. Este player inclui controles básicos e avançados para gerenciar a reprodução de áudio.

##### Recursos do reprodutor:

1. **Botões de controlo**:
   - **Retroceder (F1)**: Retrocede a reprodução de acordo com o tempo selecionado. O utilizador pode configurar este tempo.
   - **Reproduzir/Pausar (F2)**: inicia ou pausa a reprodução do ficheiro de áudio.
   - **Avanço rápido (F3)**: Avanço rápido da reprodução de acordo com o tempo definido pelo utilizador.
   - **parar (F4)**: Pára a reprodução completamente.

2. **Volume e velocidade**:- **Volume (F5/F6)**: Ajusta o volume de reprodução usando um controle deslizante.
   - **Velocidade (F7/F8)**: Altere a velocidade de reprodução, com opções de 0,50x a 2,0x a velocidade normal.

3. **Texto associado**: mostra o texto traduzido numa caixa de somente leitura, permitindo ao utilizador visualizar o que está sendo reproduzido.

4. **guardar**: Permite guardar o ficheiro de áudio gerado em formato WAV no sistema do utilizador.

5. **Fechar**: Fecha o reprodutor e liberta os recursos associados.

##### Atalhos de teclado:

- `F1`: Atrasar a reprodução.
- `F2`: Reproduzir ou pausar o áudio.
- `F3`: Avanço rápido na reprodução.
- `F4`: Parar a reprodução.
- `F5/F6`: Ajusta o volume.
- `F7/F8`: Alterar a velocidade de reprodução.
- `F9`: Informação do tempo de reprodução.
- `Shift+F10/Aplicativos`: Os botões voltar e avançar mostrarão um menu contextual para escolher o tempo correspondente.

##### Recursos adicionais:

- **guardar áudio**: os utilizadores podem optar por guardar o ficheiro de áudio nos seus dispositivos no formato WAV para uso posterior.
- **Menu de opções avançadas**: O reprodutor permite escolher o tempo exato para atrasar ou avançar a reprodução através de um menu contextual (acedido com a tecla `Shift+F10`) ou tecla de aplicativos.

#### Menu virtual

Foi adicionado um menu virtual que contém todas as opções que o extra possui.

Podemos invocar do menu virtual todas as opções que podemos atribuir no "definir comandos, desta forma a partir do menu virtual o extra pode ser utilizado completamente sem a necessidade de ter mais teclas atribuídas.

Isto depende do utilizador.

Para invocar o menu virtual teremos que lhe atribuir um atalho.

A utilização do menu virtual é simples, uma vez invocado teremos que pressionar a tecla correspondente à ação que queremos executar.

Uma vez pressionado, será executado e seremos sempre informados do que foi feito. Se pressionarmos uma tecla que não esteja atribuída, o menu virtual será fechado e também poderemos fechá-lo com escape.

##### Atalhos de teclado do menu virtual

O menu virtual do Advanced Translator permite aceder rapidamente as funções mais úteis do extra. Abaixo estão os atalhos que pode usar para realizar várias ações:

- **`P`**: **Abrir configuração**  
  Abre as configurações do Advanced Translator onde pode ajustar os idiomas e serviços de tradução.

- **`U`**: **Verificar se há atualizações de idioma**  
  Verifique e baixe as atualizações disponíveis para os idiomas do extra.

- **`O`**: **Alterar idioma de origem**  
  Altere o idioma do texto que deseja traduzir (idioma de origem).

- **`D`**: **Alterar idioma de destino**  
  Altere o idioma para o qual deseja traduzir o texto (idioma de destino).

- **`C`**:**Alterar serviço de tradução**  
  Permite alternar entre os serviços de tradução disponíveis, como Google, DeepL, Microsoft, entre outros.

- **`A`**: **Excluir todo o cache de tradução**  
  Limpa todas as traduções em cache.

- **`X`**: **Excluir cache de tradução do aplicativo atual**  
  Limpe as traduções em cache apenas para o aplicativo que você abriu.

- **`G`**: **Ativar/desativar cache de tradução**  
  Ative ou desative o recurso de cache que guarda temporariamente as traduções.

- **`L`**: **Copia a última tradução para a área de transferência**  
  Copie a última tradução feita para a área de transferência para colá-la onde precisar.

- **`B`**: **Traduzir texto da área de transferência**  
  Traduz o conteúdo atual da área de transferência.

- **`V`**: **Traduzir o último texto falado**  
  Traduz o último texto que o NVDA leu em voz alta.

- **`T`**: **Ativar/desativar tradução em tempo real**  
  Ative ou desative a tradução automática enquanto navega pelos textos.

- **`S`**: **Traduzir o texto selecionado**  
  Traduza o texto que selecionou no aplicativo.

- **`Z`**: **Traduzir texto do objeto do navegador**  
  Traduz o texto de um objeto específico no navegador, como um botão ou caixa de texto.

- **`W`**: **Interface de tradução aberta**  
  Abre a janela gráfica onde pode inserir manualmente o texto que deseja traduzir.

- **`I`**: **Detectar idioma selecionado**  
  Detecta automaticamente o idioma do texto selecionado.

- **`J`**: **Ativar/desativar troca automática de idioma**  
  Ative ou desative a troca automática se o idioma de origem detectado corresponder ao idioma de destino.

- **`K`**: **Trocar idiomas primários e alternativos**  
  Troque o idioma principal pelo idioma alternativo nas configurações do tradutor.

- **`H`**: **Mostrar histórico de tradução**  
  Mostra um histórico de traduções recentes realizadas.

- **`F1`**: **Mostrar lista de comandos**  
  Mostra uma caixa de diálogo listando comandos de tecla única para o Advanced Translator.

#### Detecção de idioma

Esta opção permite detectar automaticamente o idioma do texto selecionado em qualquer aplicativo. Para usar este recurso:
1. Selecione o texto cujo idioma deseja conhecer.
2. Use o atalho de teclado configurado no "definir comandos" (ou no menu virtual) para ativar a detecção de idioma.
3. O sistema detectará e informará o idioma em que o texto selecionado está escrito.
Este recurso é útil quando não tem certeza do idioma de um texto e precisa conhecê-lo antes de traduzi-lo ou realizar qualquer outra ação.

#### Troca Automática de Idiomas no NVDA Advanced Translator

  1. Ative a troca automática pressionando o atalho de teclado correspondente ou acessando-o no menu virtual.
  2.Se o texto selecionado estiver no mesmo idioma do idioma de destino, o sistema mudará automaticamente o idioma de destino para o idioma alternativo para evitar traduções desnecessárias.
  3. Pode desativar esta opção a qualquer momento usando o mesmo atalho.

##### Configurações de idioma no extra

- Pode configurar **idiomas de destino** e **idiomas alternativos** acedendo **Configurações do plug-in** na secção **Geral**. A partir daí pode selecionar os idiomas que serão usados para troca automática.

Este recurso é útil para evitar confusões na tradução de textos cujo idioma de origem é igual ao idioma de destino, alternando automaticamente para um idioma alternativo configurado.

#### Ajuda nas caixas de diálogo do extra

Adicionada funcionalidade para mostrar ajuda contextual nas caixas de diálogo do extra. Pressionar a combinação de teclas `Ctrl+H` mostrará uma pequena descrição da função do widget que está atualmente em foco.

Em qualquer lugar, nas caixas de diálogo do plugin, se precisar de informações sobre a função de um botão, caixa de texto, controlo deslizante ou outro controlo, pode simplesmente pressionar `Ctrl+H`. Isso exibirá uma breve descrição do widget em foco, fornecendo um guia rápido para seu uso.

#### Traduzir texto do objeto do navegador


1. Coloque o cursor sobre o objeto que deseja traduzir (pode ser um botão, uma caixa de texto, etc.).
2. Ative a funcionalidade pressionando a combinação de teclas atribuída ou através do menu virtual.
3. O extra irá traduzir o texto contido naquele objeto e mostrá-lo ou pronunciá-lo, dependendo das configurações.

- Traduza qualquer texto contido no objeto selecionado dentro de uma página web, aplicativo ou qualquer outra interface onde o NVDA interaja.
- Útil para traduzir pequenos trechos de texto que não fazem parte do corpo principal de uma página ou aplicativo, como menus, botões ou rótulos.
- Caso o objeto não contenha texto ou esteja inacessível, o extra mostrará uma mensagem informando que não há texto para traduzir.

- Pode aceder a esta funcionalidade tanto no menu virtual do extra quanto definindo uma tecla de atalho no "definir comandos" do NVDA.

#### Módulo OpenAI

Foi adicionado um novo módulo para tradução com OpenAI com o modelo chatGPT-4º-mini, que é o mais barato e rápido.

Este módulo está em teste, às vezes apresentando um pouco de atraso, mas irá melhorar em versões futuras.

Este módulo requer que uma chave API seja atribuída na configuração/módulos.

O OpenAI é pago, portanto cabe ao utilizador verificar os seus gastos.

No link a seguir pode ver a despesa que tem:

[https://platform.openai.com/usage](https://platform.openai.com/usage)

#### Melhoria no módulo Microsoft

O módulo tradutor da Microsoft foi escrito do zero e melhorou a velocidade,estabilidade e poder ter mais tempo de tradução até que bloqueiem por uso e tenhamos que esperar alguns minutos para traduzir novamente.

Até agora, nos testes realizados e traduzindo simultaneamente muito texto para uso mais que normal, não sofri nenhuma restrição.

Então no momento funciona e foi melhorado em relação ao módulo anterior.

#### Outros

* Corrigido problema na verbalização de algumas mensagens.
* Alterada forma de verificar se há internet.
* Correções de bugs
* Língua francesa oficialmente adicionada.

[Voltar ao índice](#índice)