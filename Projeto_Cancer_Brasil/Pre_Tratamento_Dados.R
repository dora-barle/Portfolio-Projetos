##Juntar CSV

library(dplyr)

###Total de registros 1.987.418
###Registros Trabalhados 667016

# Defina o caminho para os arquivos
arquivos <- list.files(pattern = "*.csv", full.names = TRUE)

colunas_por_arquivo <- lapply(arquivos, function(arquivo) {
  colnames(read.csv(arquivo))
})

# Nomear a lista com os nomes dos arquivos
names(colunas_por_arquivo) <- basename(arquivos)

# Exibir as colunas de cada arquivo
print(colunas_por_arquivo)

# Verificar se todas as colunas são iguais
colunas_iguais <- Reduce(setequal, colunas_por_arquivo)

if (colunas_iguais) {
  cat("Todos os arquivos têm as mesmas colunas. Pronto para combinar!\n")
} else {
  cat("Os arquivos têm colunas diferentes. Veja a lista de colunas:\n")
  print(colunas_por_arquivo)
}

# Ler e combinar todos os arquivos sem modificar os nomes das colunas
dados_combinados <- do.call(rbind, lapply(arquivos, function(arquivo) {
  read.csv(arquivo, sep = ";", stringsAsFactors = FALSE, check.names = FALSE)
}))

# Salvar o arquivo combinado, preservando os nomes das colunas
write.csv(dados_combinados, "dados_combinados.csv", row.names = FALSE, sep = ";")
cat("Arquivo combinado criado: dados_combinados.csv\n")


# Leia e combine os arquivos em um único dataframe
dados_combinados <- arquivos %>%
  lapply(read.csv) %>%
  bind_rows()

write.csv(dados_combinados, "dados_5com.csv", row.names = FALSE)


