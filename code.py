import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import statistics

data = pd.read_csv("mathscore.csv")
data_list = data["Math_score"].to_list()

mean = statistics.mean(data_list)
stdev = statistics.stdev(data_list)

print("Mean = ", mean, ", Standard Deviation = ", stdev)
def random_sample(counter):
    sample_space = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data_list)-1)
        value = data_list[random_index]
        sample_space.append(value)
    sample_mean = statistics.mean(sample_space)
    return sample_mean

mean_list = []

for i in range(0, 1000):
    mean_set = random_sample(100)
    mean_list.append(mean_set)

sample_mean = statistics.mean(mean_list)
sample_stdev = statistics.stdev(mean_list)
print("Sample Mean = ", sample_mean, ", Sample Standard Deviation = ", sample_stdev)

figure = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
figure.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.2], mode="lines", name="Mean"))
figure.show()