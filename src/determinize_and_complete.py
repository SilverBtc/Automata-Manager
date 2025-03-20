from src.determinize import determinize
from src.complete import complete

def determinize_and_complete(fa):
    det_fa = determinize(fa)
    comp_fa = complete(det_fa)
    return comp_fa