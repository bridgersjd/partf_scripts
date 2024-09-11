import pandas as pd

def main():
    folder = "/Users/john/Desktop/matrices/Sep9Matrices/"

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

    num_samples = 1000

    clades = ["green", "blue", "orange", "red", "notC2C5"]
    for c in clades:
        for i in [0,1,2]:
            path_raw = folder + files_raw[i]
            path_corrected = folder + files_corrected[i]
            alpha = None
            beta = None
            if i == 0 or i == 1:
                alpha = 0.001
                beta = 0.075
            else:
                alpha = 0.0001
                beta = 0.075


            df_corrected = pd.read_csv(path_corrected, sep="\t", index_col=[0]).sort_values(by=["cell_id_x_mut_id"])

            red = ["C20","C7","C8","C16","C11","C15","C18","C13"]
            green = ["C23", "C17", "C12", "C10", "C14", "C3"] + ["C19"]
            blue = ["C6", "C21", "C24", "C9"]
            orange = ["C22", "C4", "C1"]
            two_and_five = ["C2", "C5"]


            cells = None
            all_cells = list(df_corrected.index)
            if c == "red":
                cells = red
            elif c == "green":
                cells = green
            elif c == "blue":
                cells = blue
            elif c == "orange":
                cells = orange
            else:
                cells = list(set(all_cells) - set(two_and_five))

            
            clade = {cell : 0 for cell in all_cells}
            clade.update({c : 1 for c in cells})

            muts = []
            for col in df_corrected.columns:
                if dict(df_corrected[col]) == clade:
                    muts += [col]

            for mut in muts:
                cmd = "sbatch"
                cmd += ' --job-name="' + 'partf.' + str(i) + '.' + c + '.' + mut + '"'
                cmd += ' --output="' + 'partf.' + str(i) + '.' + c + '.' + mut + '.%j.out"'
                cmd += ' --error="' + 'partf.' + str(i) + '.' + c + '.' + mut + '.%j.err"'
                cmd += ' --export=CLADE="' + c + '"'
                cmd += ',MUT="' + mut + '"'
                cmd += ',ALPHA="' + str(alpha) + '"'
                cmd += ',BETA="' + str(beta) + '"'
                cmd += ',INPUT="' + path_raw + '"'
                cmd += ',SAMPLES="' + str(num_samples) + '"'
                cmd += ' run_partf.sbatch'
                print(cmd)


if __name__ == "__main__":
    main()