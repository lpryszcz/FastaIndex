# FastaIndex

FastA index (.fai) handler compatible with samtools faidx (http://www.htslib.org/doc/faidx.html).
.fai is extended with 4 columns storing counts for A, C, G & T for each sequence.

# Usage

## Dependencies
- Python 2.7

## Parameters

```
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         verbose
  -i FASTA, --fasta FASTA
                        FASTA file(s)
  -o OUT, --out OUT     output stream	 [stdout]
  -r [REGIONS [REGIONS ...]], --regions [REGIONS [REGIONS ...]]
                        contig or contig region to output (returns reverse complement if end larger than start)
  -N N                  calculate NXX and exit ie N50
  -L L                  calculate LXX and exit ie L50
  -S, --stats           return FastA stats aka fasta_stats
```

## Examples
```
# retrieve sequence of scaffold00001 starting at 100 and ending at 200 base (0-based)
FastaIndex -i contigs.fa -r 'scaffold00001:100-200'

# retrieve reverse complement of the same region
FastaIndex -i contigs.fa -r 'scaffold00001:100-200'

# statistics of FastA file
FastaIndex -i contigs.fa -S
# or
fasta_stats -i contigs.fa
```

## Installation
```
sudo pip install -U FastaIndex
```