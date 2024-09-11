#!/bin/bash
 
#SBATCH --mem=64g
#SBATCH --time=24:00:00



cmd += ' --export=CLADE="' + c + '"'
                cmd += ',MUT="' + mut + '"'
                cmd += ',ALPHA="' + str(alpha) + '"'
                cmd += ',BETA="' + str(beta) + '"'
                cmd += ',INPUT="' + path_raw + '"'
                cmd += ',SAMPLES="' + str(num_samples) + '"'
 
EPS=10
DELTA=0.8
COEF=10
NUM_SAMPLES=10000
CLADE="$CLADE"
MUT="$MUT"
ALPHA="$ALPHA"
BETA="$BETA"
INPUT="$INPUT"
SAMPLES="$SAMPLES"
 
source myconda
mamba activate partition

 
(time (python /home/bridgersjd/trisicell/scripts/partf_scripts/run.py --eps ${EPS} --delta ${DELTA} --coef ${COEF} --num_samples ${SAMPLES} --clade ${CLADE} --mutation ${MUT} --alpha ${ALPHA} --beta ${BETA} --patherror ${INPUT} > ~/trisicell/results/partfRes_${MUT}_${CLADE}_${NUM_SAMPLES}_${EPS}_${DELTA}_${COEF}_${SLURM_JOB_ID}.txt)) 2> ~/trisicell/results/time_${CLADE}_${NUM_SAMPLES}_${EPS}_${DELTA}_${COEF}_${SLURM_JOB_ID}.txt