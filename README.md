eggnogCOGextractor.py

Description
The eggnogCOGextractor.py script is designed to extract and analyze COG (Clusters of Orthologous Groups) features from EggNOG-mapper output files. This script is particularly useful for bioinformaticians working on comparative genomics, functional annotation, and pathway analysis.

Usage
To run the script, use the following command:
python eggnogCOGextractor.py

Input Example
The input file should be an EggNOG-mapper output file in tab-separated format. An example of the first few lines of the input file:
#query  seed_ortholog evalue  score   eggNOG_OGs  max_annot_lvl  COG cat  Description    Preferred_name  GOs EC  KEGG_ko KEGG_Pathway    KEGG_Module KEGG_Reaction   KEGG_rclass BRITE   KEGG_TC CAZy    BiGG_Reaction   tax_scope   eggNOG_HMM_model Annotation_tax_scope   Matching_OGs
gene_1  KOG0001  1e-50  500.0   COG0001|KOG0001|NOG0001  1  J   Ribosomal protein S12    rpsL    GO:0006412 GO:0003735 GO:0005622  2.7.7.6   K01193  path:map00195 path:map00230   M00002  R00200  rc01010 BR:ko00001 2.A.1.1.1 GT1 GH13    RXN-12345  12908:123    5.0.0.1   1234_5678 1234_5678|5678_9101
gene_2  KOG0002  2e-20  300.0   COG0002|KOG0002|NOG0002  1  K   Chromatin structure and dynamics   hisT    GO:0006396 GO:0005634  3.6.1.3   K03654  path:map00770 path:map00310   M00233  R00123  rc02020 BR:ko00010 3.A.1.2.2 GT2 GH2 RXN-67890  11056:789    5.0.0.2   2345_6789 2345_6789|6789_1234

Output Example
The output file will contain the extracted and processed COG features in a tab-separated format. An example of the first few lines of the output file:
Gene_ID COG_ID  COG_Category  COG_Description
gene_1  COG0001 J   Ribosomal protein S12
gene_2  COG0002 K   Chromatin structure and dynamics

Citation
If you use this script for your research, please consider citing it as follows:

Sharma, V. (2024). eggnogCOGextractor.py [Python script]. Retrieved from https://github.com/vsmicrogenomics/Citation
If you use this script for your research, please consider citing it as follows:

Sharma, V. (2024). eggnogCOGextractor.py [Python script]. Retrieved from https://github.com/vsmicrogenomics/Pathway-Feature-Identification
