import argparse

# python generatingMethodsBatchshell.py
# python generatingMethodsBatchshell.py --imputeMode
parser = argparse.ArgumentParser(description='Generating sbatch files for HPC cluster running')
parser.add_argument('--outputDir', type=str, default='',
                    help='Directory of batch files for cluster running')
parser.add_argument('--imputeMode', action='store_true', default=False,
                    help='whether impute')
args = parser.parse_args()

templateStr1 = "#! /bin/bash\n"\
"######################### Batch Headers #########################\n"\
"#SBATCH -A xulab\n"\
"#SBATCH -p BioCompute               # use the BioCompute partition\n"\
"#SBATCH -J "

templateStr2 = "\n#SBATCH -o results-%j.out           # give the job output a custom name\n"\
"#SBATCH -t 2-00:00                  # two days time limit\n"\
"#SBATCH -N 1                        # number of nodes\n"\
"#SBATCH -n 8                        # number of cores (AKA tasks)\n"\
"#SBATCH --mem=128G\n"\
"#################################################################\n"\
"module load miniconda3\n"\
"source activate conda_R\n"

#tuple list
#batchInfo,scGNNparam,outDir
methodsList = [
    ('run_experiment_1_g_b E1gb','--EMtype EM --useBothembedding --npyDir','npyG1B/'),
    ('run_experiment_1_g_e E1ge','--EMtype EM --useGAEembedding --npyDir','npyG1E/'),
    ('run_experiment_1_g_f E1gf','--EMtype EM --npyDir','npyG1F/'),
    ('run_experiment_1_r_b E1rb','--EMtype EM --useBothembedding --npyDir','npyR1B/'),
    ('run_experiment_1_r_e E1re','--EMtype EM --useGAEembedding --npyDir','npyR1E/'),
    ('run_experiment_1_r_f E1rf','--EMtype EM --npyDir','npyR1F/'),
    ('run_experiment_1_n_e E1nb','--regulized-type noregu --EMtype EM --useBothembedding --npyDir','npyN1B/'),
    ('run_experiment_1_n_e E1ne','--regulized-type noregu --EMtype EM --useGAEembedding --npyDir','npyN1E/'),
    ('run_experiment_1_n_f E1nf','--regulized-type noregu --EMtype EM --npyDir','npyN1F/'),
    ('run_experiment_2_g_b E2gb','--EMtype celltypeEM --useBothembedding  --npyDir','npyG2B/'),
    ('run_experiment_2_g_e E2ge','--EMtype celltypeEM --useGAEembedding  --npyDir','npyG2E/'),
    ('run_experiment_2_g_f E2gf','--EMtype celltypeEM --npyDir','npyG2F/'),
    ('run_experiment_2_r_b E2rb','--EMtype celltypeEM --useBothembedding  --npyDir','npyR2B/'),
    ('run_experiment_2_r_e E2re','--EMtype celltypeEM --useGAEembedding  --npyDir','npyR2E/'),
    ('run_experiment_2_r_f E2rf','--EMtype celltypeEM --npyDir','npyR2F/'),
    ('run_experiment_2_n_b E2nb','--regulized-type noregu --EMtype celltypeEM --useBothembedding --npyDir','npyN2B/'),
    ('run_experiment_2_n_e E2ne','--regulized-type noregu --EMtype celltypeEM --useGAEembedding --npyDir','npyN2E/'),
    ('run_experiment_2_n_f E2nf','--regulized-type noregu --EMtype celltypeEM --npyDir','npyN2F/'),
    ('run_experiment_2_g_b_AffinityPropagation E2gbA','--EMtype celltypeEM --clustering-method AffinityPropagation --useBothembedding --npyDir','npyG2B_AffinityPropagation/'),
    ('run_experiment_2_g_b_AgglomerativeClustering E2gbG','--EMtype celltypeEM --clustering-method AgglomerativeClustering --useBothembedding --npyDir','npyG2B_AgglomerativeClustering/'),
    ('run_experiment_2_g_b_Birch E2gbB','--EMtype celltypeEM --clustering-method Birch --useBothembedding --npyDir','npyG2B_Birch/'),
    ('run_experiment_2_g_b_KMeans E2gbK','--EMtype celltypeEM --clustering-method KMeans --useBothembedding --npyDir','npyG2B_KMeans/'),
    ('run_experiment_2_g_b_SpectralClustering E2gbS','--EMtype celltypeEM --clustering-method SpectralClustering --useBothembedding --npyDir','npyG2B_SpectralClustering/'),
    ('run_experiment_2_g_e_AffinityPropagation E2geA','--EMtype celltypeEM --clustering-method AffinityPropagation --useGAEembedding --npyDir','npyG2E_AffinityPropagation/'),
    ('run_experiment_2_g_e_AgglomerativeClustering E2geG','--EMtype celltypeEM --clustering-method AgglomerativeClustering --useGAEembedding --npyDir','npyG2E_AgglomerativeClustering/'),
    ('run_experiment_2_g_e_Birch E2geB','--EMtype celltypeEM --clustering-method Birch --useGAEembedding --npyDir','npyG2E_Birch/'),
    ('run_experiment_2_g_e_KMeans E2geK','--EMtype celltypeEM --clustering-method KMeans --useGAEembedding --npyDir','npyG2E_KMeans/'),
    ('run_experiment_2_g_e_SpectralClustering E2geS','--EMtype celltypeEM --clustering-method SpectralClustering --useGAEembedding --npyDir','npyG2E_SpectralClustering/'),
    ('run_experiment_2_g_f_AffinityPropagation E2gfA','--EMtype celltypeEM --clustering-method AffinityPropagation --npyDir','npyG2F_AffinityPropagation/'),
    ('run_experiment_2_g_f_AgglomerativeClustering E2gfG','--EMtype celltypeEM --clustering-method AgglomerativeClustering --npyDir','npyG2F_AgglomerativeClustering/'),
    ('run_experiment_2_g_f_Birch E2gfB','--EMtype celltypeEM --clustering-method Birch --npyDir','npyG2F_Birch/'),
    ('run_experiment_2_g_f_KMeans E2gfK','--EMtype celltypeEM --clustering-method KMeans --npyDir','npyG2F_KMeans/'),
    ('run_experiment_2_g_f_SpectralClustering E2gfS','--EMtype celltypeEM --clustering-method SpectralClustering --npyDir','npyG2F_SpectralClustering/'),
    ('run_experiment_2_r_b_AffinityPropagation E2rbA','--EMtype celltypeEM --clustering-method AffinityPropagation --useBothembedding --npyDir','npyR2B_AffinityPropagation/'),
    ('run_experiment_2_r_b_AgglomerativeClustering E2rbG','--EMtype celltypeEM --clustering-method AgglomerativeClustering --useBothembedding --npyDir','npyR2B_AgglomerativeClustering/'),
    ('run_experiment_2_r_b_Birch E2rbB','--EMtype celltypeEM --clustering-method Birch --useBothembedding --npyDir','npyR2B_Birch/'),
    ('run_experiment_2_r_b_KMeans E2rbK','--EMtype celltypeEM --clustering-method KMeans --useBothembedding --npyDir','npyR2B_KMeans/'),
    ('run_experiment_2_r_b_SpectralClustering E2rbS','--EMtype celltypeEM --clustering-method SpectralClustering --useBothembedding --npyDir','npyR2B_SpectralClustering/'),
    ('run_experiment_2_r_e_AffinityPropagation E2reA','--EMtype celltypeEM --clustering-method AffinityPropagation --useGAEembedding --npyDir','npyR2E_AffinityPropagation/'),
    ('run_experiment_2_r_e_AgglomerativeClustering E2reG','--EMtype celltypeEM --clustering-method AgglomerativeClustering --useGAEembedding --npyDir','npyR2E_AgglomerativeClustering/'),
    ('run_experiment_2_r_e_Birch E2reB','--EMtype celltypeEM --clustering-method Birch --useGAEembedding --npyDir','npyR2E_Birch/'),
    ('run_experiment_2_r_e_KMeans E2reK','--EMtype celltypeEM --clustering-method KMeans --useGAEembedding --npyDir','npyR2E_KMeans/'),
    ('run_experiment_2_r_e_SpectralClustering E2reS','--EMtype celltypeEM --clustering-method SpectralClustering --useGAEembedding --npyDir','npyR2E_SpectralClustering/'),
    ('run_experiment_2_r_f_AffinityPropagation E2rfA','--EMtype celltypeEM --clustering-method AffinityPropagation --npyDir','npyR2F_AffinityPropagation/'),
    ('run_experiment_2_r_f_AgglomerativeClustering E2rfG','--EMtype celltypeEM --clustering-method AgglomerativeClustering --npyDir','npyR2F_AgglomerativeClustering/'),
    ('run_experiment_2_r_f_Birch E2rfB','--EMtype celltypeEM --clustering-method Birch --npyDir','npyR2F_Birch/'),
    ('run_experiment_2_r_f_KMeans E2rfK','--EMtype celltypeEM --clustering-method KMeans --npyDir','npyR2F_KMeans/'),
    ('run_experiment_2_r_f_SpectralClustering E2rfS','--EMtype celltypeEM --clustering-method SpectralClustering --npyDir','npyR2F_SpectralClustering/'),
    ('run_experiment_2_n_b_AffinityPropagation E2nbA','--regulized-type noregu --EMtype celltypeEM --clustering-method AffinityPropagation --useBothembedding --npyDir','npyN2B_AffinityPropagation/'),
    ('run_experiment_2_n_b_AgglomerativeClustering E2nbG','--regulized-type noregu --EMtype celltypeEM --clustering-method AgglomerativeClustering --useBothembedding --npyDir','npyN2B_AgglomerativeClustering/'),
    ('run_experiment_2_n_b_Birch E2nbB','--regulized-type noregu --EMtype celltypeEM --clustering-method Birch --useBothembedding --npyDir','npyN2B_Birch/'),
    ('run_experiment_2_n_b_KMeans E2nbK','--regulized-type noregu --EMtype celltypeEM --clustering-method KMeans --useBothembedding --npyDir','npyN2B_KMeans/'),
    ('run_experiment_2_n_b_SpectralClustering E2nbS','--regulized-type noregu --EMtype celltypeEM --clustering-method SpectralClustering --useBothembedding --npyDir','npyN2B_SpectralClustering/'),
    ('run_experiment_2_n_e_AffinityPropagation E2neA','--regulized-type noregu --EMtype celltypeEM --clustering-method AffinityPropagation --useGAEembedding --npyDir','npyN2E_AffinityPropagation/'),
    ('run_experiment_2_n_e_AgglomerativeClustering E2neG','--regulized-type noregu --EMtype celltypeEM --clustering-method AgglomerativeClustering --useGAEembedding --npyDir','npyN2E_AgglomerativeClustering/'),
    ('run_experiment_2_n_e_Birch E2neB','--regulized-type noregu --EMtype celltypeEM --clustering-method Birch --useGAEembedding --npyDir','npyN2E_Birch/'),
    ('run_experiment_2_n_e_KMeans E2neK','--regulized-type noregu --EMtype celltypeEM --clustering-method KMeans --useGAEembedding --npyDir','npyN2E_KMeans/'),
    ('run_experiment_2_n_e_SpectralClustering E2neS','--regulized-type noregu --EMtype celltypeEM --clustering-method SpectralClustering --useGAEembedding --npyDir','npyN2E_SpectralClustering/'),
    ('run_experiment_2_n_f_AffinityPropagation E2nfA','--regulized-type noregu --EMtype celltypeEM --clustering-method AffinityPropagation --npyDir','npyN2F_AffinityPropagation/'),
    ('run_experiment_2_n_f_AgglomerativeClustering E2nfG','--regulized-type noregu --EMtype celltypeEM --clustering-method AgglomerativeClustering --npyDir','npyN2F_AgglomerativeClustering/'),
    ('run_experiment_2_n_f_Birch E2nfB','--regulized-type noregu --EMtype celltypeEM --clustering-method Birch --npyDir','npyN2F_Birch/'),
    ('run_experiment_2_n_f_KMeans E2nfK','--regulized-type noregu --EMtype celltypeEM --clustering-method KMeans --npyDir','npyN2F_KMeans/'),
    ('run_experiment_2_n_f_SpectralClustering E2nfS','--regulized-type noregu --EMtype celltypeEM --clustering-method SpectralClustering --npyDir','npyN2F_SpectralClustering/')
]

# datasetNameList = [
#     'MMPbasal_2000',
#     'MMPbasal_2000 --discreteTag',
#     'MMPbasal_2000_LTMG',
#     '4.Yan --n-clusters 7',
#     '4.Yan --discreteTag --n-clusters 7',
#     '4.Yan_LTMG --n-clusters 7',
#     '5.Goolam --n-clusters 5',
#     '5.Goolam --discreteTag --n-clusters 5',
#     '5.Goolam_LTMG --n-clusters 5',
#     '7.Deng --n-clusters 10',
#     '7.Deng --discreteTag --n-clusters 10',
#     '7.Deng_LTMG --n-clusters 10'
#     '8.Pollen --n-clusters 11',
#     '8.Pollen --discreteTag --n-clusters 11',
#     '8.Pollen_LTMG --n-clusters 11',
#     '11.Kolodziejczyk --n-clusters 3',
#     '11.Kolodziejczyk --discreteTag --n-clusters 3',
#     '11.Kolodziejczyk_LTMG --n-clusters 3'
# ]

datasetNameList = [
    'T1000 --n-clusters 3',
    'T1000 --discreteTag --n-clusters 3',
    'T1000_LTMG --n-clusters 3',
    'T2000 --n-clusters 3',
    'T2000 --discreteTag --n-clusters 3',
    'T2000_LTMG --n-clusters 3',
    'T4000 --n-clusters 3',
    'T4000 --discreteTag --n-clusters 3',
    'T4000_LTMG --n-clusters 3',
    'T8000 --n-clusters 3',
    'T8000 --discreteTag --n-clusters 3',
    'T8000_LTMG --n-clusters 3'
]

# generate sbatch files:
for item in methodsList:
    batchInfo,scGNNparam,outDirStr = item
    tmp = batchInfo.split()
    tmpstr1=tmp[0]
    tmpstr2=tmp[1]
    imputeStr = ''
    if args.imputeMode:
        tmpstr1 = tmpstr1.replace('run_experiment','run_experimentImpute')
        tmpstr2 = "I"+tmpstr2[1:]
        imputeStr = ' --imputeMode  '
        outDirStr = "npyImpute"+outDirStr[3:]
    outputFilename = args.outputDir + tmpstr1
    abbrStr = tmpstr2   

    count = 1
    for datasetName in datasetNameList:
        commandLine = "python3 -W ignore main.py --datasetName "+datasetName+" "+scGNNparam+" "+outDirStr+imputeStr+"\n"
        outStr = templateStr1 + abbrStr + "_" + str(count) + templateStr2 + commandLine + "\n"
        with open(outputFilename+"_"+str(count)+".sh",'w') as fw:
            fw.write(outStr)
            fw.close()
        count += 1
