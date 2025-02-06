# Modelagem de Nicho Ecológico
A Modelagem de Nicho Ecológico (MNE) permite avaliar a expansão ou contração de habitats adequados das espécies com base nas coordenadas geográficas de ocorrência.
Este repositório armazena um conjunto de trabalhos que mostra como as áreas de adequabilidade de diferentes espécies foram moldadas pelo paleoclima e como elas podem ser afetadas pelas previsões climáticas futuras. 

## Objetivo
O objetivo deste repositório é mostrar algumas das ferramentas e metodologias utilizadas na MNE.

## Fontes de Dados
- **Ocorrência de Espécies:** [GBIF](https://www.gbif.org/), [SpeciesLink](https://specieslink.net/)
- **Dados Climáticos e Modelos Climáticos:** [WorldClim](https://www.worldclim.org/data/index.html), [CHELSA](https://chelsa-climate.org/)
- **The Intergovernmental Panel on Climate Change**: [https://www.ipcc.ch/](https://www.ipcc.ch/)

## Metodologia
A MNE foi realizada utilizando uma abordagem de *ensemble*, combinando algoritmos baseados em distância como *Domain* e *Distância de Mahalanobis* e métodos de aprendizado de máquina, como *Máxima Entropia* (Maxent) e *Máquinas de Vetores de Suporte* (SVM). A colinearidade das variáveis bioclimáticas foi analisada usando o Fator de Inflação da Variância (VIF) e a correlação de Pearson.
No entanto, existem diversas abordagens para fazer a MNE.

## Ferramentas Utilizadas
- **Pacotes R:** raster, rgdal, dismo, usdm, randomForest, rJava
- **Software de Visualização:** [QGIS](https://qgis.org)

### Artigos de Referência
1. Stylosanthes: [https://doi.org/10.1016/j.jaridenv.2024.105124](https://doi.org/10.1016/j.jaridenv.2024.105124)
2. Tacinga inamoena: [https://doi.org/10.1093/botlinnean/boad054](https://doi.org/10.1093/botlinnean/boad054)
3. Cluster de D. buzzatii: [https://doi.org/10.1093/jhered/esy042](https://doi.org/10.1093/jhered/esy042)
4. Artigo de D. antonietae e D. meridionalis: [https://doi.org/10.1093/aesa/saaa011](https://doi.org/10.1093/aesa/saaa011)
5. Artigo de D. antonietae e D. serido: [https://doi.org/10.1111/jeb.13934](https://doi.org/10.1111/jeb.13934)
