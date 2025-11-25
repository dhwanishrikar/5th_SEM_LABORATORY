import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator

data=pd.read_csv('heart.csv')
subset_data=data[['age','sex','cp','thalach','exang','oldpeak','target']]
print(subset_data.head())

model=BayesianModel([('age','target'),
                     ('sex','target'),
                     ('cp','target'),
                     ('thalach','target'),
                     ('exang','target'),
                     ('oldpeak','target')
                    ])
model.fit(subset_data, estimator=MaximumLikelihoodEstimator)
inference=VariableElimination(model)
evidence={'age':55,'sex':1,'cp':3,'thalach':150,'exang':0,'oldpeak':2.3}
result=inference.query(variables=['target'], evidence=evidence)
print(result)
