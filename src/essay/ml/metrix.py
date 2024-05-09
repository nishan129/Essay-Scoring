from sklearn.metrics import cohen_kappa_score
from src.essay.exception import ModelException
import sys


def compute_metrics_for_regression(eval_pred):
    try:
        
    
        predictions, labels = eval_pred
        qwk = cohen_kappa_score(labels, predictions.clip(0,5).round(0), weights='quadratic')
        results = {
            'qwk': qwk
        }
        return results
    except Exception as e:
        raise ModelException(e,sys)