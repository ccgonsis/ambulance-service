import ciw
import AS_setting
import numpy as np

# similar with first model
def dist_in_arriving(num):
    if num == 0:
        return ciw.dists.NoArrivals()
    else:
        return ciw.dists.Exponential(num)

def dist_in_serving(num):
    if num == 0:
        return ciw.dists.Deterministic(0.0)
    else:
        return ciw.dists.Exponential(num)

arrival_list = [dist_in_arriving(post) for post in AS_setting.emer_time]
serving_list = [dist_in_serving(address) for address in AS_setting.des_time]

# using scene place capability means that it represent the busiest situation in AS system
service_num = AS_setting.SCE_capability + AS_setting.hospital_setting

b = AS_setting.STD_metrix

N = ciw.create_network(
    arrival_distributions= arrival_list,
    service_distributions= serving_list,
    routing=b,
    number_of_servers=service_num
)

# we just only get average waiting time in this part
A_waiting_time = []
for num_node in range(54, 108):
    for trial in range(10):
        ciw.seed(trial)
        Q = ciw.Simulation(N)
        Q.simulate_until_max_time(720)
        recs = Q.get_all_records()
        num_completed = len([r for r in recs if r.node == int(num_node)])
        waiting_time = [r.waiting_time for r in recs if r.node == int(num_node)]
        if waiting_time == []:
            waiting_time = [0.0]

    print(waiting_time)
    A_waiting_time.append(np.mean(waiting_time))

print('average waiting time = ', A_waiting_time)

