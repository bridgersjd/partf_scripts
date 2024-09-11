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

    output = "number of samples = " + str(num_samples) + "\n"

    

    red_minus_c13 = ["C20","C7","C8","C16","C11","C15","C18"]
    red = ["C20","C7","C8","C16","C11","C15","C18","C13"]
    green = ["C23", "C17", "C12", "C10", "C14", "C3"] + ["C19"]
    blue = ["C6", "C21", "C24", "C9"]
    blue_with_c19 = blue + ["C19"]
    orange = ["C22", "C4", "C1"]
    two_and_five = ["C2", "C5"]


    cells = None
    all_cells = list(df_corrected.index)
    if args.clade == "red":
        cells = red
    elif args.clade == "green":
        cells = green
    elif args.clade == "blue":
        cells = blue
    elif args.clade == "orange":
        cells = orange
    else:
        cells = list(set(all_cells) - set(two_and_five))

    
    clade = {cell : 0 for cell in all_cells}
    clade.update({c : 1 for c in cells})

    

    muts = muts[args.mutation]

    names_to_cells = list(df.index)

    # print("\ndelta = " + str(delta) + " divide=" + str(divide) + " epsilon=" + str(eps) + " gamma (coef)=" + str(coef))
    pf = trisicell.tl.partition_function(df_input=df, alpha=alpha, beta=beta, n_samples=num_samples, n_batches=1, muts=muts, cells=cells, names_to_cells=names_to_cells,eps = eps, delta=delta, divide=divide, coef=coef)
    # output += str(cells) + "\n" + str(pf) + "\n\n"

    output = args.patherror + "," + str(args.alpha) + "," + str(args.beta) + "," + args.clade + "," + args.num_samples + "," + args.mutation
    output += "," + str(pf)


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
    parser.add_argument("-C", "--clade", type=str,                                                        
                        help="major clade", required=True)
    parser.add_argument("-m", "--mutation", type=str,                                                        
                        help="mutation", required=True)
    parser.add_argument("-a", "--alpha", type=float,                                                        
                        help="alpha (fp)", required=True)
    parser.add_argument("-b", "--beta", type=float,                                                        
                        help="beta (fn)", required=True)
    
    
    main(parser.parse_args())
