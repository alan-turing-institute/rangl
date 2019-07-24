#!/usr/bin/env python

from rangl import Environment, Policy


def A(t_array, env):
    """Example linear A(t) function"""
    A_0 = -3.5
    threshold = env.THRESHOLD
    terminal = env.TERMINAL

    A_ = A_0 + (threshold - A_0) * t_array / terminal
    return A_


def B(t_array, env):
    """Example linear B(t) function"""
    B_0 = -0.5
    threshold = env.THRESHOLD
    terminal = env.TERMINAL

    B_ = B_0 + (threshold - B_0) * t_array / terminal
    return B_


def rule(t_array, X_array, env):
    A_array = A(t_array, env)
    B_array = B(t_array, env)

    spill_pred = False
    for t_, X_, A_, B_ in zip(t_array, X_array, A_array, B_array):
        t_pred = t_
        if X_ <= A_:
            spill_pred = False
            return t_pred, spill_pred
        if X_ > B_:
            spill_pred = True
            return t_pred, spill_pred


env = Environment()
policy = Policy(rule)


for i in range(10):
    env.render()
    score = env.score(policy)
    print(f"score: {score}")

