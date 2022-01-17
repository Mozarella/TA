import statistics
def Createdataset(filePPG):
    min = filePPG.min()
    max = filePPG.max()
    mean = statistics.mean(filePPG)
    med = statistics.median(filePPG)
    std = statistics.stdev(filePPG)
    return (min,max,mean,med,std)