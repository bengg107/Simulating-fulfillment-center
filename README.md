# Simulating-fulfillment-center

In this project, you are going to develop a simulator to get a distribution of travel distances to fulfill a day's worth of orders. Here are some assumptions and particulars about your retail establishment: 
1. You have $N$ products. 
2. On a given day, you have $M$ orders. 
3. The $i$-th order is a list of length $n_i$ products (2 of one product means the product number appears twice consecutively), $i=1,\ldots, M$. 
4. Some products are more popular than others, so you need to take this into account when you simulate the orders for the day. 
5. Assume that the shape of the warehouse in which the products are stored is square, and all $N$ products are lined up along four walls (same number per wall). 
6. The picker, a robot, receives an order at the Southeast corner of the building and picks the product in that order, and returns to the Southeast corner. 
Your task is to measure the distance travelled by the robot to fulfill all the orders for that day. Perform many simulations to get a distribution of distances. 

Play with parameters $N$ and $M$ to see if the distribution is sensitive to them. 

Does it matter how the $N$ products are arranged in the warehouse? 