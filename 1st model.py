import ciw
import AS_setting

# ambulance simulation time (unit: an ambulance per hours.
# for example, 12 means the first post will send an ambulance to a scene place per 12 hours)
am = [12, 8, 4.76] + [0 for _ in range(53)]
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

# arrival and service queue according to ATS simulation time
# arrival time means the simulation frequency patients call the ambulance
# service time means the travelling time the ambulances need to reach scene place
# Unit is same with ambulance simulation time.
arrival = [dist_in_arriving(i) for i in am]
service = [dist_in_serving(_) for _ in AS_setting.ATS_time]

# building the network
N = ciw.create_network(
    arrival_distributions=arrival,
    service_distributions=service,
    routing=AS_setting.routing_AM_TO_SCE,
    number_of_servers=[9, 5, 8] + AS_setting.SCE_capability,
    queue_capacities=[22, 22, 22] + AS_setting.SCE_capability
)


# get simulation results
# simulation limit: 1 month

completed_custs = [] # record the num of patients in each scene place
SCE_count = []  # record the num of patients in all scene place

A_utility = []  # average utility of Ambulance in every scene place (utility means the full load probability in scene place)
A_waiting_time = [] # average waiting time in every scene place
hindering_matrix = [] # the probability when the patients' waiting time is over 1 hour in a scene place
for num_node in range(4, 57):
    utility = []
    for trial in range(10):
        ciw.seed(trial)
        Q = ciw.Simulation(N)
        Q.simulate_until_max_time(720)
        recs = Q.get_all_records()
        num_completed = len([r for r in recs if r.node == int(num_node)])
        completed_custs.append(num_completed)
        waiting_time = [r.waiting_time for r in recs if r.node == int(num_node)]
        if waiting_time == []:
            waiting_time = [0.0]
        utility.append(Q.transitive_nodes[num_node].server_utilisation)

    print(waiting_time)
    A_utility.append(sum(utility)/len(utility))
    A_waiting_time.append(sum(waiting_time)/len(waiting_time))

    SCE_count.append(sum(completed_custs) / len(completed_custs))

    blocked_num = sum(j>1 for j in waiting_time)
    blocked_prob = blocked_num/len(waiting_time)
    hindering_matrix.append(blocked_prob)

print('average utility matrix = ', A_utility)
print('hindering probability =', hindering_matrix)
print('average waiting time = ', A_waiting_time)
print('patients numbers is: ', SCE_count)

# hindering factor in a scene place = average utility * hindering probability
# if hindering factor is less than 0.1 in a scene place, it means that the AS is 'good' in that place.















