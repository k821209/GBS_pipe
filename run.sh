parallel -j 4 "bwa mem -t1 -B9 -O16 -L5 ../../ref/Enzyme_site_block_ApeKI.txt.fa {1}_1.fastq.gz {1}_2.fastq.gz | sambamba view -f bam -o {1}.bam -S /dev/stdin" :::: samples
# samtools mpileup -t DP,AD,ADF,ADR,SP -g -o sortedbamfiles.bcf -b sortedbamfiles -f ./ref/Enzyme_site_block_ApeKI.txt.fa -I
# bcftools call -mv -o sortedbamfiles.mv.vcf sortedbamfiles.bcf


## samtools mpileup -g -o bamfiles.bcf -b bamfiles -f ../../ref/Enzyme_site_block_ApeKI.txt.fa -I 
