import pandas as pd
import os

def main():
    folder = "/home/bridgersjd/trisicell/scripts_new/partf_scripts/Sep9Matrices/"

    files_raw = [
        "D-no_correction.tsv",
        "D-C19_corrected.tsv",
        "D-C19_and_C2C5_corrected.tsv"
    ]

    files_corrected = [
        "E-no_correction-fp_0.001-fn_0.075.tsv", 
        "E-C19_corrected-fp_0.001-fn_0.075.tsv", 
        "E-C19_and_C2C5_corrected-fp_0.0001-fn_0.075.tsv"
    ]

    num_samples = 10000

    all_cells = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24"]
    red = ["C20","C7","C8","C16","C11","C15","C18","C13"]
    green_no_19 = ["C23", "C17", "C12", "C10", "C14", "C3"]
    green_w_19 = green_no_19 + ["C19"]
    blue_no_19 = ["C6", "C21", "C24", "C9"]
    blue_w_19 = blue_no_19 + ["C19"]
    orange = ["C22", "C4", "C1"]
    two_and_five = ["C2", "C5"]
    not_two_and_five = list(set(all_cells) - set(two_and_five))

    alphas = [0.001, 0.0001]
    betas = [0.075]
    seeds = [0,1,2,3,4,5]


    for i in [0,1,2]:
        # 0 - no correction, 1 - C19 corrected, 2 - both corrections
        clades = None
        if i == 0:
            clades = [red, blue_w_19, green_no_19, orange, not_two_and_five]
        elif i == 1:
            clades = [red, blue_no_19, green_w_19, orange, not_two_and_five]
        else:
            clades = [red, blue_no_19, green_w_19, orange]

        for c in clades:
            path_raw = folder + files_raw[i]
            path_corrected = folder + files_corrected[i]


            df_corrected = pd.read_csv(path_corrected, sep="\t", index_col=[0]).sort_values(by=["cell_id_x_mut_id"])

            cells = "_".join(c)
            all_cells = list(df_corrected.index)

            clade = {cell : 0 for cell in all_cells}
            clade.update({x : 1 for x in c})

            muts = []
            for col in df_corrected.columns:
                if dict(df_corrected[col]) == clade:
                    muts += [col]

            for mut in muts:
                for seed in seeds:
                    for alpha in alphas:
                        for beta in betas:
                            cmd = "sbatch"
                            cmd += ' --job-name="' + 'job_partf.' + str(i) + '.' + cells + '.' + mut + '.' + str(alpha) + '.' + str(beta) + '"'
                            cmd += ' --output="' + 'job_partf.' + str(i) + '.' + cells + '.' + mut + '.' + str(alpha) + '.' + str(beta) + '.%j.out"'
                            cmd += ' --error="' + 'job_partf.' + str(i) + '.' + cells + '.' + mut + '.' + str(alpha) + '.' + str(beta) + '.%j.err"'
                            cmd += ' --export=CELLS="' + cells + '"'
                            cmd += ',MUT="' + mut + '"'
                            cmd += ',ALPHA="' + str(alpha) + '"'
                            cmd += ',BETA="' + str(beta) + '"'
                            cmd += ',SEED="' + str(seed) + '"'
                            cmd += ',INPUT="' + path_raw + '"'
                            cmd += ',SAMPLES="' + str(num_samples) + '"'
                            cmd += ' run_partf.sbatch'
                            os.system(cmd)
                            print(cmd)

if __name__ == "__main__":
    main()
