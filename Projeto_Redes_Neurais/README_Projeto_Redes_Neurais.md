## Classificação das espécies do cluster Drosophila buzzatii (grupo D. repleta) utilizando Redes Neurais Convolucionais.

## Resumo 
O cluster Drosophila buzzatii compreende sete espécies endêmicas e cactófilas da América do Sul. Tradicionalmente, a classificação dessas espécies tem se baseado nas características dos edeagos, que são estruturas da genitália externa masculina. No entanto, essa abordagem é suscetível ao 'erro do pesquisador' durante o contorno das estruturas, o que pode levar a resultados inconsistentes. Para superar esse desafio, foi implementado uma técnica de aprendizado de máquina utilizando uma Rede Neural Convolucional (RNC). Inicialmente, a RNC foi treinada para reconhecer quatro espécies do cluster. A construção da rede partiu do zero, e foram realizados testes em um conjunto de 7.200 imagens após a ampliação artificial dos dados com nove modificações. Durante o processo de treinamento, foi observado melhorias significativas quando aumentado o número de filtros nas camadas de convolution e max-pooling, bem como o número de épocas. Além disso, foram calibrados os parâmetros de aumento de dados para evitar perda de informações devido a deslocamentos ou rotações excessivas das imagens. Como resultado, a rede alcançou uma precisão de classificação de 86,14% para as quatro espécies avaliadas. No entanto, o recall variou de 0,18 a 0,47 entre as espécies. Em conclusão, embora a RNC tenha representado uma abordagem inovadora para a classificação de espécies de Drosophila, reconhece-se a necessidade contínua de aprimoramentos e otimizações. Com refinamentos contínuos, essa metodologia promete ser uma ferramenta altamente promissora, não apenas para a classificação de espécies deste grupo específico, mas também para a categorização de espécies em diversos grupos taxonômicos, aumentando assim a precisão e confiabilidade da classificação taxonômica.

## Dados

**Fonte dos Dados**: A rede foi treinada utilizando uma base de dados de imagens de edeagos das diferentes espécies do cluster D. buzzatii, armazenada no Laboratório de Genética Evolutiva do Departamento de Biologia – FFCLRP – USP. Como o conjunto de treinamento (CTre) não era ideal, utilizou-se a técnica de Data Augmentation, que cria variações artificiais nos dados de treinamento através da aplicação de transformações simples nas imagens originais. Entre as transformações mais comuns estão rotações, espelhamento horizontal, ajustes de brilho e contraste, zoom e outras distorções. O CTre foi aumentado nove vezes ao aplicar rotação de 180 graus, deslocamento horizontal e vertical aleatório, cisalhamento aleatório, efeito de zoom, além de espelhamentos horizontais e verticais aleatórios.


Tabela 1. Espécies incluídas e número de imagens utilizadas para a construção do modelo.

| Classe | Espécie          | Base de Dados | Treinamento | Validação |
|--------|------------------|---------------|-------------|-----------|
| 0      | _D. antonietae_  | 394           | 315         | 79        |
| 1      | _D. gouveai_     | 163           | 130         | 33        |
| 2      | _D. seriema_     | 209           | 167         | 42        |
| 3      | _D. serido_      | 236           | 188         | 48        |
|        | **Total**        | **1002**      | **800**     | **202**   |



## Repositório:

1. **RNC_Final.py**: Script em Python que implementa a Rede Neural Convolucional (RNC) utilizada para a classificação das espécies do cluster Drosophila buzzatii. O script inclui a definição da arquitetura da rede, o processo de treinamento com técnicas de Data Augmentation, o ajuste de parâmetros e a avaliação do modelo utilizando métricas como acurácia, recall e matriz de confusão. Além disso, o script contém a implementação de otimizações para melhorar o desempenho da rede.
2. **Resultado_RNC_Final.txt**: Resultado da matriz de confusão, recall e precisão.
3. **Resultado_treinamento_RNC_Final.txt**: Resultado do treinamento da RNC.
