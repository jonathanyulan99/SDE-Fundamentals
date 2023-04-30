'''
Imagine you are creating an algorithm for currency trading. Now you have a prototype which handles trading of a single currency. Each day, it can sell or buy exactly one unit of the currency or do nothing.

You are given rates, an array of positive integers where rates[i] represents the currency price on the ith day. You're also given strategy, an array of -1s, 0s, and 1s, where strategy[i] represents what operation the algorithm should perform on the ith day:

-1 represents the buy operation,
0 represents the hold operation, meaning nothing is bought or sold,
1 represents the sell operation.
You're also given an integer k, which is guaranteed to be even.

In order to improve the algorithm's performance, you may change the strategy in the following way:

Choose a range of exactly k consecutive elements,
Set elements of the first half of the chosen range to 0,
Set elements of the second half of the chosen range to 1.
Your task is to choose the range optimally to maximize the algorithm's total profit. The profit is defined as the sum of all selling rates minus the sum of all buying rates (in other words, the difference between the end and start amount). The profit may be negative in case the end amount is lower than the start amount.

NOTE: Assume it is always possible to perform buy and sell operations, meaning you always have enough currency and budget.





'''