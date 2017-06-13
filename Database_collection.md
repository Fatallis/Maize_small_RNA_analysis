# Small RNAs expression Analysis on Zea mays embryogenic callus.
This file describe the database collection for the analysis of the illumina small RNAs libraries from maize embryogenic callus.

## Database collection and preparation.
### Ensembl Genomic Features.
We created an specific folder to work in and entered to it to begin the process:

    mkdir zm_databases
    cd zm_databases
We downloaded the Ensembl Zea mays release 32 DNA toplevel dataset:

    wget ftp://ftp.ensemblgenomes.org/pub/release-32/plants/fasta/zea_mays/dna/Zea_mays.AGPv4.dna.toplevel.fa.gz
We also downloaded the annotation gtf and gff3 files:

    wget ftp://ftp.ensemblgenomes.org/pub/release-32/plants/gtf/zea_mays/Zea_mays.AGPv4.32.gtf.gz
    wget ftp://ftp.ensemblgenomes.org/pub/plants/release-32/gff3/zea_mays/Zea_mays.AGPv4.32.gff3.gz
The files were decompressed with the following command:

    gunzip *.gz
Data was retrieved on 05/sep/2016.

The fasta files corresponding to the genomic features annotated on the gtf and gff3 files were obtained with the bedtools software v2.25.0 using the following commands:

    bedtools getfasta -name -split -s -fi Zea_mays.AGPv4.dna.toplevel.fa -bed Zea_mays.AGPv4.32.gtf -fo gtf.fa
    bedtools getfasta -name -split -s -fi Zea_mays.AGPv4.dna.toplevel.fa -bed Zea_mays.AGPv4.32.gff3 -fo gff3.fa

The gtf.fa and gff3.fa files, were then processed to extract the sequences of the different genomic features annotated, we used the python script sort_fasta.py entering the following commands:

    sort_fasta.py gtf.fa
    sort_fasta.py gff3.fa
The sort_fasta.py script can be found [here.](https://github.com/Fatallis/Small_RNA_analysis/blob/master/python/sort_fasta.py)

The results of this script are the corresponding CDS, exon, five_prime_UTR, gene, miRNA, miRNA_gene, repeat_region, three_prime_UTR, transcript, start_codon, and stop_codon fasta files. The start_codon and stop_codon files were deleted because they will not be used in the further analysis. The other files were moved to the corresponding database.

### Maize genome.

We copied the Ensembl Zea mays release 32 to the zm_genome directory.

    mkdir zm_genome
    cp Zea_mays.AGPv4.dna.toplevel.fa zm_genome

### Transcripts database.

We copied the files obtained in the 'Ensembl Genomic Features' step corresponding to the 'transcript' category to the zm_transcripts directory:
    mkdir zm_transcripts
    mv *transcript.* zm_transcripts/

We downloaded the Ensembl Zea mays release 32 cDNA dataset:

    cd zm_transcripts
    wget ftp://ftp.ensemblgenomes.org/pub/release-32/plants/fasta/zea_mays/cdna/Zea_mays.AGPv4.cdna.all.fa.gz
    gunzip *.gz

Data retrieved on 05/sep/2016

### Coding Sequences (CDS) database.

We copied the files obtained in the 'Ensembl Genomic Features' step corresponding to the 'CDS' category to the zm_CDSs directory:

    mkdir zm_CDSs
    mv *CDS* zm_CDSs/

We downloaded the Ensembl Zea mays release 32 CDS dataset:

    cd zm_CDSs
    wget ftp://ftp.ensemblgenomes.org/pub/release-32/plants/fasta/zea_mays/cds/Zea_mays.AGPv4.cds.all.fa.gz
    gunzip *.gz

Data was retrieved on 05/sep/2016

### Exons database.

We copied the files obtained in the 'Ensembl Genomic Features' step corresponding to the 'Exons' category to the zm_exons directory:

    mkdir zm_exons
    mv *exon* zm_exons/

### 5' UTRs database.

We copied the files obtained in the 'Ensembl Genomic Features' step corresponding to the 'Five prime UTRs' category to the zm_five_prime_utrs directory:

    mkdir zm_five_prime_utrs
    mv *five* zm_five_prime_utrs/

### 3' UTRs database.

We copied the files obtained in the 'Ensembl Genomic Features' step corresponding to the 'Three prime UTRs' category to the zm_three_prime_utrs directory:

    mkdir zm_three_prime_utrs
    mv *three* zm_three_prime_utrs/

### miRNAs database.

We copied the files obtained in the 'Ensembl Genomic Features' step corresponding to the 'miRNAs' category to the zm_miRNAs directory:

    mkdir zm_miRNAs
    mv *miRNA* zm_miRNAs/

We downloaded the miRNA datasets from miRBase release 21 (http://www.mirbase.org/).

    cd zm_miRNAs/
    wget ftp://mirbase.org/pub/mirbase/CURRENT/mature.fa.gz
    wget ftp://mirbase.org/pub/mirbase/CURRENT/hairpin.fa.gz
    wget ftp://mirbase.org/pub/mirbase/CURRENT/organisms.txt.gz
    gunzip *.gz

Data was retrieved on 05/sep/2016

The sequences belonging to maize were filtered with the following commands:

    filter_miRNAs.py -o organisms.txt mature.fa zma -f zm_mature.fa
    filter_miRNAs.py -o organisms.txt hairpin.fa zma -f zm_hairpin.fa

The sequences belonging to plants were filtered with the following command:

    filter_miRNAs.py -t organisms.txt mature.fa Viridiplantae -f plants_mature.fasta

The mature.fa, hairpin.fa and organisms.txt files were deleted.

    rm mature.fa hairpin.fa organisms.txt
The filter_miRNAs.py script can be found [here.](https://github.com/Fatallis/Small_RNA_analysis/blob/master/python/filter_miRNAs.py)

### lincRNAs database.

We copied the files obtained in the 'Ensembl Genomic Features' step corresponding to the 'lincRNAs' category to the zm_lincRNAs directory:

    mkdir zm_lincRNAs
    mv *lincRNA* zm_lincRNAs/

### tRNAs database.

We copied the files obtained in the 'Ensembl Genomic Features' step corresponding to the 'tRNAs' category to the zm_tRNAs directory:

    mkdir zm_tRNAs
    mv *tRNA* zm_tRNAs/

We downloaded the GtRNAdb Zea mays section.

    wget http://gtrnadb.ucsc.edu/genomes/eukaryota/Zmays5/zeaMay5-tRNAs.fa -O maize_tRNAs.fa

Data was retrieved on 05/sep/2016

### rRNAs database.

We navigated to the SILVA rRNA database release 126 homepage (<http://www.arb-silva.de/>) and on the search section, selected the SSU r126 Database; entered "Zea mays" on the organism name field and clicked the "Search" button, all the results were downloaded as a fasta without gaps file and saved as silva126_ssu.fasta. The same procedure was followed selecting the LSU r126 database instead. All the results were downloaded and saved as silva126_lsu.fasta. Data retrieved on 05/sep/2016.

    tar -xvzf silva126_ssu.fasta.tgz
    tar -xvzf silva126_lsu.fasta.tgz

The extracted fasta files were renamed accordingly as silva126_ssu.fa and silva126_lsu.fa. The commands to do this step are not showed to avoid confusion due to the fact that the extracted files have names including the id ot the session used to download them and therefore the name is different each time the files are downloaded.

We navigated to <http://combio.pl/rrna/> and then clicked on "Search" button and searched for Zea mays. The results were saved as 5S.fa. Data retrieved on 05/sep/2016.
We navigated to the PhytoREF version 1.1 homepage (<http://5.196.17.195/phytoref/index.php>) and on the "Search & Downloads" section selected the "Genus" option and entered "Zea". The results were saved in a fasta file named: 16S.fa. Data retrieved on 17/11/2015.

### snoRNAs database.

We navigated to the Plant snoRNA Database version 1.2 and in the "Sequences" option (<http://bioinf.scri.sari.ac.uk/cgi-bin/plant_snorna/get-sequences>) selected all the "Zea mays" corresponding sequences (those starting with "Zm"). The results were saved in the file snoRNAs.fa.

Data was retrieved on 05/sep/2016

### snRNAs database.

We navigated to the Splicing Related Gene Database <http://www.plantgdb.org/SRGD/ASRG/ShowRNA.php> and selected all the elements of the list of Arabidospsis genes corresponding to the snRNAs and save them in the snRNAs.fasta file.

Data was retrieved on 05/sep/2016

### Repeats database.

The file containing the Maize Repeats was downloaded executing the following command:

    mkdir zm_repeats
    cd zm_repeats/
    wget ftp://ftp.plantbiology.msu.edu/pub/data/TIGR_Plant_Repeats/TIGR_Zea_Repeats.v3.0 -O maize_repeats_TIGR.fa

The maize transposable elements database was downloaded:

    wget http://maizetedb.org/~maize/TE_12-Feb-2015_15-35.fa -O maize_repeats_maizeTEDB.fa

The PGSB Plant Genome and Systems Biology database was downloaded:

    wget ftp://ftpmips.helmholtz-muenchen.de/plants/REdat/mipsREdat_9.3p_Poaceae_TEs.fasta.gz
    gunzip *.gz

Data was retrieved on 05/sep/2016

The sequences corresponding to maize from the PGSB database were filtered with the following command:

    filter_by_name.py mipsREdat_9.3p_Poaceae_TEs.fasta maize_repeats_PGSB.fa Zea
The filter_by_name.py script can be found [here.](https://github.com/Fatallis/Small_RNA_analysis/blob/master/python/filter_by_name.py)

### tasiRNAs database.

We retrieved the cDNA sequences from Ensembl Maize Genome AGPv3.29 of transcripts of TAS3 genes as reported in:

Dotto, M. C., Petsch, K. A., Aukerman, M. J., Beatty, M., Hammell, M., & Timmermans, M. C. P. (2014). Genome-Wide Analysis of leafbladeless1-Regulated and Phased Small RNAs Underscores the Importance of the TAS3 ta-siRNA Pathway to Maize Development. PLoS Genetics, 10(12), e1004826. doi:10.1371/journal.pgen.1004826

The gene IDs for these TAS3 genes are listed here:

GRMZM2G178686
GRMZM2G020468
GRMZM2G084821
GRMZM2G124744
GRMZM5G806469
GRMZM2G155490
GRMZM2G082055
GRMZM2G588623
GRMZM2G512113

The sequences were saved in the file tasiRNAs.fasta.

Data was retrieved on 17/11/2015

### RFAM

The RF files containing Zea mays sequences were searched on the PFAM website <http://rfam.xfam.org/>.
The accession numbers of the files were manually added to the files: miRNAs.rna, mixedRNAs.rna, rRNAs.rna, snoRNAs.rna  snRNAs.rna, tRNAs.rna. The mixedRNAs.rna files contained those RNAs which were difficult to fit in a single definite category.

The accession number of those files were saved on the Databases.txt file. And then the files were downloaded to the Rfam directory and uncompressed:

    while read p; do
	   wget ftp://ftp.ebi.ac.uk/pub/databases/Rfam/12.1/fasta_files/$p.fa.gz
    done < Databases.txt
    gunzip *.gz
    
Data was retrieved on 05/sep/2016

Then the files corresponing to Zea mays were extracted from the downloaded files.

    for fasta in  *.fa; do
	   filter_by_name.py $fasta zm_$fasta Zea;
    done
The filter_by_name.py script can be found [here.](https://github.com/Fatallis/Small_RNA_analysis/blob/master/python/filter_by_name.py)

And then were moved to the corresponding directory according with its classification:

    move_rfams.py
The move_rfams.py script can be found [here.](https://github.com/Fatallis/Small_RNA_analysis/blob/master/python/move_rfams.py)

The following command was executed to concatenate the different files corresponding to each database, transform RNA to DNA and collapse them to avoid duplicate sequences.

    batch_fasta_cat.py
The batch_fasta_cat.py script can be found [here.](https://github.com/Fatallis/Small_RNA_analysis/blob/master/python/batch_fasta_cat.py) and requires the fasta_cat.py script which can be found [here.](https://github.com/Fatallis/Small_RNA_analysis/blob/master/python/fasta_cat.py)

As a result of the command execution:
* The transcript sequences were concentrated in a unique file ok_transcripts.fasta.
* The coding sequences were concentrated in a unique file ok_CDSs.fasta.
* The exon sequences were concentrated in a unique file ok_exons.fasta.
* The 5' UTR sequences were concentrated in a unique file ok_five_primes.fasta.
* The 3' UTR sequences were concentrated in a unique file ok_three_primes.fasta.
* The miRNAs sequences were converted to DNA sequences and concentrated in a unique file ok_miRNAs.fasta.
* The lincRNAs sequences were concentrated in a unique file ok_lincRNAs.fasta.
* The tRNAs sequences were concentrated in a unique file ok_tRNAs.fasta.
* The rRNAs sequences were concentrated in a unique file ok_rRNAs.fasta.
* The snoRNAs sequences were concentrated in a unique file ok_snoRNAs.fasta.
* The snRNAs sequences were concentrated in a unique file ok_snRNAs.fasta.
* The repeats sequences were concentrated in a unique file ok_repeats.fasta.
* The tasiRNAs sequences were concentrated in a unique file ok_tasiRNAs.fasta.

### Global database

A global database was created including all the sequences on the previous databases plus the sequences on the toplevel maize genome version (Ensembl 32). 

The sequences of all the "ok" databases were copied to the zm_all_ok_dbs directory:

    find . -name "ok*.fasta" -exec cp {} zm_all_ok_dbs/ \;
    
The genome fasta file also was copied to this directory and changed the extension from fa to fasta:

    cp Zea_mays.AGPv4.dna.toplevel.fa zm_all_ok_dbs/
    mv zm_all_ok_dbs/Zea_mays.AGPv4.dna.toplevel.fa zm_all_ok_dbs/Zea_mays.AGPv4.dna.toplevel.fasta

All those files were concatenated to a single file. The "ok" files were deleted and the remaining file renamed as ok_full_zm.fasta

    cat zm_all_ok_dbs/*.fasta > zm_all_ok_dbs/tmp.fa
    rm zm_all_ok_dbs/*.fasta
    mv zm_all_ok_dbs/tmp.fa zm_all_ok_dbs/ok_full_zm.fasta

### Bowtie indexes

Bowtie index files were created in order to use the databases with the bowtie program.
Bowtie indexes were built for each ok_file in the different directories:

    bowtie_index.py
    
The bowtie_index.py script can be found [here.](https://github.com/Fatallis/Small_RNA_analysis/blob/master/python/bowtie_index.py)
