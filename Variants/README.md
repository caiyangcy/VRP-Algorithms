# Variants Intro

This is a short intro on difference types of variants of VRP. This may be different from the overview image. This repo only focus on CVRP so far (may added others).

## Capacitated VRP(CVRP)

The vehicle has a limited capacity.

## VRP with Time Window(VRPTW)

Each customer is only available in a specific duration. Meanwhile there is also a restriction on the time intervel of depot which is called the scheduling horizon and the delivery must start and end within this time interval.

## VRP with Pick-Up and Delivering(VRPPD)
There is a chance that some customers return the commodities.

It’s needed to take into account that the goods that customers return to the deliver vehicle must fit into it. This restriction make the planning problem more difficult and can lead to bad utilization of the vehicles capacities, increased travel distances or a need for more vehicles.

Another usual simplification is to consider that every vehicle must deliver all the commodities before picking up any goods.

## VRP with Backhauls(VRPB)

Customers can demand or return some commodities. 

VRPB is similar to VRPPD with the restriction that in the case of VRPB all deliveries for each route must be completed before any pickups are made.

The critical assumption in that all deliveries must be made on each route before any pickups can be made. This arises from the fact that the vehicles are rear-loaded, and rearrangement of the loads on the tracks at the delivery points is not deemed economical or feasible. The quantities to be delivered and picked-up are fixed and known in advance.

## Stochastic VRP(SVRP)

one or several components of the problem are random. There three major cases: random customer(customer is present or not), random time window(random service time) and random demand(demands of customers are random).

## Multiple Depot VRP(MDVRP)

A MDVRP requires the assignment of customers to depots. A fleet of vehicles is based at each depot. Each vehicle originate from one depot, service the customers assigned to that depot, and return to the same depot. Each cluster is solved independently.

## Split Delivery VRP(SDVRP)

This same customer can be delivered by multiple times This relaxation is very important if the sizes of the customer orders are as big as the capacity of a vehicle. Note that currently the codings are all based on Non-split delivery.
