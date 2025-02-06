# Modelagem de Nicho Ecológico
Este repositório armazena informações relacionadas à modelagem de nicho ecológico (MNE) de várias espécies, com foco na análise dos impactos das mudanças climáticas.

## Objetivo
O objetivo deste trabalho é entender como as áreas de adequabilidade para espécies podem ter sido moldadas pelo paleoclima e como elas podem ser afetadas pelas previsões climáticas futuras, com base em dados bioclimáticos e geoespaciais.

## Fontes de Dados
- **Ocorrência de Espécies:** [GBIF](https://www.gbif.org/), [SpeciesLink](https://specieslink.net/)
- **Dados Climáticos e Modelos Climáticos:** [WorldClim](https://www.worldclim.org/data/index.html), [CHELSA](https://chelsa-climate.org/)

## Metodologia
A modelagem de nicho ecológico foi realizada utilizando uma abordagem de *ensemble*, combinando algoritmos baseados em distância (como *Domain* e *Distância de Mahalanobis*) e métodos de aprendizado de máquina, como *Máxima Entropia* (Maxent) e *Máquinas de Vetores de Suporte* (SVM). A colinearidade das variáveis bioclimáticas foi analisada usando o Fator de Inflação da Variância (VIF) e a correlação de Pearson.

## Ferramentas Utilizadas
- **Pacotes R:** raster, rgdal, dismo, usdm, randomForest, rJava
- **Software de Visualização:** [QGIS](https://qgis.org)

### Artigos de Referência
1. Stylosanthes: [https://doi.org/10.1016/j.jaridenv.2024.105124](https://doi.org/10.1016/j.jaridenv.2024.105124)
2. Tacinga inamoena: [https://doi.org/10.1093/botlinnean/boad054](https://doi.org/10.1093/botlinnean/boad054)
3. Cluster de D. buzzatii: [https://doi.org/10.1093/jhered/esy042](https://doi.org/10.1093/jhered/esy042)
4. Artigo de D. antonietae e D. meridionalis: [https://doi.org/10.1093/aesa/saaa011](https://doi.org/10.1093/aesa/saaa011)
5. Artigo de D. antonietae e D. serido: [https://doi.org/10.1111/jeb.13934](https://doi.org/10.1111/jeb.13934)

