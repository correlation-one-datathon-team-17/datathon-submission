import argparse
from datetime import datetime
import numpy as np
import csv
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import argparse

'''
Read in csv
'''

def read_dates(filename):
    dataset = None
    with open(filename, 'rU') as f:
        dataset = f.readline().strip().split(',')[1:]
    return dataset


'''
Sum up date freqs for weekdays and weekends

result: [borough, uber_freq__wd_total, uber_freq__wk_total, green_trip_freq_wd_total, green_trip_freq_wk_total, yellow_cab_freq_wd_total, yellow_cab_freq_wk_total, median_income, median_age]
'''

def plot_freq_sum(x, y):
    plot_2d(x, y, 'date', 'freq_sum', 'uber_freq.png')

def combine_weekday_weekend(input_file):
    # d = read_file(input_file)
    start_date = datetime.strptime("2017-03-25", "%Y-%m-%d")
    # first_weekday = start_date.weekday()
    # print first_weekday
    # data = np.asarray(data[2:])) #, dtype=np.float64)
    # print data
    # x = np.arange(90)

    dates = read_dates(input_file)
    x = [datetime.strptime(d,"%m/%d/%Y").date() for d in dates]

    data = np.genfromtxt(input_file, dtype=float, delimiter=',')
    # print data.shae
    fig = plt.figure()
    output_path = 'uber_freq_.png'
    # print data.shape
    # print data[0,:]

    tag = ['Staten_Island', 'Brooklyn', 'Bronx', 'Manhattan', 'Queens']
    color = ['g', 'c', 'm', 'b', 'r']
    nsteps = 8
    cmap = cm.autumn

    for i in range(1,6):
        print i
        y = np.log(data[i,1:])#[0:20]
        min_index = np.argmin(y)
        print np.min(y), x[min_index]
        # markers = []
        # markers.append(x[min_index])

        ax = fig.add_subplot(111)
        ax.set_xlabel('date')
        ax.set_ylabel('freq_sum(log2)')
        line = plt.plot(x, y, label=tag[i-1])
        # plt.setp(line, color=color[i-1], label=tag[i-1], linewidth=2.0)
        plt.tight_layout()


    plt.legend(loc='upper right', fontsize='small', ncol=3)
    # plt.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
    # plt.plot(xs, ys, '-gD', markevery=markers_on)

    plt.ylim(ymax=13)
    plt.savefig(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="Input file")
    # parser.add_argument("-o", "--out", type=str, default="mountain.png", help="Output file")
    args = parser.parse_args()
    combine_weekday_weekend(args.file)
