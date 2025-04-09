def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    bridge_weight = 0

    while truck_weights or bridge_weight > 0:
        time += 1
        bridge_weight -= bridge.pop(0)

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)

    return time