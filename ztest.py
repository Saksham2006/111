import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import statistics

# 1st Stdev, 2nd Stdev, 3rd Stdev

raw_data = pd.read_csv("mathscore.csv")
raw_data_list = raw_data["Math_score"].to_list()

def random_sample(counter):
    sample_space = []
    for i in range(0, counter):
        random_index = random.randint(0, len(raw_data_list)-1)
        value = raw_data_list[random_index]
        sample_space.append(value)
    sample_mean = statistics.mean(sample_space)
    return sample_mean

mean_list = []

for i in range(0, 1000):
    mean_set = random_sample(100)
    mean_list.append(mean_set)

stdev_raw = statistics.stdev(mean_list)
mean_raw = statistics.mean(mean_list)

print("Stdev raw = ", stdev_raw, ". Mean raw = ", mean_raw)

first_stdev_start, first_stdev_end = mean_raw - stdev_raw, mean_raw + stdev_raw  
second_stdev_start, second_stdev_end = mean_raw - (2*stdev_raw), mean_raw + (2*stdev_raw)  
third_stdev_start, third_stdev_end = mean_raw - (3*stdev_raw), mean_raw + (3*stdev_raw)

int1_data = pd.read_csv("interventions/one.csv")
int1_list = int1_data["Math_score"].to_list()
int1_mean = statistics.mean(int1_list)
print("Int1 mean = ", int1_mean)
figure = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
figure.add_trace(go.Scatter(x=[mean_raw, mean_raw], y=[0, 0.2], mode="lines", name="Mean"))
figure.add_trace(go.Scatter(x=[int1_mean, int1_mean], y=[0, 0.2], mode="lines", name="Mean of Students who used MathLab"))
figure.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.2], mode="lines", name="Standard Deviation 1 - End"))
figure.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.2], mode="lines", name="Standard Deviation 2 - End"))
figure.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.2], mode="lines", name="Standard Deviation 3 - End"))
figure.show()

int2_data = pd.read_csv("interventions/two.csv")
int2_list = int2_data["Math_score"].to_list()
int2_mean = statistics.mean(int2_list)
print("Int2 mean = ", int2_mean)
figure = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
figure.add_trace(go.Scatter(x=[mean_raw, mean_raw], y=[0, 0.2], mode="lines", name="Mean"))
figure.add_trace(go.Scatter(x=[int2_mean, int2_mean], y=[0, 0.2], mode="lines", name="Mean of Students who used the app"))
figure.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.2], mode="lines", name="Standard Deviation 1 - End"))
figure.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.2], mode="lines", name="Standard Deviation 2 - End"))
figure.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.2], mode="lines", name="Standard Deviation 3 - End"))
figure.show()

int3_data = pd.read_csv("interventions/three.csv")
int3_list = int3_data["Math_score"].to_list()
int3_mean = statistics.mean(int3_list)
print("Int3 mean = ", int3_mean)
figure = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
figure.add_trace(go.Scatter(x=[mean_raw, mean_raw], y=[0, 0.2], mode="lines", name="Mean"))
figure.add_trace(go.Scatter(x=[int3_mean, int3_mean], y=[0, 0.2], mode="lines", name="Mean of Students who attended extra classes"))
figure.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.2], mode="lines", name="Standard Deviation 1 - End"))
figure.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.2], mode="lines", name="Standard Deviation 2 - End"))
figure.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.2], mode="lines", name="Standard Deviation 3 - End"))
figure.show()


zscore_1 = (mean_raw - int1_mean)/stdev_raw
zscore_2 = (mean_raw - int2_mean)/stdev_raw
zscore_3 = (mean_raw - int3_mean)/stdev_raw

print("z-score 1 = ", zscore_1)
print("z-score 2 = ", zscore_2)
print("z-score 3 = ", zscore_3)