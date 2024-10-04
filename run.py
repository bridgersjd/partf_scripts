import trisicell
import pandas as pd
import argparse

def main(args):
    path = args.patherror

    df = trisicell.io.read(path)
    
    alpha=args.alpha
    beta=args.beta

    divide = True
    num_samples = args.num_samples
    delta = args.delta
    eps = args.eps
    coef = args.coef
    seed = args.seed

    output = "number of samples = " + str(num_samples) + "\n"
    cells = sorted(args.cells.split("_"))

    all_cells = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24"]
    clade = {cell : 0 for cell in all_cells}
    clade.update({c : 1 for c in cells})

    

    muts = [args.mutation]

    names_to_cells = list(df.index)

    # print("\ndelta = " + str(delta) + " divide=" + str(divide) + " epsilon=" + str(eps) + " gamma (coef)=" + str(coef))
    pf = trisicell.tl.partition_function(df_input=df, alpha=alpha, beta=beta, n_samples=num_samples, n_batches=1, muts=muts, cells=cells, names_to_cells=names_to_cells,eps = eps, delta=delta, divide=divide, coef=coef, my_seed=seed)
    # output += str(cells) + "\n" + str(pf) + "\n\n"

    output = args.patherror + "\t" + str(args.alpha) + "\t" + str(args.beta) + "\t" + ",".join(cells) + "\t" + str(args.num_samples) + "\t" + args.mutation
    output += "\t" + str(pf[0].iloc[0][0]) + "\t" + str(pf[0].iloc[0][1])
    print(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='run.py')

    parser.add_argument("-pe", "--patherror", type=str,                                                        
                        help="input genotype matrix", required=True)
    parser.add_argument("-e", "--eps", type=float,                                                        
                        help="epsilon", required=True)
    parser.add_argument("-d", "--delta", type=float,                                                        
                        help="delta", required=True)
    parser.add_argument("-c", "--coef", type=float,                                                        
                        help="coef", required=True)
    parser.add_argument("-n", "--num_samples", type=int,                                                        
                        help="num_samples", required=True)
    parser.add_argument("-C", "--cells", type=str,                                                        
                        help="cells (comma sep)", required=True)
    parser.add_argument("-m", "--mutation", type=str,                                                        
                        help="mutation", required=True)
    parser.add_argument("-a", "--alpha", type=float,                                                        
                        help="alpha (fp)", required=True)
    parser.add_argument("-b", "--beta", type=float,                                                        
                        help="beta (fn)", required=True)
    parser.add_argument("-s", "--seed", type=int,                                                        
                        help="random seed", required=True)
    
    
    main(parser.parse_args())
