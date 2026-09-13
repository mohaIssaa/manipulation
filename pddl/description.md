In defaultMethod_performance.py, the performance by default method using in exercise has been evaluated and as a baseline to compare with outcomes from diffusion.

In evaluate_diffusion.py, it is the process to evaluate and test the result from diffusion models. Currently, only action validation is the rule to activate the replan.

In init.py, there are parameters for running test loop.
In reset.py, it is the reset function for testing each result.
testData.py, works on a one-time data processing for entire, small testing set from training set.

todo: more rules introducing bridge, such as eval_ik, corridor_blocked are the next step or advanced rules to be extended. They can be placed separately as a rule set file or in evaluate_diffusion.py directly.
