#Phenotype Based Analysis
rm(list=ls())
Pheno <- read.csv(file="query.output.genome_summary.csv", header=TRUE)
head(Pheno)
dim(Pheno)

## Input Phenotype based gene list
ph <- read.csv(file="Genelist.csv", header=TRUE)
head(ph)
dim(ph)

## Inititialise the list object
my.list <- list()

## Read each genomic position in Table B N=2575 using For loop
for (i in 1:nrow(ph))
{ 
  
  print (ph[i,])  
  # my.list[[i]] <- filter5[grepl(ph[i,], filter5$Gene.refGene, ignore.case = TRUE),]
  my.list[[i]] <- Pheno[grep(paste("\\b",ph[i,],"\\b", sep=""), Pheno$Gene.refGene, perl=TRUE,  ignore.case = TRUE),]
  
}
final.data <- do.call(rbind, my.list)
head(final.data)
dim(final.data)

write.csv(final.data, file="6_Phenotype_Gene_Variant-list.csv", row.names=F)