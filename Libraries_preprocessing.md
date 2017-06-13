##Libraries preprocessing.

###Not aligning reads removal.

The libraries were named 00_EC.fastq, 01_EC.fastq, 04_EC.fastq and 10_EC.fastq for Immature embryos, one month, four months and 10 months old callus respectively.
The four libraries were concatenated and collapsed to map it against the ok_full_zm.fasta file.

    *.fastq > full_reads.fq
    fastx_collapser -i full_reads.fq -o full_reads_collapsed.fasta

The individual libraries were collapsed also:

    fastx_collapser -i 00_EC.fastq -o 00_EC_collapsed.fasta
    fastx_collapser -i 01_EC.fastq -o 01_EC_collapsed.fasta
    fastx_collapser -i 04_EC.fastq -o 04_EC_collapsed.fasta
    fastx_collapser -i 10_EC.fastq -o 10_EC_collapsed.fasta

The number of unique and total sequences were counted on the full set of collapsed files:

    batch_count_reads.py EC_collapsed

The results of this counts were:

    00_EC_collapsed.fasta
    Unique reads:	2087525
    Total reads:	3798445
    
    01_EC_collapsed.fasta
    Unique reads:	1877775
    Total reads:	8393542
    
    04_EC_collapsed.fasta
    Unique reads:	427544
    Total reads:	879841
    
    10_EC_collapsed.fasta
    Unique reads:	5471147
    Total reads:	18337128
    
    full_reads_EC_collapsed.fasta
    Unique reads:	9169355
    Total reads:	31408956

The full_reads_EC_collapsed.fasta was mapped against the whole sequences of the databases and reads not aligned were stored in the not_aligning directory, in the not_aligning.fasta file.

    mkdir not_aligning
    bowtie ../databases/zm_all_ok_dbs/ok_full_zm -f full_reads_EC_collapsed.fasta -v 1 --un not_aligning/not_aligning.fasta -p 12 tmp.bowtie
    rm tmp.bowtie

The output of the Bowtie program was:

    # reads processed: 9169355
    # reads with at least one reported alignment: 6900431 (75.26%)
    # reads that failed to align: 2268924 (24.74%)
    Reported 6900431 alignments to 1 output stream(s)

The sequences in the not_aligning.fasta file were blasted against the nt database to retrieve as many information for this reads. ######################################### NOT DONE YET ##################################

The not aligned reads were removed from the individual collapsed reads. The files created in these steps were named according to step they correspond secuentially (e.g. S1, S2, etc.).

    batch_remove_fasta_records.py not_aligning/not_aligning.fasta EC_collapsed Clean_S1

The output of the script was:

    00_EC_collapsed.fasta
    Unique reads removed:	335694
    Total reads removed:	547448
    
    01_EC_collapsed.fasta
    Unique reads removed:	744552
    Total reads removed:	2460632
    
    04_EC_collapsed.fasta
    Unique reads removed:	102802
    Total reads removed:	142222
    
    10_EC_collapsed.fasta
    Unique reads removed:	1146876
    Total reads removed:	2364115
    
    full_reads_EC_collapsed.fasta
    Unique reads removed:	2268924
    Total reads removed:	5514417

The sequences in the produced fasta files were counted to verify that the process went ok:

    batch_count_reads.py Clean_S1

The results were:

    00_Clean_S1.fasta
    Unique reads:	1751831
    Total reads:	3250997
    
    01_Clean_S1.fasta
    Unique reads:	1133223
    Total reads:	5932910
    
    04_Clean_S1.fasta
    Unique reads:	324742
    Total reads:	737619
    
    10_Clean_S1.fasta
    Unique reads:	4324271
    Total reads:	15973013
    
    full_reads_Clean_S1.fasta
    Unique reads:	6900431
    Total reads:	25894539

###snRNAs mapping reads removal.

The full_reads_Clean_S1.fasta file was mapped against the snRNAs database and the reads aligning were stored in the snRNAs directory, in the snRNAs.fasta file.

    mkdir snRNAs
    bowtie ../databases/zm_snRNAs/ok_snRNAs -f full_reads_Clean_S1.fasta -v 1 --al snRNAs/snRNAs.fasta -p 12 tmp.bowtie
    rm tmp.bowtie

The output of the Bowtie program was:

    # reads processed: 6900431
    # reads with at least one reported alignment: 9043 (0.13%)
    # reads that failed to align: 6891388 (99.87%)
    Reported 9043 alignments to 1 output stream(s)

The aligned reads were removed from the individual Clean_S1 files.

    batch_remove_fasta_records.py snRNAs/snRNAs.fasta Clean_S1 Clean_S2

The results of the script which corresponds to the number of snRNAs that may will be reported were:

    00_Clean_S1.fasta
    Unique reads removed:	5502
    Total reads removed:	24953
    
    01_Clean_S1.fasta
    Unique reads removed:	2351
    Total reads removed:	13431
    
    04_Clean_S1.fasta
    Unique reads removed:	702
    Total reads removed:	1596
    
    10_Clean_S1.fasta
    Unique reads removed:	2437
    Total reads removed:	15024
    
    full_reads_Clean_S1.fasta
    Unique reads removed:	9043
    Total reads removed:	55004

The sequences in the produced fasta files were counted to verify that the process went ok:

    batch_count_reads.py Clean_S2

The results were:

    00_Clean_S2.fasta
    Unique reads:	1746329
    Total reads:	3226044
    
    01_Clean_S2.fasta
    Unique reads:	1130872
    Total reads:	5919479
    
    04_Clean_S2.fasta
    Unique reads:	324040
    Total reads:	736023
    
    10_Clean_S2.fasta
    Unique reads:	4321834
    Total reads:	15957989
    
    full_reads_Clean_S2.fasta
    Unique reads:	6891388
    Total reads:	25839535

###snoRNAs mapping reads removal.

The full_reads_Clean_S2.fasta file was mapped against the snoRNAs database and the reads aligning were stored in the snoRNAs directory, in the snoRNAs.fasta file.

    mkdir snoRNAs
    bowtie ../databases/zm_snoRNAs/ok_snoRNAs -f full_reads_Clean_S2.fasta -v 1 --al snoRNAs/snoRNAs.fasta -p 12 tmp.bowtie
    rm tmp.bowtie

The output of the Bowtie program was:

    # reads processed: 6891388
    # reads with at least one reported alignment: 6809 (0.10%)
    # reads that failed to align: 6884579 (99.90%)
    Reported 6809 alignments to 1 output stream(s)


The aligned reads were removed from the individual Clean_S2 files.

    batch_remove_fasta_records.py snoRNAs/snoRNAs.fasta Clean_S2 Clean_S3

The results of the script which corresponds to the number of snoRNAs that may will be reported were:

    00_Clean_S2.fasta
    Unique reads removed:	3847
    Total reads removed:	15398
    
    01_Clean_S2.fasta
    Unique reads removed:	1735
    Total reads removed:	5055
    
    04_Clean_S2.fasta
    Unique reads removed:	1037
    Total reads removed:	2115
    
    10_Clean_S2.fasta
    Unique reads removed:	2133
    Total reads removed:	6969
    
    full_reads_Clean_S2.fasta
    Unique reads removed:	6809
    Total reads removed:	29537

The sequences in the produced fasta files were counted to verify that the process went ok:

    batch_count_reads.py Clean_S3

The results were:

    00_Clean_S3.fasta
    Unique reads:	1742482
    Total reads:	3210646
    
    01_Clean_S3.fasta
    Unique reads:	1129137
    Total reads:	5914424
    
    04_Clean_S3.fasta
    Unique reads:	323003
    Total reads:	733908
    
    10_Clean_S3.fasta
    Unique reads:	4319701
    Total reads:	15951020
    
    full_reads_Clean_S3.fasta
    Unique reads:	6884579
    Total reads:	25809998

###tRNAs mapping reads removal.

The full_reads_Clean_S3.fasta file was mapped against the tRNAs database and the reads aligning were stored in the tRNAs directory, in the tRNAs.fasta file.

    mkdir tRNAs
    bowtie ../databases/zm_tRNAs/ok_tRNAs -f full_reads_Clean_S3.fasta -v 1 --al tRNAs/tRNAs.fasta -p 12 tmp.bowtie
    rm tmp.bowtie

The output of the Bowtie program was:

    # reads processed: 6884579
    # reads with at least one reported alignment: 24012 (0.35%)
    # reads that failed to align: 6860567 (99.65%)
    Reported 24012 alignments to 1 output stream(s)

The aligned reads were removed from the individual Clean_S2 files.

    batch_remove_fasta_records.py tRNAs/tRNAs.fasta Clean_S3 Clean_S4

The results of the script which corresponds to the number of tRNAs that may will be reported were:

    00_Clean_S3.fasta
    Unique reads removed:	10853
    Total reads removed:	322110
    
    01_Clean_S3.fasta
    Unique reads removed:	7790
    Total reads removed:	154150
    
    04_Clean_S3.fasta
    Unique reads removed:	2157
    Total reads removed:	11932
    
    10_Clean_S3.fasta
    Unique reads removed:	9391
    Total reads removed:	125789
    
    full_reads_Clean_S3.fasta
    Unique reads removed:	24012
    Total reads removed:	613981

The sequences in the produced fasta files were counted to verify that the process went ok:

    batch_count_reads.py Clean_S4

The results were:

    00_Clean_S4.fasta
    Unique reads:	1731629
    Total reads:	2888536
    
    01_Clean_S4.fasta
    Unique reads:	1121347
    Total reads:	5760274
    
    04_Clean_S4.fasta
    Unique reads:	320846
    Total reads:	721976
    
    10_Clean_S4.fasta
    Unique reads:	4310310
    Total reads:	15825231
    
    full_reads_Clean_S4.fasta
    Unique reads:	6860567
    Total reads:	25196017

###rRNAs mapping reads removal.

The full_reads_Clean_S4.fasta file was mapped against the rRNAs database and the reads aligning were stored in the rRNAs directory, in the rRNAs.fasta file.

    mkdir rRNAs
    bowtie ../databases/zm_rRNAs/ok_rRNAs -f full_reads_Clean_S4.fasta -v 1 --al rRNAs/rRNAs.fasta -p 12 tmp.bowtie
    rm tmp.bowtie

The output of the Bowtie program was:

    # reads processed: 6860567
    # reads with at least one reported alignment: 217195 (3.17%)
    # reads that failed to align: 6643372 (96.83%)
    Reported 217195 alignments to 1 output stream(s)


The aligned reads were removed from the individual Clean_S4 files.

    batch_remove_fasta_records.py tRNAs/tRNAs.fasta Clean_S4 Clean_S5

The results of the script which corresponds to the number of rRNAs that may will be reported were:

    00_Clean_S4.fasta
    Unique reads removed:	60782
    Total reads removed:	723126
    
    01_Clean_S4.fasta
    Unique reads removed:	122488
    Total reads removed:	3717938
    
    04_Clean_S4.fasta
    Unique reads removed:	31868
    Total reads removed:	196498
    
    10_Clean_S4.fasta
    Unique reads removed:	79225
    Total reads removed:	1016624
    
    full_reads_Clean_S4.fasta
    Unique reads removed:	217195
    Total reads removed:	5654186

The sequences in the produced fasta files were counted to verify that the process went ok:

    batch_count_reads.py Clean_S5

The results were:

    00_Clean_S5.fasta
    Unique reads:	1670847
    Total reads:	2165410
    
    01_Clean_S5.fasta
    Unique reads:	998859
    Total reads:	2042336
    
    04_Clean_S5.fasta
    Unique reads:	288978
    Total reads:	525478
    
    10_Clean_S5.fasta
    Unique reads:	4231085
    Total reads:	14808607
    
    full_reads_Clean_S5.fasta
    Unique reads:	6643372
    Total reads:	19541831

##Clean reads graphical representation.

The frecuency of the clean reads was determined with the following command:

    batch_count_sizes.py Clean_S5 -e full

The results of this command were:

    	00_Clean_S5.fasta
    18	82083
    19	160630
    20	200686
    21	340594
    22	410773
    23	335419
    24	619093
    25	14473
    26	1286
    27	373
    
    	01_Clean_S5.fasta
    18	103915
    19	94382
    20	104707
    21	350359
    22	540722
    23	128886
    24	701335
    25	10649
    26	3532
    27	3849
    
    	04_Clean_S5.fasta
    18	72823
    19	28828
    20	56936
    21	103642
    22	161384
    23	17417
    24	82087
    25	1621
    26	403
    27	337
    
    	10_Clean_S5.fasta
    18	74907
    19	153779
    20	457102
    21	2832701
    22	3859345
    23	685593
    24	6537412
    25	185042
    26	13978
    27	8748

This data was saved in a table format on the file Clean_sizes.csv, the reads per million values were calculated and saved in table format on the file Clean_RPM_sizes.csv.

The plot to represent this data was generated with the follwing R code:

    library(RColorBrewer)
    
    bitmap('RNA_sizes.png',width = 7, height = 4, units = 'in', res = 300)
    options(scipen=999)
    Sizes=c(18:27)
    Samples=c("Immature embryos", "1 month callus", "4 months callus", "10 months callus")
    d=read.table('Clean_RPM_sizes.csv', header=T, row.names = 1)
    d=t(d)
    prop = prop.table(as.matrix(d), margin=1)
    prop = prop*100
    rowSums(prop)
    
    
    par(mar=c(4.5, 4, 1.5, 1), xpd=TRUE)
    barplot(as.matrix(d), col=brewer.pal(length(rownames(d)), "Accent"), width=2, ylab='Reads per million', beside=TRUE,xaxt="n", xlab='Length of small RNAs')
    legend("top",inset=c(-0.05,0), fill=brewer.pal(length(rownames(prop)), "Accent"), legend=Samples)
    axis(1,at=c(6,16,26,36,46,56,66,76,86,96), labels=as.character(Sizes))
    
    dev.off()
