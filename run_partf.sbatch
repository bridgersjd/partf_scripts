#!/bin/bash
 
#SBATCH --mem=2g
#SBATCH --time=1:00:00
 
EPS=10
DELTA=0.8
COEF=10

CLADE="$CLADE"
MUT="$MUT"
ALPHA="$ALPHA"
BETA="$BETA"
SEED="$SEED"
INPUT="$INPUT"
SAMPLES="$SAMPLES"
 
source myconda
mamba activate partition

python /home/bridgersjd/trisicell/scripts_new/partf_scripts/run.py --eps ${EPS} --delta ${DELTA} --coef ${COEF} --num_samples ${SAMPLES} --cells "${CELLS}" --mutation ${MUT} --alpha ${ALPHA} --beta ${BETA} --seed ${SEED} --patherror ${INPUT}
